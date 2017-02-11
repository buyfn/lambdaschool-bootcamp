import requests

url = "http://api.openweathermap.org/data/2.5/forecast?lat=52.75&lon=25.11&appid=932101dce842f87527bad4bc2fe1b2b6&units=metric"
data = requests.get(url).json().get("list")
temps = [x['main']['temp'] for x in data]
avg = sum(temps) / len(temps)

print(avg)
