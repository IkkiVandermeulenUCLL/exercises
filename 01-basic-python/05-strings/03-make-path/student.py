# Write your code here
def make_path(parts):
    result=""
    for x in range(len(parts)):
        if x<len(parts)-1:
            result+= parts[x]+"/"
        else:
            result+= parts[x]
    return result