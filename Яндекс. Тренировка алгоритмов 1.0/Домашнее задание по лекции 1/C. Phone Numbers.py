# https://contest.yandex.ru/contest/27393/problems/C/

def process_number(number):
    number = number.replace('+', '').replace('(', '') \
        .replace(')', '').replace('-', '')
    if len(number) == 7:
        number = '8495' + number
    number = number.replace(number[0], '8', 1)
    return number


def main():
    new_number = int(process_number(input()))
    for _ in range(3):
        if new_number == int(process_number(input())):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
