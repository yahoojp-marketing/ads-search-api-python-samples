--------------------------------
[Version]
Please refer to the following for the latest version.
- [API Reference](https://ads-developers.yahoo.co.jp/reference/en)
- [Release Note](https://ads-developers.yahoo.co.jp/en/ads-api/developers-guide/release-note.html)


--------------------------------
[Overview]
--------------------------------
These code samples show how to use Python to call APIs.

--------------------------------
[Contents]
--------------------------------
- conf/config.ini     : Config files to specify Ids.
- report_sample.py    : Examples of creating report.

--------------------------------
[Configuration]
--------------------------------
Install the software below to organize environment.

1. Python 3.10 or above
2. OpenAPI generator 6.1.0
3. Set the following environment variables.
   - ACCOUNT_ID          : Account ID (required)
   - ACCESS_TOKEN        : Access token (required)
   - BASE_ACCOUNT_ID     : Account ID that should be specified in 'x-z-base-account-id' header. (required)

--------------------------------
[How to execute Sample Code]
--------------------------------
Execute OpenAPI Generator and generate client for Python. Please specify the latest version in ${VERSION}. 
*There is a difference in the execution method of OpenAPI Generator depending on the installation. The example below is for Homebrew installation.
```
openapi-generator generate -i https://yahoojp-marketing.github.io/ads-search-api-documents/design/${VERSION}/Route.yaml -g python -o ./
```

Install the dependency libraries.
```
python -m pip install -r requirements.txt
```

Install the local package.
```
python -m pip install .
```

Example
```
python report_sample.py
```

On the first execution, modifications to `report_sample.py` are required. Please specify the desired version for `${VERSION}`.  
```diff
- configuration.host = "https://ads-search.yahooapis.jp/api/${VERSION}"
+ configuration.host = "https://ads-search.yahooapis.jp/api/vXX"
```

--------------------------------
NOTICE：　LY Ads Search Ads API - For use of sample code
--------------------------------

The sample code of LY Ads API is provided to API users only who concluded the contract of "Application to Use LY Ads API" with LY Corporation.

Additionally, please note that LY Corporation may change the contents and the specification of the sample code, and may discontinue providing the sample code without any notice.
