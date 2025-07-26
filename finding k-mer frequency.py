seq = "CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA"

def k_mer_frequency(sequence):
    dic = {}
    l = []
    for k in range(0, len(sequence) - 2):
        l.append(sequence[k:k+3])

    for k_mer in l:
        if k_mer not in dic:
            dic[k_mer] = 1
        else:
            dic[k_mer] += 1
    return dic
print(k_mer_frequency(seq))



