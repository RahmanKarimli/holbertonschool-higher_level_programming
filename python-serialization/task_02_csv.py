import json, csv


data = {}
def convert_csv_to_json(filename):
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data[row['name']] = row
            with open("data.json", "w") as jf:
                jf.write(json.dumps(data))
        return True
    except FileNotFoundError:
        return False
