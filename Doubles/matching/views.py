from django.shortcuts import render
import json
import urllib.request
import requests


def getStation(lat, long):
   key = "eBBWPyXMYduCN759"
   url = "http://api.ekispert.jp/v1/json/geo/station?key="+key+"&geoPoint="+str(lat)+","+str(long)+",tokyo,10000&type=train&stationCount=1"
   result = requests.get(url)
   data = result.json()
   return data["ResultSet"]["Point"]["Station"]

def map(request):


    url = 'https://itto-ki.cybozu.com/k/v1/records.json?app=7&fields=name&fields=latitude&fields=longitude'

    # headers = {
    #     'Content-Type': 'application/json',
    #     'X-Cybozu-API-Token': 'RY6pqwdXsLotz6ZCQ7PR1r2BLuepTOA23BqDUkP4'
    # }
    headers = {

            # 'Content-Type': 'application/json',
            'X-Cybozu-API-Token': 'njpCik1eeDfvJsPO2N47QL968nN9K9G1aSn2IJts'}
    res = requests.get(url ,headers=headers)

    data = res.json()
    # print((data['records']))
    dct = {'data':json.dumps(data)}
    # req = urllib.request.get(url, json.dumps(data).encode(), headers)
    # with urllib.request.urlopen(req) as res:
    #     body = res.read()
    #     print(body)
    return render(request, 'map.html',dct)

def search(request):
    station_info =getStation(request.POST['input_lat'],request.POST['input_lng'])
    # print(station_info)
    # print(station_info[2])
    data = {
        'input_date': request.POST['input_date'],
        'input_start_time': request.POST['input_start_time'],
        'input_end_time': request.POST['input_end_time'],
        'input_lat': request.POST['input_lat'],
        'input_lng': request.POST['input_lng'],
        'station_name':station_info['code'],
        'station_code':station_info["Name"],
        'available_time':request.POST['available_time']
    }

    post_data = {
        "app": 9,
        "record": {
            "userID": {
                "value": "テスト"
                },
                "date": {
                "value": data['input_date']
                },
                "start_time": {
                "value": data['input_start_time']
                },
                "end_time": {
                "value": data['input_end_time']
                },
                "station_name": {
                "value": data["station_name"]
                },
                "station_code": {
                "value": data["station_code"]
                },
                "range": {
                "value": data["available_time"]
                },
                "flag": {
                "value": ["on"]
                }
                }
            }

    url = "https://itto-ki.cybozu.com/k/1/record.json"


    # post_data = {'app':"9",'record':record}

    headers = {
            'Host: example.cybozu.com:443'
            'X-Cybozu-API-Token':'wHESFXvG6wQP4QEEaPn2rWkDpTIWv57jjJNLPpZ1',
            'Authorization': 'Basic wHESFXvG6wQP4QEEaPn2rWkDpTIWv57jjJNLPpZ1',
            'Content-Type': 'application/json'
            }
    res = requests.post(url ,json=post_data,headers=headers)
    print(res.text)
    # print(data)
    return render(request,'search.html')
