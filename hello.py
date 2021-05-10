import requests
import json
token = ''
r = requests.post('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx969333a36ca53da2&secret=568526454b3129db9228349cd4845956')
token = r.json()['access_token']
print(token)

datas = json.dumps({
    'env':'demo-whglk',
    'query':'db.collection("List_data").get()'
})
m = requests.post('https://api.weixin.qq.com/tcb/databasequery?access_token='+token,data=datas)
result = m.json()
print(result)