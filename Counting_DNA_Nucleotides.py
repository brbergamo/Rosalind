sample = "GCGCCTCGCCGGGGTCAAATGATAATACTCTGATGTGCGATGGTAGTTTGACCTTGTCAGCGGATGACTAGGAATTCTCTCTCCATTATGCCATGAGGAACGCTGGCGATAGGGGGGCATTGTGGGAAGATCGGCGTGCCTATATGATTTGAGCTCTTCAAAACATGCAGATGGCGTGTACCCTTCTTCGGCACTACGGCTCTAGACAACCTCGACATTAAGACTCCACGGTGGGAAAGAACTTACCTCAGGTTCATGCCAAGAATGCCACGCTCCTGTCCGCAACGCACGTTCTGTGAACGAAGCCGACGCTACCCAAGAGCTTATTTCGCCAAAGAGTCGGCCCATCCCTATTTAGAGATTGTTGTCTGCGCCTATCGTAGCGAATAAATCCACGCTAGAACATATCGGTGCCAGTACACATAGGTGGTCTAAAAGTGCTTGGTGAAGCGTATCAATCCTGCACTGCTTGGGTCTCAAATCATCTACGGGCATTTAACGTCATCGTGCTGATTCGAGAATATACGTTATGCGTTAACACCTCTCCCTCCTTTACAACTGCAAGCCTGTTTATAAGCGCGCTAACATGTTTCACGATATCACTACCGTAGTATGAAAATTCCCTCACATGCCACCTATAAATCCATTCTTCGCTTATGCGTTTTTTGGGAGCCTCACACTCTAAGGTGTGATTCCCTACTTTATTTACATCGGAGGCCACAGGAGTTGTCATAAGCATGCTATTTTCCGGTCCTCTCTTACTGGATTGCTGAGGCTCTTAGGAGGACACAGTTTTGTAGATCTGCTAAGTCTTACTCAGGTGGCGGTCCTGAACCAGACCCTATCGTGAGACATTGTTGGGTCTGGATGGCAAAATGCGCACAGATCC"


def count_bases(string):
    a = string.count("A")
    t = string.count("T")
    g = string.count("G")
    c = string.count("C")
    print(a, c, g, t)


count_bases(sample)
