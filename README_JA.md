--------------------------------
【バージョン】
--------------------------------
最新バージョンについては以下を参照ください。
- [APIリファレンス](https://ads-developers.yahoo.co.jp/reference/)
- [リリースノート](https://ads-developers.yahoo.co.jp/ja/ads-api/developers-guide/release-note.html)


--------------------------------
【概要】
--------------------------------
このサンプルプログラムは、Pythonを使用して各APIを呼び出す処理のサンプルです。

--------------------------------
【内容物】
--------------------------------

  - conf/config.ini          : 各種IDを記述する設定ファイルです。

  - report_sample.py       : レポートのサンプルです。

--------------------------------
【環境設定】
--------------------------------
Python環境を構築するために、以下をインストールしてください。

1. Python 3.8.13以上のバージョン
2. OpenAPI generator 6.1.0
3. 以下の環境変数を設定します。
   - ACCOUNT_ID          : アカウントIDを記述してください(必須)。
   - ACCESS_TOKEN        : アクセストークンを記述してください(必須)。
   - BASE_ACCOUNT_ID     : x-z-base-account-id ヘッダーで指定するアカウントID(必須)。

--------------------------------
【実行】
--------------------------------
OpenAPI Generatorを実行しPython用のclientを生成します。${VERSION}には最新バージョンを指定してください。
※インストール方法によってOpenAPI Generatorの実行方法に違いがあります。以下の例はHomebrewでインストールした場合です。
```
openapi-generator generate -i https://yahoojp-marketing.github.io/ads-search-api-documents/design/${VERSION}/Route.yaml -g python -o ./
```

直下にsetup.pyをインストールします。
```
python setup.py install --user
```

実行例
```
python report_sample.py
```

--------------------------------
ご注意：　Yahoo!広告 検索広告 API - サンプルコードの利用に関して
--------------------------------

LINEヤフー株式会社の提供するAPIに関するサンプルコードは、別途LINEヤフー株式会社との間で締結いただいた当該APIの提供に関する契約に基づき、APIユーザー様に提供されるものであり、LINEヤフー株式会社との間で当該契約を締結いただいていない場合は、サンプルコードをご利用いただけません。
また、APIユーザー様に予め通知することなく、サンプルコードの内容や仕様の変更または提供の停止もしくは中止をする場合があります。ご了承のうえご利用ください。
