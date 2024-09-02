import requests

api_key = '85cc0a8a8a7e6695de777691cf451349'

city = str(input("Enter your city name :"))

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    #min_temp = data['main']['temp_min']
    #max_temp = data['main']['temp_max']
    hum = data['main']['humidity']
    fl_temp = data['main']['feels_like']
    #print(f'City: {cit}')
    temp = int(temp-273.15)
    fl_temp = int(fl_temp-273.15)
    print(f'Temperature: {temp}°C')
    print(f'Feels Like: {fl_temp}°C')
    #print(f'Max: {max_temp} K')
    #print(f'Min: {min_temp} K')
    print(f'Description: {desc}')
    print(f'Humidity: {hum}%')
    print(data)
else:
    print("Error")
