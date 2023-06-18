# https://contest.yandex.ru/contest/27472/problems/C/

def main():
    list_size = int(input())
    number_list = list(map(int, input().split()))
    search_number = int(input())

    min_diff, min_diff_index = abs(number_list[0] - search_number), 0
    for i in range(1, list_size):
        current_difference = abs(number_list[i] - search_number)
        if current_difference < min_diff:
            min_diff = current_difference
            min_diff_index = i
    return number_list[min_diff_index]


if __name__ == '__main__':
    print(main())
