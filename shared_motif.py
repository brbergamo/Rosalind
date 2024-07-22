def get_seqs(file):
    lines = []
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if ">" in line:
                lines.append("")
                continue
            lines[-1] += line
        return lines


def find_motif(lista):
    longest_substring = ""
    sorted_seq = sorted(lista, key=len)
    for start in range(len(sorted_seq[0])):
        for end in range(len(sorted_seq[0]), start, -1):
            motif = sorted_seq[0][start:end]
            if all(motif in seqs for seqs in sorted_seq):
                if len(motif) > len(longest_substring):
                    longest_substring = motif

    return longest_substring


if __name__ == "__main__":
    info = get_seqs("/home/beatriz/Downloads/rosalind_lcsm.txt")
    print(find_motif(info))
