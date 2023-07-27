import json
import datetime


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def transfer_date(data):
    date = []
    for x in data:
        if x == {}:
            continue
        elif x["state"] == "EXECUTED":
            date_line = datetime.datetime.fromisoformat(x["date"])
            converted_date = datetime.datetime.strftime(date_line, "%d.%m.%Y")
            date.append(converted_date)
    return date[-5:]

