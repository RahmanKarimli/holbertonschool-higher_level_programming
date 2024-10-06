import json
import csv
data = []


def convert_csv_to_json(filename):
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        with open("data.json", "w") as jf:
            json.dump(data, jf, indent=4)
        return True
    except FileNotFoundError:
        return False
