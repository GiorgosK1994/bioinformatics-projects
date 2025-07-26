def find_pattern(seq, pattern):
    for k in range(0, len(seq)):
        if seq[k:k + len(pattern)] == pattern:
            return k

seq1 = "GACGATATACGACGATA"
pattern1 = "CGA"
print(find_pattern(seq1, pattern1))

