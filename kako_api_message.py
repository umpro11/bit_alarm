import requests
import json

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
    "Authorization": "Bearer " + '{1eMzRfhuf3n1OpElEHmRDWiG1ecHH9Pw-xoX-Ao9cusAAAF7TaKLRA}'
}

data ={
    "template_object" : json.dumps({
        "object_type" : "text",
        "text" : "하나의 첫 카카오톡 메시지입니다.",
        "link" : {
            "web_url" : "www.naver.com"
        }
    })
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
