# https://contest.yandex.ru/contest/27472/problems/A/

def main():
    input_list = input().split()
    for i in range(len(input_list) - 1):
        if input_list[i + 1] <= input_list[i]:
            return "NO"
    return "YES"


if __name__ == '__main__':
    print(main())
