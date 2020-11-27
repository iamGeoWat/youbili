# -*- coding: utf-8 -*-

import os
from google.oauth2 import service_account
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    credentials = service_account.Credentials.from_service_account_file(
        'bot_key.json')
    print(credentials)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        channelId="UCsqjHFMB_JYTaEnf_vmTNqg",
        maxResults=5,
        order="date",
        part=[]
    )
    try:
        response = request.execute()
        print(response)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
