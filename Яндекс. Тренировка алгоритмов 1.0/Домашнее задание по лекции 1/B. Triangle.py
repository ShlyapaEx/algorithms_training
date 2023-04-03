# https://contest.yandex.ru/contest/27393/problems/B/

def main():
    a, b, c = [int(input()) for _ in range(3)]
    if a + b > c and b + c > a and a + c > b:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
