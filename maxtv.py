import json
import requests

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Authorization': 'Bearer ..---ENTER YOUR TOKEN HERE----',
    'app-version-code': '94',
    'app-version-name': '2.0.1',
    'x-timestamp': 'America/New_York',
    'x-securetv-uuid': 'YO:UR:MA:C0:HE:RE',
    'x-ethernet-address': 'YO:UR:MA:C0:HE:RE',
    'x-securetv-sdk-scope': 'IPTV',
    'platform-sdk-client': '',
    'User-Agent': 'MaxTV/2.0.1 (com.securetv.maxtv.androidbox; build:94; Android 13; Model:Pixel 2 XL; Brand:google; Device:taimen) okhttp',
    'Host': '192.168.187.169:8094',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip'
}

response = requests.get('http://192.168.187.169:8094/api/v3/sync/channels', headers=headers)

if response.status_code == 200:
    with open('channels.json', 'w') as f:
        json.dump(response.json(), f)
        print('channels.json saved successfully!')
else:
    print('Error: API request failed')
