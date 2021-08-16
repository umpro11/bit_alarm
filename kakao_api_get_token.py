import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '0970e1132129f5a3bcdcbe8af3bb3188'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'FOieMOlVw41PRzuh3z6DY9AyJ3z1GKlhG3ax3wXyRO_v_YcQcA01EgtWEVRbF_GmhHm4WgopcFAAAAF7TcjEgg'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)
