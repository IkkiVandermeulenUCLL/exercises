def fizzbuzz():
    i=1
    while True:
        result = ''
        if i%3==0:
            result+='fizz'
        if i%5==0:
            result+='buzz'
        
        if result=="":
            result = str(i)
        yield result
        i+=1