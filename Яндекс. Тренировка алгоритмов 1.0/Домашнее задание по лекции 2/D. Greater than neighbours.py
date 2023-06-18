# https://contest.yandex.ru/contest/27472/problems/D/

def main():
    result = 0
    number_list = list(map(int, input().split()))
    for i in range(1, len(number_list) - 1):
        if number_list[i - 1] < number_list[i] > number_list[i + 1]:
            result += 1
    return result


if __name__ == '__main__':
    print(main())
