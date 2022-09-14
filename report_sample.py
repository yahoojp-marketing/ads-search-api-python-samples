# Copyright (C) 2020 Yahoo Japan Corporation. All Rights Reserved.

import time
import sys
import configparser
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
config_ini = configparser.ConfigParser()
config_ini.read('conf/config.ini', encoding='utf-8')

configuration = openapi_client.Configuration()
# Configure OAuth2 access token for authorization: oAuth
configuration.access_token = config_ini['DEFAULT']['access_token']

# Defining host is optional and default to https://ads-search.yahooapis.jp/api/v9
configuration.host = "https://ads-search.yahooapis.jp/api/v9"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ReportDefinitionServiceApi(api_client)
    job_id = 0

    # Add
    report_definition = openapi_client.ReportDefinition(
        report_date_range_type=openapi_client.ReportDefinitionServiceReportDateRangeType.YESTERDAY,
        report_name="sample",
        fields=["IMPS","CLICKS"],
        report_type=openapi_client.ReportDefinitionServiceReportType.ACCOUNT
    )

    report_definition_service_operation = openapi_client.ReportDefinitionServiceOperation(
        account_id=config_ini['DEFAULT']['account_id'],
        operand=[report_definition]
    ) # ReportDefinitionServiceOperation |  (optional)

    try:
        api_response = api_instance.report_definition_service_add_post(report_definition_service_operation=report_definition_service_operation)
        job_id = api_response.rval.values[0].report_definition.report_job_id
    except ApiException as e:
        print("Exception when calling ReportDefinitionServiceApi->report_definition_service_add_post: %s\n" % e)

    # Get
    report_definition_service_selector = openapi_client.ReportDefinitionServiceSelector(
        account_id=config_ini['DEFAULT']['account_id'],
        report_job_ids=[job_id]
    ) # ReportDefinitionServiceSelector |  (optional)

    try:
        api_response = api_instance.report_definition_service_get_post(report_definition_service_selector=report_definition_service_selector)

        num = 0
        while api_response.rval.values[0].report_definition.report_job_status != openapi_client.ReportDefinitionServiceReportJobStatus.COMPLETED:
            time.sleep(1)
            num += 1
            if num >= 100:
                sys.exit(1)
            api_response = api_instance.report_definition_service_get_post(report_definition_service_selector=report_definition_service_selector)

    except ApiException as e:
        print("Exception when calling ReportDefinitionServiceApi->report_definition_service_get_post: %s\n" % e)

    # download
    report_definition_service_download_selector = openapi_client.ReportDefinitionServiceDownloadSelector(
        account_id=config_ini['DEFAULT']['account_id'],
        report_job_id=job_id
    ) # ReportDefinitionServiceDownloadSelector |  (optional)

    try:
        api_response = api_instance.report_definition_service_download_post(
            report_definition_service_download_selector=report_definition_service_download_selector,
            _preload_content=False) # OpenAPI Python Bug 4847
        with open("download/sample.scv", mode="wb") as f:
            f.write(api_response.read())

    except ApiException as e:
        print("Exception when calling ReportDefinitionServiceApi->report_definition_service_download_post: %s\n" % e)

