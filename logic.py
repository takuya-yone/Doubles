
import numpy as np
import json
import requests
import urllib.parse


# - `getCode` 新たなユーザーが選んだ緯度経度をもとに，最寄駅の駅コードを取得する
# - `tmp `選んだ緯度経度から最大100近傍

# In[154]:


def getCode(lat, long):
    key = "eBBWPyXMYduCN759"
    url = "http://api.ekispert.jp/v1/json/geo/station?key="+key+"&geoPoint="+str(lat)+","+str(long)+",tokyo,10000&type=train&stationCount=1"
    result = requests.get(url)
    data = result.json()
    return str(data["ResultSet"]["Point"]["Station"]["code"])

#緯度経度をもとに最寄駅のコードを取得する
def getCode(lat, long):
    key = "eBBWPyXMYduCN759"
    url = "http://api.ekispert.jp/v1/json/geo/station?key="+key+"&geoPoint="+str(lat)+","+str(long)+",tokyo,10000&type=train&stationCount=1"
    result = requests.get(url)
    data = result.json()
    return str(data["ResultSet"]["Point"]["Station"]["code"])

#現在のリクエストマスタを取得する
def get_requestData():
    url = 'https://itto-ki.cybozu.com/k/v1/records.json?app=9'
    headers = {'X-Cybozu-API-Token': 'tjNhIJmlfeLfKrdN86eN3hv0dGRPxkSsdzrg3Wks'}
    res = requests.get(url ,headers=headers)
    return  res.json()["records"]


#対象ユーザの最寄駅コードと許容時間を渡して，共通の駅を取得する
def get_commonStation(bl, um):
    url = "http://api.ekispert.jp/v1/json/search/multipleRange?key=eBBWPyXMYduCN759&baseList="+bl+"&upperMinute="+um+"&limit=1"
    r = requests.get(url)
    return r.json()


#post_data:今回新たに申請してきたユーザー
#waiting_data:リクエストマスタに登録されている，　マッチングを待っているユーザー群
def compare();
    waiting_data = get_requestData()
    for i in range(1, len(waiting_data)):
        if(waiting_data[0]["sex"]["value"] == waiting_data[i]["sex"]["value"]):
            bl = new_code + ":" + waiting_data[i]["station_code"]["value"]
            um = buffer +":"+ waiting_data[i]["range"]["value"]
            station = get_commonStation(bl, um)

            if "Point" in station["ResultSet"]:
                    for j in range(len(waiting_data)):
                        if (waiting_data[0]["sex"]["value"] != waiting_data[j]["sex"]["value"] ):
                                bl2 = bl+":"+waiting_data[j]["station_code"]["value"]
                                um2 = um+":"+ waiting_data[j]["range"]["value"]
                                station=get_commonStation(bl2, um2)

                                if "Point" in station["ResultSet"]:
                                    for k in range(len(waiting_data)):
                                        if (waiting_data[0]["sex"]["value"] != waiting_data[k]["sex"]["value"] and k > j):
                                            bl3 = bl2+":"+waiting_data[k]["station_code"]["value"]
                                            um3 = um2 +":"+ waiting_data[k]["range"]["value"]
                                            station=get_commonStation(bl3, um3)
                                            if "Point" in station["ResultSet"]:
                                                ##jとkの性別が同じ
                                                if(np.random.rand() > 0.5):
                                                    write_validation(waiting_data, i, j)
                                                    write_validation(waiting_data, j, i)
                                                    write_validation(waiting_data, k, 0)
                                                    write_validation(waiting_data,0, k)
                                                else :
                                                    write_validation(waiting_data, 0, j)
                                                    write_validation(waiting_data, j, 0)
                                                    write_validation(waiting_data, k, i)
                                                    write_validation(waiting_data,i, k)
                                                print(station["ResultSet"]["Point"]["Station"]["Name"])
                                                break
                                else:
                                    continue
                                break
            else:
                    print("i:"+str(i)+":"+waiting_data[i]["sex"]["value"])
                    print("miss match")

    return render(request,"success.html")
    # In[216]:


##評価待ちマスタへの書き込み
def write_validation(waiting_data, i, x):
        url = 'https://itto-ki.cybozu.com/k/v1/record.json'
        headers = {'X-Cybozu-API-Token': 'BX3ERqNmj6BbMPtle4V9XOdvrk5A6ICglp7wPdmM','Content-Type' : "application/json"}

        record = {
                    "app": "10",
                    "records": {
                        "name": {
                            "value": waiting_data[i]["userID"]["value"]
                            },
                        "date": {
                            "value": waiting_data[i]["date"]["value"]
                            },
                        "start_time": {
                            "value": waiting_data[i]["start_time"]["value"]
                            },
                        "end_time": {
                            "value": waiting_data[i]["end_time"]["value"]
                            },
                        "station_name": {
                            "value": waiting_data[i]["station_name"]["value"]
                            },
                        "station_code": {
                            "value": waiting_data[i]["station_code"]["value"]
                            },
                        "range": {
                            "value": waiting_data[i]["range"]["value"]
                            },
                        "sex": {
                            "code": waiting_data[i]["sex"]["value"]
                            },
                        "partner":{
                            "value":waiting_data[x]["userID"]["value"]
                           },
                        "line":{
                            "value":waiting_data[i]["userID"]["value"]
                           }
                        }
                    }

        resp = requests.post(url, json=record, headers=headers)
        return resp
