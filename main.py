import requests

key = "6c1633a7-f863-4ac6-8c97-effd24d41d70"  # TODO подставьте значение вашего ключа доступа к API
lat = "59.93"  # широта в градусах
lon = "30.31"  # долгота в градусах

url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"
headers = {"X-Yandex-API-Key": f"{key}"}

response = requests.get(url, headers=headers)
print(response.json())
