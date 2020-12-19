from urllib import request
from urllib import parse
import json

url = "htt?" + parse.urlencode({"page": 1, "per_page": 20})
req = request.Request(url=url,
                      headers={"PRIVATE-TOKEN": "WLuxzfzn1CYxSqzthWs1"},
                      method="GET")
response = request.urlopen(req)
print("url:", response.url)
print("response code:", response.status)
print("DATE:", response.info()["DATE"])
print("response headers", response.info())
print("response data:", json.loads(response.read().decode("utf-8")))
