import json


def read_file(path):
    """чтение json файла"""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def payment_by_invoice(card_number):
    """функция скрывает номер счёта"""
    return (len(card_number[:2]) * '*') + card_number[-4:]


def payment_by_card(card_number):
    """функция скрывает номер карты"""
    private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
    return " ".join([private_number[i:i + len(private_number) // 4] for i in
                     range(0, len(private_number), len(private_number) // 4)])
