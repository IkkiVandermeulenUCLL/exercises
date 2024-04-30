def rle_encode(data):
    data = iter(data)

    try:
        count=1
        previous = next(data)
        for x in data:
            if x == previous:
                count += 1
            else:
                yield (previous, count)
                previous = x
                count = 1
        yield (previous,count)
    except StopIteration:
        pass

def rle_decode(data):
    data = iter(data)

    try:
        for char, count in data:
            for x in range(count):
                yield char
    except StopIteration:
        pass