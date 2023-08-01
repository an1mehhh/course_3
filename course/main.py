import datetime

from utils.utils import read_file
from utils.operations_card import transfer_date, translation_description, transfer_from, transfer_to, transfer_amount, \
    currency


def main():
    """основной код"""
    # путь json
    path = "./data/operations.json"

    # массив с 5 последними выполненными операциями
    data = [item for item in read_file(path) if item.get("state") == "EXECUTED"][-5:]
    data_for_dict = []
    for i in range(5):
        card = {
            "date": transfer_date(data)[i],
            "description": translation_description(data)[i],
            "from": transfer_from(data)[i],
            "to": transfer_to(data)[i],
            "amount": transfer_amount(data)[i],
            "currency": currency(data)[i]
        }
        data_for_dict.append(card)
    # сортировка массива по дате
    data_for_dict = sorted(data_for_dict, key=lambda x: datetime.datetime.strptime(x['date'], '%d.%m.%Y'), reverse=True)

    # вывод в консоль
    for item in data_for_dict:
        print(f"{item['date']} {item['description']}")
        if item['from'] == " ":
            print(f"{item['to']}")
        else:
            print(f"{item['from']} -> {item['to']}")
        print(f"{item['amount']} {item['currency']}")
        print()


if __name__ == "__main__":
    main()
