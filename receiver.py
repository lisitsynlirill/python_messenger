import requests
import time

from requests.models import Response

after_val=0
while(True):
    r=requests.get(
        "http://127.0.0.1:5000/receive",
        params={"after": after_val}
    )
    response = r.json()
    if len(response["messages"]) > 0:
        after_val = response["messages"][-1]["date"],
        print(r.text)
    time.sleep(5)
    print("--------------")
