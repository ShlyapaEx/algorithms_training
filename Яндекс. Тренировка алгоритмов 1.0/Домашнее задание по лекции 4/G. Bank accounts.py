# https://contest.yandex.ru/contest/27665/problems/G/


def create_client_if_not_existing(client_surname: str, clients_data: dict):
    if client_surname not in clients_data:
        clients_data[client_surname] = 0


def add_money_to_client(client_surname: str, money_amount: int,
                        clients_data: dict):
    create_client_if_not_existing(client_surname, clients_data)
    clients_data[client_surname] += money_amount


def withdraw_money_from_client(client_surname: str, money_amount: int,
                               clients_data: dict):
    create_client_if_not_existing(client_surname, clients_data)
    clients_data[client_surname] -= money_amount


def get_client_balance(client_surname: str, clients_data: dict):
    if client_surname not in clients_data:
        return 'ERROR'
    return clients_data[client_surname]


def transfer_money(sender_surname: str, recevier_surname: str,
                   money_amount: int, clients_data: dict):
    create_client_if_not_existing(sender_surname, clients_data)
    create_client_if_not_existing(recevier_surname, clients_data)

    clients_data[sender_surname] -= money_amount
    clients_data[recevier_surname] += money_amount


def give_income(added_percent, clients_data: dict):
    for client, balance in clients_data.items():
        if balance > 0:
            clients_data[client] = int(
                balance + (balance * (added_percent / 100)))


def process_bank_operations(operations: list[str]):
    clients_data = {}

    for operation_string in operations:
        operation_data = operation_string.split()
        operation_name = operation_data[0]
        match operation_name:
            case 'DEPOSIT':
                add_money_to_client(client_surname=operation_data[1],
                                    money_amount=int(operation_data[2]),
                                    clients_data=clients_data)
            case 'WITHDRAW':
                withdraw_money_from_client(client_surname=operation_data[1],
                                           money_amount=int(operation_data[2]),
                                           clients_data=clients_data)
            case 'BALANCE':
                print(get_client_balance(client_surname=operation_data[1],
                                         clients_data=clients_data))
            case 'TRANSFER':
                transfer_money(sender_surname=operation_data[1],
                               recevier_surname=operation_data[2],
                               money_amount=int(operation_data[3]),
                               clients_data=clients_data)
            case 'INCOME':
                give_income(added_percent=int(operation_data[1]),
                            clients_data=clients_data)


def main():
    with open('input.txt', 'r', encoding='utf-8') as file:
        file_lines = file.readlines()
    process_bank_operations(file_lines)


if __name__ == '__main__':
    main()
