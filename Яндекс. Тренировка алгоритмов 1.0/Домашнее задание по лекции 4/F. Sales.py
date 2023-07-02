# https://contest.yandex.ru/contest/27665/problems/F/

def group_sales_by_customer(sales_data: list[str]) -> dict[str: dict[str: int]]:
    grouped_sales = {}

    for sale_order in sales_data:
        customer, product, quantity = sale_order.split()
        if grouped_sales.get(customer, None) is None:
            grouped_sales[customer] = {}
        if grouped_sales[customer].get(product, None) is None:
            grouped_sales[customer][product] = 0
        grouped_sales[customer][product] += int(quantity)

    return grouped_sales


def main():
    with open('input.txt', 'r', encoding='utf-8') as file:
        file_lines = file.readlines()
    result = group_sales_by_customer(file_lines)

    for customer in sorted(result):
        print(customer + ':')
        for product in sorted(result[customer]):
            print(product, result[customer][product])


if __name__ == '__main__':
    main()
