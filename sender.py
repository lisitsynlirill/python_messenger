
import requests
#r=requests.get("https://google.com")
#print(r)
#print(r.headers)
#print(r.text)
print("Enter Name: ")
name=input()

while(True):
    print("Enter message: ")
    text=input()

    r=requests.post(
        "http://127.0.0.1:5000/send",
        json={"text": text, "name": name}
    )
#print(r)
#print(r.headers)
#print(r.text)