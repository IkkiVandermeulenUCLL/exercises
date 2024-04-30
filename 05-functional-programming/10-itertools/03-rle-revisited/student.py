from itertools import groupby, repeat

def rle_encode(data):
    groups = (list(g) for _,g in groupby(iter(data)))
    return ((group[0], len(group)) for group in groups)

def rle_decode(data):
    return (char for char,count in iter(data) for i in range(count))