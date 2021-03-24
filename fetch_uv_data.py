import os
import requests
from pprint import pprint


uv_url_template ='https://api.openuv.io/api/v1/uv?lat={lat}&lng={lng}&dt={data}'
my_latitude = '51.52369' 
my_longitude = '-0.0395857' 
my_date = '2018-11'
headers = {'x-access-token': os.environ.get('OPENUV_TOKEN')}
uv_url = uv_url_template.format(lat=my_latitude, lng = my_longitude, data=my_date)
resp = requests.get(uv_url, headers=headers)
if resp.ok:
    uv = resp.json()
else:
    print(resp.reason)
pprint(uv)