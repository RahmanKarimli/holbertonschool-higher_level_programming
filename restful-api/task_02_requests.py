import json
import csv
import requests

resopnse = requests.get("https://jsonplaceholder.typicode.com/posts")

def fetch_and_print_posts():
    print(f"Status Code: {resopnse.status_code}")
    data = resopnse.json()
    for i in data:
        print(i['title'])


def fetch_and_save_posts():
    with open("test.csv", "w", newline='') as f:
        data = json.loads(resopnse.text)
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for i in data:
            f.write(f"{i['id']}, {i['title']}, {i['body']}\n")
