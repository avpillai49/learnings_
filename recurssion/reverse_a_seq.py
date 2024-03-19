def reverse_sq(seq, start, stop):
    if start < stop - 1:
        seq[start] = seq[stop - 1]
        seq[stop - 1] = seq[start]
        reverse_sq(seq, start+ 1, stop -1)

    
if __name__ == "__main__":
    seq = [2,3,4,12,3,5,6,77,8]