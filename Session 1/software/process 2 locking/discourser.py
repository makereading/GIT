import requests
import json
import os

# Category 5 is for events

def to_tlc(message, title):
    params={
        "Api-Key":os.environ["DISCOURSE_API_KEY"],
        "Api-Username":"parameshwar",
        "title": title,
        "raw": message,
        "topic_id": 0,
        "category": 5,
        }

    data = requests.post("https://forums.tamillinuxcommunity.org/posts.json",params=params)
    if data.status_code==200:
        print("Post created successfully!")
    else:
        print("Something happened")
