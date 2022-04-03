from random import random
from time import sleep
import requests as req

while 1:
    x = random() * 20 + 20
    params = dict(sensor="1", temp=x)
    r = req.get("http://127.0.0.1:5000/temp", params=params)
    print(r.text)
    sleep(1)
