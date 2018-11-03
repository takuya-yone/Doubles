from django.shortcuts import render
import requests
import json

# Create your views here.
def waiting(request):
    return render(request, 'waiting.html')

def matching_for_other(request):
    print(request.POST)
    headers = {
                'X-Cybozu-API-Token': 'RY6pqwdXsLotz6ZCQ7PR1r2BLuepTOA23BqDUkP4',
            }
    queres = 'app=8&fields=name&fields=sex&fields=latitude&fields=longitude'
    json_string = requests.get('https://itto-ki.cybozu.com/k/v1/records.json?{}'.format(queres), headers=headers)
    people = json.loads(json_string.text)
    nearest_person = people['records'].pop()
    for person in people['records']:
        pass

    return render(request, 'waiting.html')
