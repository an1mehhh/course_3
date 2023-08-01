import datetime

from course.utils.utils import payment_by_invoice, payment_by_card


def transfer_date(data):
    """обработка 'date' из json"""
    date = []
    for item in data:
        if isinstance(item.get("date"), str) or item.get("date") == {}:
            # перевод даты в формат дд.мм.гг.
            date_line = datetime.datetime.fromisoformat(item.get("date"))
            converted_date = datetime.datetime.strftime(date_line, "%d.%m.%Y")
            date.append(converted_date)

        else:
            date.append("")

    return date


def translation_description(data):
    """обработка 'description' из json"""
    date = []
    for item in data:
        if item is None or item.get("description") == {}:
            date.append("")
        date.append(item.get("description"))
    return date


def transfer_from(data):
    """обработка 'from' из json"""
    date = []
    for item in data:

        card_info = item.get("from")
        if card_info is None or item.get("from") == {}:
            card_name, card_number = "", ""
            date.append(f"{card_name} {card_number}")
        else:
            # вытягиваем имя карты и его номер
            card_name, card_number = card_info.split()[0], card_info.split()[1]

            # если это карта, зашифровка карты ведётся в функции payment_by_card()
            # если это счёт, зашифровка счёта ведётся в функции payment_by_invoice()
            if len(card_number) == 16:
                hide_number_card = payment_by_card(card_number)
            elif card_name == "Счет":
                hide_number_card = payment_by_invoice(card_number)

            date.append(f"{card_name} {hide_number_card}")

    return date


def transfer_to(data):
    """обработка 'to' из json"""
    date = []
    for item in data:

        card_info = item.get("to")
        if item is None or item.get("to") == {}:
            card_name, card_number = "", ""
            date.append(f"{card_name} {card_number}")
        else:
            # вытягиваем имя карты и его номер
            card_name, card_number = card_info.split()[0], card_info.split()[1]

            # если это карта, зашифровка карты ведётся в функции payment_by_card()
            # если это счёт, зашифровка счёта ведётся в функции payment_by_invoice()
            if len(card_number) == 16:
                hide_number_card = payment_by_card(card_number)
            elif card_name == "Счет":
                hide_number_card = payment_by_invoice(card_number)

            date.append(f"{card_name} {hide_number_card}")

    return date


def transfer_amount(data):
    """обработка 'amount' из json"""
    date = []
    for item in data:
        if item is None or item["operationAmount"]["amount"] == {}:
            date.append("")
        date.append(item["operationAmount"]["amount"])

    return date


def currency(data):
    """обработка 'currency' из json"""
    date = []
    for item in data:
        if item is None or item["operationAmount"]["currency"]["name"] == {}:
            date.append("")
        date.append(item["operationAmount"]["currency"]["name"])

    return date
