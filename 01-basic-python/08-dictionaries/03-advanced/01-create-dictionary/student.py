# Write your code here
def create_dictionary(keys, values):
    result = dict()
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result