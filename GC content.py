seq = input("Write a DNA sequence using only nucleotides(A,T,G,C): ").upper()
nucleotides = {"A", "T", "G", "C"}
def seq_validation(sequence):
    return all(nuc in nucleotides for nuc in sequence )

while not seq_validation(seq):
    print("Choose only from the existing nucleotides (A, T, G, C). Try again.")
    seq = input("Write a DNA sequence using only nucleotides (A, T, G, C): ").upper()


def calculate_gc_content(sequence):
    gc_content = (sequence.count("G") + sequence.count("C") )/ len(sequence) * 100
    return f"GC content of {sequence} is {round(gc_content, 2)}%"
print(calculate_gc_content(seq))
