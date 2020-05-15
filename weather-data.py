import requests
from datetime import datetime
res = requests.get(
    url='https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22')

weather_data = res.json()

def test_case_1(weather_data):
    print("\n\n--------- \n Test Case 1: \n ---------")
    """
    Prob definition: Check if the response contains 4 days of data
    """
    days_info = []
    for i in range(0, len(weather_data['list'])):
        days_info.append((weather_data['list'][i]['dt_txt']).split(' ')[0])
    no_of_days = {n for n in days_info}
    if len(no_of_days) == 4:
        print("Pass \n The Weather Data contains 4 days of data!")
    elif(len(no_of_days) > 4):
        print("Failed \n No the response doesnt contain 4 days of Data, instead it has 4+ days of data!")
    else:
        print("Failed \n The Weather Data contains less than 4 days of data!")


def test_case_2(weather_data):
    print("\n\n--------- \n Test Case 2: \n ---------")
    days_info = []
    validity = False
    for i in range(0, len(weather_data['list'])):
        if i == len(weather_data['list'])-1:
            validity = True
            break
        x = weather_data['list'][i+1]['dt_txt']
        y = weather_data['list'][i]['dt_txt']
        time1 = datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
        time2 = datetime.strptime(y, "%Y-%m-%d %H:%M:%S")
        diff = time1 - time2
        hour_diff = diff.total_seconds()/3600
        if hour_diff == 1.0:
            continue
    if validity:
        print("Pass \n All the forecasts are exactly in hourly interval!")
    else:
        print("Failed \n The forecasts are NOT in hourly interval!")


def test_case_3(weather_data):
    print("\n\n--------- \n Test Case 3: \n ---------")
    temp = []
    temp_exceeded = []
    for i in range(0, len(weather_data['list'])):
        temp = weather_data['list'][i]['main']['temp']
        temp_min = weather_data['list'][i]['main']['temp_min']
        temp_max = weather_data['list'][i]['main']['temp_max']
        if temp < temp_min or temp > temp_max:
            temp_exceeded.append(weather_data['list'][i]['dt_txt'])
    if len(temp_exceeded) == 0:
        print("Pass \n Temperature is within the specified range - temp_min, temp_max !")
    else:
        print("Failed \n Temperature is NOT within the specified range for below Days:!")
        print(temp_exceeded)


def test_case_4(weather_data):
    print("\n\n--------- \n Test Case 4: \n ---------")
    validity = False
    for i in range(0, len(weather_data['list'])):
        if weather_data['list'][i]['weather'][0]['id'] == 500 and weather_data['list'][i]['weather'][0]['description'] == 'light rain':
            validity = True
    if validity:
        print("Pass \n All weather IDs: 500 has description - light rain!")
    else:
        print(" Failed \n All weather IDs: 500 does not have description - light rain!")

        
def test_case_5(weather_data):
    print("\n\n--------- \n Test Case 5: \n ---------")
    validity = False
    for i in range(0, len(weather_data['list'])):
        if weather_data['list'][i]['weather'][0]['id'] == 800 and weather_data['list'][i]['weather'][0]['description'] == 'clear sky':
            validity = True
    if validity:
        print("Pass \n All weather IDs: 800 has description - clear sky!")
    else:
        print("Failed \n All weather ID: 800 does nit have description - clear sky!")

test_case_1(weather_data)
test_case_2(weather_data)
test_case_3(weather_data)
test_case_4(weather_data)
test_case_5(weather_data)




