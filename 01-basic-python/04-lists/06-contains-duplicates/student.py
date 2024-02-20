# Write your code here
def contains_duplicates(xs):
    return sorted(xs) != sorted(list(set(xs)))