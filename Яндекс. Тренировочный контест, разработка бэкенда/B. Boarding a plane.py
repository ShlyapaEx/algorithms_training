# https://contest.yandex.ru/contest/28412/problems/B/
class Passengers:
    def __init__(self, schema: str) -> None:
        data = schema.split()
        self.group_size = int(data[0])
        self.side = data[1]
        self.preference = data[2]
        self.found_place = False

    def __repr__(self) -> str:
        return ' '.join((self.group_size, self.side, self.preference))


class Row:
    def __init__(self, schema: str) -> None:
        self.left = schema[:3]
        self.right = schema[4:]

    def __repr__(self) -> str:
        return self.left + '_' + self.right

    def can_fit_group(self, group: Passengers):
        side_status: str = getattr(self, group.side)
        # TODO: Проверка на сторону лево/право
        if group.preference == 'aisle':
            if side_status[-group.group_size:] == '.' * group.group_size:
                return True
        elif group.preference == 'window':
            if side_status[:group.group_size] == '.' * group.group_size:
                return True
        return False


def main():
    number_of_rows = int(input())
    rows: list[Row] = []
    for _ in range(number_of_rows):
        rows.append(Row(input()))

    number_of_passengers = int(input())
    passengers: list[Passengers] = []
    for _ in range(number_of_passengers):
        passengers.append(Passengers(input()))

    for passenger_group in passengers:
        for row in rows:
            if row.can_fit_group(passenger_group):
                print("WOW")
                break
            print("BAD")


if __name__ == '__main__':
    main()
