import requests
import json

header = {"Authorization": "OAuth AgAAAABCy87BAADLW6O1qy92EUwAqWrXIsHWemY" }

file_name = "Letter.txt"
with open(file_name, encoding = "utf-8") as f:
    _file = f.read()
    file = requests.get(f"https://cloud-api.yandex.net:443/v1/disk/resources/upload?path=/{file_name}",
                    headers = header)


href = file.json()["href"]

download = requests.put(href, data = _file)

print(download.text)

