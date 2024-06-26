# Write your code here
def process_data(string_data):
    result = dict()
    for x in string_data:
        name, age,*courses = x.split(",")
        result[name]= {'age':int(age), 'courses': courses}
    return result

def average_age(data):
    total=[]
    for k in data.keys():
        total.append(data[k]['age'])
    return sum(total)/len(total)

def courses(data):
    result = set()
    for k in data.keys():
        for course in data[k]['courses']:
            result.add(course)
    return result

def most_common_courses(data):
    map = dict()
    result= set()
    hoogste =0

    for v in data.values():
        for course in v['courses']:
            map.setdefault(course,1)
            map[course]+=1
    for k,v in map.items():
        if v>hoogste:
            hoogste=v
    for k,v in map.items():
        if v==hoogste:
            result.add(k)
    return result