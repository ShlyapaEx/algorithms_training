# https://contest.yandex.ru/contest/27663/problems/F/


def get_genome_pairs(genome: str) -> list[str]:
    genome_pairs = []
    for i in range(len(genome) - 1):
        genome_pairs.append(''.join(genome[i] + genome[i + 1]))
    return genome_pairs


def get_genome_proximity_degree(first_genome: set, second_genome: str):
    first_pairs = get_genome_pairs(first_genome)
    second_pairs = set(get_genome_pairs(second_genome))

    pairs_count = 0
    for genome_pair in first_pairs:
        if genome_pair in second_pairs:
            pairs_count += 1
    return pairs_count


def main():
    first_genome, second_genome = input(), input()
    result = get_genome_proximity_degree(first_genome, second_genome)
    print(result)


if __name__ == '__main__':
    main()
