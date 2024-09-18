file_path = "/home/beatriz/Downloads/rosalind_gc.txt"
dict_seqs = {}

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if ">" in line:
            seq_id = line[1:]
            dict_seqs[seq_id] = ""
            continue
        dict_seqs[seq_id] += line


def gc_content(seqs):
    answer = ["", 0]
    for key, value in seqs.items():
        gc_value = (value.count("G") + value.count("C")) / len(value) * 100
        if gc_value > answer[1]:
            answer = [key, gc_value]
    print(answer[0], answer[1], sep="\n")


gc_content(dict_seqs)
