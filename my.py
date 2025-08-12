# hh_test.py
import requests
import json
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def save_hh_data():
    response = requests.get("https://api.hh.ru/vacancies?text=python&per_page=5", verify=False)
    data = response.json()

    with open('hh_json.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False )
    
    print('Данные получены')


if __name__ == "__main__":
   save_hh_data()