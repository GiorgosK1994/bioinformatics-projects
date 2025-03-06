import random
from Bio import pairwise2

nucleotides = ["A", "T","G", "C"]
seq1 = "".join([random.choice(nucleotides) for nuc in range(25)])
seq2 = "".join([random.choice(nucleotides) for nuc in range(25)])
print(f"Sequence 1: {seq1}")
print(f"Sequence 2: {seq2}")
match = int(input("Enter match score: "))
mismatch = int(input("Enter mismatch penalty: "))
open_gap = int(input("Enter gap open penalty: "))
extend_gap= int(input("Enter gap extension penalty: "))
alignments = pairwise2.align.globalms(seq1,seq2, match, mismatch,open_gap, extend_gap)
for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))