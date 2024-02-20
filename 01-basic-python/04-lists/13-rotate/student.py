# Write your code here
def rotate(xs,n):
    for x in range(n):
        xs.append(xs.pop(0))