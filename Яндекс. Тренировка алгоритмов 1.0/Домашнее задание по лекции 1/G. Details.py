# https://contest.yandex.ru/contest/27393/problems/G/


def main():
    metal_kg, template_kg, detail_kg = map(int, input().split())
    detail_count = 0
    while metal_kg >= template_kg >= detail_kg:
        template_count = metal_kg // template_kg
        metal_kg = metal_kg % template_kg

        detail_count += (template_kg // detail_kg) * template_count
        metal_kg += (template_kg % detail_kg) * template_count
    return detail_count


if __name__ == '__main__':
    print(main())
