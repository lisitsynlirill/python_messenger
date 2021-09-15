from datetime import datetime, timedelta

import time

from flask import Flask, request, abort

app = Flask(__name__)

db = [
  {
    "msg": "Hi",
    "name": "Nata",
    "date": time.time()-100,
  },
  {
    "msg": "Hi-Hi",
    "name": "Kirill",
    "date": time.time()-50,
  },
  {
    "msg": "Hi-Hi-hi",
    "name": "Nata",
    "date": time.time()-10,
  },
  ]

@app.route("/")
def hello():
    return "<p>Hello World!</p>"

@app.route("/status")
def status():
    return {
        "status": True,
        "name": "MyMessenger",
        "time": datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
        #"t2": time.time(),
        #"t3": datetime.utcnow().strftime("%H:%M"),
    }


@app.route("/send", methods=["POST"])
def send_message():
    data = request.json

    if not isinstance(data, dict):
      abort(400)
    if "text" not in data or "name" not in data:
      abort(400)

    text = data["text"]
    name = data["name"]    

    if len(text) > 100 or len(name) > 100:
      abort(400)
    if len(text) == 0 or len(name) == 0:
      abort(400)

    mes = {
      "msg": text,
      "name": name,
      "date": time.time()
    }
    db.append(mes)
    return {"status": "OK"}

@app.route("/receive", methods=["GET"])
def get_messages():
  if "after" not in request.args:
    abort(400)
  after = request.args["after"]
  try:
    after=float(after)
  except ValueError:
    abort(400)
  N=10
  result = []
  for item in db:
    if item["date"] > after:
      result.append(item)
  return {"messages": result[:N]}


@app.route("/show", methods=["GET"])
def print_db():
  return {"database": db}

if __name__ == "__main__":
    app.run(debug=True)
