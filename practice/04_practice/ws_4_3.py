import requests
from pprint import pprint as print

dummy_data = []

for i in range(1,11):
    new_dict = {}

    # 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    # API 요청
    response = requests.get(API_URL)
    # JSON -> dict 데이터 변환
    parsed_data = response.json()

    # 특정 데이터 출력
    name_data = parsed_data['name']

    lat_data = parsed_data['address']['geo']['lat']

    lng_data = parsed_data['address']['geo']['lng']
    
    company_name_data = parsed_data['company']['name']

    new_dict['name'] = name_data
    new_dict['lat'] = lat_data
    new_dict['lng'] = lng_data
    new_dict['company'] = company_name_data

    if float(lat_data) > -80 and float(lat_data) < 80 :
        if float(lng_data) > -80 and float(lng_data) < 80 :
            dummy_data.append(new_dict)

print(dummy_data)
