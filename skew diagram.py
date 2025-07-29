import matplotlib.pyplot as plt
def calculate_skew(sequence):
    skew = [0]
    score = 0
    for nuc in sequence:
        if nuc == "C":
            score -= 1
        if nuc == "G":
            score += 1
        skew.append(score)
    return skew


seq = "CATGGGCATCGGCCATACGCC"
print(calculate_skew(seq))
skew_values = calculate_skew(seq)
positions = range(len(calculate_skew(seq)))
plt.plot(positions, skew_values)
plt.xlabel("Position")
plt.ylabel("Skew")
plt.grid(True)
plt.show()
#This code computes the cumulative GC skew across a DNA sequence to track changes in nucleotide composition position by position and creates a plot, done