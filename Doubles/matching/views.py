from django.shortcuts import render
import json
import urllib.request
import requests
import os.path


def getStation(lat, long):
   key = "eBBWPyXMYduCN759"
   url = "http://api.ekispert.jp/v1/json/geo/station?key="+key+"&geoPoint="+str(lat)+","+str(long)+",tokyo,10000&type=train&stationCount=1"
   result = requests.get(url)
   data = result.json()
   return data["ResultSet"]["Point"]["Station"]

def login(request):
    return render(request,'login.html')

def login_auth(request):


    line_id = request.POST['line_id']
    password = request.POST['password']

    s = 'password=\"' + password + '\"and line=\"'+ line_id + '\"'

    s_quote = urllib.parse.quote(s)

    url = 'https://itto-ki.cybozu.com/k/v1/records.json?app=8&query='+s_quote
    # +'&password='+password
# headers = {
#     'Content-Type': 'application/json',
#     'X-Cybozu-API-Token': 'RY6pqwdXsLotz6ZCQ7PR1r2BLuepTOA23BqDUkP4'
# }
    headers = {
        'X-Cybozu-API-Token': 'RY6pqwdXsLotz6ZCQ7PR1r2BLuepTOA23BqDUkP4'}

    res = requests.get(url ,headers=headers)

    data = res.json()

    if len(data["records"])!=1:
        return render(request,'login.html')
    else:
        request.session['userid'] = data["records"][0]["$id"]["value"]
        request.session['sex'] = data["records"][0]["sex"]["value"]
        request.session['name'] = data["records"][0]["name"]["value"]
        dct = {"session_name":request.session['name']}
        return render(request,'home.html',dct)



def register(request):
    return render(request,'register.html')

def register_auth(request):
    name = request.POST['name']
    category = request.POST['category']
    sex = request.POST['sex']
    password = request.POST['password']
    age = request.POST['age']
    line_id = request.POST['line_id']

    post_data = {
            "app": "8",
            "record": {
                "name": {
                    "value": name
                    },
                "password": {
                    "value": password
                    },
                "age": {
                    "value": age
                    },
                "line": {
                    "value": line_id
                    },
                "sex": {
                    "value": sex
                    },
                "category": {
                    "value": category
                    }
                }
            }
    url = "https://itto-ki.cybozu.com/k/v1/record.json"

    headers = {
            # 'Host': 'example.cybozu.com:443',
            'X-Cybozu-API-Token': 'RY6pqwdXsLotz6ZCQ7PR1r2BLuepTOA23BqDUkP4',
            'Content-Type': 'application/json'
            }
    res = requests.post(url, data=json.dumps(post_data), headers=headers)
    print(res.text)




    return render(request,'login.html')

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
            "app": "9",
            "record": {
                "name": {
                    "value": 2
                    },
                "date": {
                    "value": str(data['input_date'])
                    },
                "start_time": {
                    "value": str(data['input_start_time'])
                    },
                "end_time": {
                    "value": str(data['input_end_time'])
                    },
                "station_name": {
                    "value": str(data["station_name"])
                    },
                "station_code": {
                    "value": str(data["station_code"])
                    },
                "range": {
                    "value": str(data["available_time"])
                    },
                "flag": {
                    "value": "off"
                    },
                "sex": {
                    "value": "男"
                    }
                }
            }

    url = "https://itto-ki.cybozu.com/k/v1/record.json"

    headers = {
            # 'Host': 'example.cybozu.com:443',
            'X-Cybozu-API-Token': '2HAqiXnC777v4trbOmvG2ojn9LlNJngTw6TS9wTL',
            'Content-Type': 'application/json'
            }
    res = requests.post(url, data=json.dumps(post_data), headers=headers)
    print(res.text)
    # print(data)
    return render(request,'search.html')
