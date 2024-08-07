from Bio import SeqIO


def get_superstring(reads_list, superstring=""):
    if len(reads_list) == 0:
        return superstring

    elif len(superstring) == 0:
        superstring = reads_list.pop(0)
        print(superstring)
        return get_superstring(reads_list, superstring)

    else:
        for current_read_index in range(len(reads_list)):
            current_read = reads_list[current_read_index]
            current_read_length = len(current_read)

            for trial in range(current_read_length // 2):
                overlap_length = current_read_length - trial

                if superstring.startswith(current_read[trial:]):
                    reads_list.pop(current_read_index)
                    return get_superstring(
                        reads_list, current_read[:trial] + superstring
                    )

                if superstring.endswith(current_read[:overlap_length]):
                    reads_list.pop(current_read_index)
                    return get_superstring(
                        reads_list, superstring + current_read[overlap_length:]
                    )


def main():
    reads = []
    for record in SeqIO.parse("rosalind_long.txt", "fasta"):
        reads.append(str(record.seq))
    superstring = get_superstring(reads)
    with open("superstring.txt", "w") as file:
        file.write(superstring)


if __name__ == "__main__":
    main()
