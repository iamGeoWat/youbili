# -*- coding: utf-8 -*-

import os
from google.oauth2 import service_account
import googleapiclient.discovery
import googleapiclient.errors
import time
import requests


def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    credentials = service_account.Credentials.from_service_account_file(
        'bot_key.json')
    print(credentials)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    video_ids = []
    page_token = ""
    for i in range(3):
        request = youtube.search().list(
            channelId="UCsqjHFMB_JYTaEnf_vmTNqg",
            maxResults=5,
            order="date",
            part=[],
            pageToken=page_token
        )
        try:
            response = request.execute()
            for item in response['items']:
                video_ids.append(item['id']['videoId'])
            page_token = response['nextPageToken']
            print(i, response)
        except Exception as e:
            print(e)
        time.sleep(0.5)
    print(len(video_ids), video_ids)
    b_url = "https://api.bilibili.com/x/web-interface/search/all/v2?context=&page=1&order=&duration=&tids_1=&tids_2" \
            "=&__refresh__=true&__reload__=false&_extra=&highlight=1&single_column=0&keyword= "
    for video_id in video_ids:
        for result in requests.get(b_url + video_id).json()['data']['result']:
            if result['result_type'] == "video":
                if len(result['data']):
                    print(video_id, result['data'][0]['arcurl'])
                else:
                    print(video_id, 'None.')
        time.sleep(0.5)


if __name__ == "__main__":
    main()
