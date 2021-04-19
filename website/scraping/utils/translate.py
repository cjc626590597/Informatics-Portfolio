import requests
import json

def translate(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }

    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        'Cookie':'OUTFOX_SEARCH_USER_ID_NCOO=1295375217.4520593; OUTFOX_SEARCH_USER_ID="981797551@10.169.0.82"; _ga=GA1.2.1565944672.1597996449; P_INFO=626590597@163.com|1598426063|0|youdao_jianwai|11&6|gud&1597996529&youdao_jianwai#US&null#10#0#0|&0|urs&youdao_jianwai|626590597@163.com; JSESSIONID=aaaXMklgs23eq7ThvQsIx; ___rl__test__cookies=1617437172532; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcuFzZjYfg2bcq7xXwIx'
    }
    response = requests.post(url, data=key, headers=head)
    if response.status_code == 200:
        return response.text
    else:
        print("calling error")
        return None


def getTranslate(word):
    list_trans = translate(word)
    result = json.loads(list_trans)
    result = result['translateResult'][0][0]['tgt']
    return result

a = "你好呀,你为什么在这里，我想认识你"
a = getTranslate(a)
print(a)
