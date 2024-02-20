data = ['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry,Math']
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

def most_common_course(data):
    map = dict()
    for v in data.values():
        for course in v['courses']:
            map.setdefault(course,1)
            map[course]+=1
    return map

print(process_data(data))
print(courses(process_data(data)))
print(most_common_course(process_data(data)))