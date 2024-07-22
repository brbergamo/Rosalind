def get_seqs(file):
    info = {}
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            if ">" in line:
                seq = line[1:]
                info[seq] = ""
                continue
            info[seq] += line
    return info


def overlap_graphs(file):
    results = []
    for id, seqs in file.items():
        for id2, seqs2 in file.items():
            if id != id2:
                if seqs[-3:] == seqs2[:3]:
                    results.append((id, id2))
    with open("results.txt", "w") as f:
        for result in results:
            f.write(result[0] + " " + result[1] + "\n")


if __name__ == "__main__":
    info = get_seqs("/home/beatriz/Downloads/rosalind_grph.txt")
    overlap_graphs(info)
