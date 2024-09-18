s = "GTCGTAAAGGTGGTCGTAAGCCTTTGTCGTAACGTCGTAACAGTCGTAACAACCAGCGCCGTCGTAAACCTCGTCGTAAGTCGTAATGTCGTAACAGTCGTAACCCTTGGTGCACGTCGTAACCAAGTCGTAATGTATTGTCGTAAGACGTCGTAAAGTCGTAAGTCGTAAGTCGTAATGGTCGTAATGTCGTAAACGTCGTAAGTCGTAAAGAAGTCGTAAAGTAGTCGTAAGGGTCGTAACGTCGTAAGTCGTAAGTCGTAAGCTGTCGTAAGTCGTAAGTCGTAAGTGTCGTAATACCCGGTCGTAAGTCGTAACGTCGTAAGTCGTAAGTCGTAAATTAGTCGTAAGTCGTAAGTCGTAAATGTCGTAACTACCGTCTGATGTCGTAAGTCGTAATCGTCGTAAAGTCGTAAGTCGTAAATTGTCCGAATCGTCGTAAGTAGTCGTAAGTTTGTCGTAAGTTATAGTCGTAACTTCGGTCGTAAGTCGTAAGTCGTAACGCGTCGTAAGGTCGTAACGTCGTAAGATCGTCGTAATCGCAGTCGTAAGGTCGTAAGCGTCGTAAGCGCGACCGTCGTAACGTCGTAACCGCTTAGTCGTAATCCATGTCGTAAAGTCGTAAGTCGGTCGTAAGTCGTAAATCTGTCGTAAAACGTCGTAAGAGTCGTAACGTCGTAATGTCGTAATGTCGTCGTAAATGTCGTAAGGTCGTAAGGTCGTAATTCCGTCGTAAGTCGTAAAGTCGTAAGAGAAGCAGTCGTAATAGTCGTAAGTCGTAATAGAGTCGTAACGTCGTAAGAGTCGTAACGTCGTAATGTCGTAAGAGTCGTAAGGTCGTAAGACAGTCGTAAAGTCGTAACGTCGTAAGTCGTAAGTCGTAACCCGGTGTCGTAATAAGTCGTAAACGGTCGTAAGTCGTAAGGTCGTAATGGTCGTAATGTCGTAACTCTTGTCGTAAGTCGTAACG"
t = "GTCGTAAGT"


def find_motifs(string, substring):
    positions = []
    for i in range(len(string)):
        if substring in string[i : i + len(substring)]:
            positions.append(i + 1)
    print(positions)


find_motifs(s, t)
