--------------------------------
[Version]
--------------------------------
v13


--------------------------------
[Overview]
--------------------------------
These code samples show how to use Python to call APIs.

--------------------------------
[Contents]
--------------------------------

  - conf/config.ini          : Config files to specify Ids.

  - report_sample.py       : Examples of creating report.

--------------------------------
[Configuration]
--------------------------------
Install the software below to organize environment.

1. Python 3.8.13 or above
2. OpenAPI generator 6.1.0
3. Set the following environment variables.
   - ACCOUNT_ID          : Account ID (required)
   - ACCESS_TOKEN        : Access token (required)
   - BASE_ACCOUNT_ID     : Account ID that should be specified in 'x-z-base-account-id' header. (required)

--------------------------------
[How to execute Sample Code]
--------------------------------
Execute OpenAPI Generator and generate client for Python.  
*There is a difference in the execution method of OpenAPI Generator depending on the installation. The example below is for Homebrew installation.
```
openapi-generator generate -i https://yahoojp-marketing.github.io/ads-search-api-documents/design/v13/Route.yaml -g python -o ./
```

Install setup.py directly under.
```
python setup.py install --user
```

Example
```
python report_sample.py
```

--------------------------------
NOTICE：　Yahoo! JAPAN Ads Search Ads API - For use of sample code
--------------------------------

The sample code of Yahoo! JAPAN Ads API is provided to API users only who concluded the contract of "Application to Use Yahoo! JAPAN Ads API" with LY Corporation.

Additionally, please note that LY Corporation may change the contents and the specification of the sample code, and may discontinue providing the sample code without any notice.
