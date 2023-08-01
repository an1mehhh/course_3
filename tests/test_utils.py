from course.utils import operations_card
from course.utils.utils import payment_by_card, payment_by_invoice


def test_utils():
    assert payment_by_card("5211275637988469"), str == '5211 27** **** 8469'

    assert payment_by_invoice("49304996510329747621"), str == '**7621'


def test_operations_card():
    assert operations_card.transfer_date([{"date": "2019-08-26T10:50:58.294041"}]) == ["26.08.2019"]
    assert operations_card.transfer_date([{"date": 121}]) == [""]

    assert operations_card.translation_description([{"description": "Перевод с карты на счет"}]) == [
        "Перевод с карты на счет"]
    assert operations_card.translation_description([{"description": "Открытие вклада"}]) == ["Открытие вклада"]
    assert operations_card.translation_description([{"description": "Перевод организации"}]) == ["Перевод организации"]

    assert operations_card.transfer_from([{"from": "Maestro 1308795367077170"}]) == ["Maestro 1308 79** **** 7170"]
    assert operations_card.transfer_from([{"from": "Счет 17691325653939384901"}]) == ["Счет **4901"]

    assert operations_card.transfer_to([{"to": "Maestro 1308795367077170"}]) == ["Maestro 1308 79** **** 7170"]
    assert operations_card.transfer_to([{"to": "Счет 17691325653939384901"}]) == ["Счет **4901"]

    assert operations_card.transfer_amount([{"operationAmount": {"amount": "56516.63"}}]) == ["56516.63"]
    assert operations_card.transfer_amount([{"operationAmount": {"amount": "0"}}]) == ["0"]

    assert operations_card.currency([{"operationAmount": {"currency": {"name": "USD"}}}]) == ["USD"]
