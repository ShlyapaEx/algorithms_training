# https://contest.yandex.ru/contest/27393/problems/temp_room/

def main():
    temp_room, temp_cond = map(int, input().split())
    cond_mode = input()

    match cond_mode:
        case 'fan':
            print(temp_room)
        case 'auto':
            print(temp_cond)
        case 'freeze':
            print(temp_room if temp_room < temp_cond else temp_cond)
        case 'heat':
            print(temp_cond if temp_room < temp_cond else temp_room)


if __name__ == '__main__':
    main()
