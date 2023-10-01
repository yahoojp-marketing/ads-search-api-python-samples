# Copyright (C) 2023 LY Corporation. All Rights Reserved.

import time
import sys
import configparser
import openapi_client
import os
from openapi_client.api.report_definition_service_api import ReportDefinitionServiceApi
from openapi_client.model.report_definition import ReportDefinition
from openapi_client.model.report_definition_service_download_selector import ReportDefinitionServiceDownloadSelector
from openapi_client.model.report_definition_service_operation import ReportDefinitionServiceOperation
from openapi_client.model.report_definition_service_report_date_range_type import ReportDefinitionServiceReportDateRangeType
from openapi_client.model.report_definition_service_report_job_status import ReportDefinitionServiceReportJobStatus
from openapi_client.model.report_definition_service_report_type import ReportDefinitionServiceReportType
from openapi_client.model.report_definition_service_selector import ReportDefinitionServiceSelector
from openapi_client.rest import ApiException
from pprint import pprint

class EnvInterpolation(configparser.BasicInterpolation):

    def before_get(self, parser, section, option, value, defaults):
        return os.path.expandvars(value)

config_ini = configparser.ConfigParser(interpolation=EnvInterpolation())
config_ini.read('conf/config.ini', encoding='utf-8')

configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: oAuth
configuration.access_token = config_ini['DEFAULT']['access_token']

# Defining host is optional and default to https://ads-search.yahooapis.jp/api/v12
configuration.host = "https://ads-search.yahooapis.jp/api/v12"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ReportDefinitionServiceApi(api_client)
    job_id = 0
    base_account_id=int(config_ini['DEFAULT']['base_account_id'])

    # Add
    report_definition = ReportDefinition(
        report_date_range_type=ReportDefinitionServiceReportDateRangeType('YESTERDAY'),
        report_name="sample",
        fields=["IMPS","CLICKS"],
        report_type=ReportDefinitionServiceReportType('ACCOUNT')
    )

    report_definition_service_operation = ReportDefinitionServiceOperation(
        account_id=int(config_ini['DEFAULT']['account_id']),
        operand=[report_definition]
    ) # ReportDefinitionServiceOperation |  (optional)

    try:
        api_response = api_instance.report_definition_service_add_post(base_account_id, report_definition_service_operation=report_definition_service_operation)
        job_id = api_response.rval.values[0].report_definition.report_job_id
    except ApiException as e:
        print("Exception when calling ReportDefinitionServiceApi->report_definition_service_add_post: %s\n" % e)

    # Get
    report_definition_service_selector = ReportDefinitionServiceSelector(
        account_id=int(config_ini['DEFAULT']['account_id']),
        report_job_ids=[job_id]
    ) # ReportDefinitionServiceSelector |  (optional)

    try:
        api_response = api_instance.report_definition_service_get_post(base_account_id, report_definition_service_selector=report_definition_service_selector)

        num = 0
        while api_response.rval.values[0].report_definition.report_job_status != ReportDefinitionServiceReportJobStatus('COMPLETED'):
            time.sleep(1)
            num += 1
            if num >= 100:
                sys.exit(1)
            api_response = api_instance.report_definition_service_get_post(base_account_id, report_definition_service_selector=report_definition_service_selector)

    except ApiException as e:
        print("Exception when calling ReportDefinitionServiceApi->report_definition_service_get_post: %s\n" % e)

    # download
    report_definition_service_download_selector = ReportDefinitionServiceDownloadSelector(
        account_id=int(config_ini['DEFAULT']['account_id']),
        report_job_id=job_id
    ) # ReportDefinitionServiceDownloadSelector |  (optional)

    try:
        api_response = api_instance.report_definition_service_download_post(
            base_account_id,
            report_definition_service_download_selector=report_definition_service_download_selector,
            _preload_content=False) # OpenAPI Python Bug 4847
        with open("download/sample.scv", mode="wb") as f:
            f.write(api_response.read())

    except ApiException as e:
        print("Exception when calling ReportDefinitionServiceApi->report_definition_service_download_post: %s\n" % e)
