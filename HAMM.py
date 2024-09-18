def reading_file(file):
    with open(file, "r") as f:
        lines = f.read()
        lines = lines.splitlines()
    return lines[0], lines[1]


def count_point_mutations(sequence1, sequence2):
    return sum([1 for i in range(len(sequence1)) if sequence1[i] != sequence2[i]])


sequence1, sequence2 = reading_file("/home/beatriz/Downloads/rosalind_hamm.txt")
print(count_point_mutations(sequence1, sequence2))
