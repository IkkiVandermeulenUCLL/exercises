# Write your code here
def remove_duplicates(xs):
    gevonden = set()
    result = []
    for x in xs:
        if x not in gevonden:
            gevonden.add(x)
            result.append(x)
    return result