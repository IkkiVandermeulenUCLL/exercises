# Write your code here
def add_indices(xs):
    lijst = []
    for x in range(len(xs)):
        lijst.append(x)
    return list(zip(lijst,xs))