import sys 



__positive=0
__negative=0
__zero=0

a = 0.05

def parse_file(fn):
    print fn
    global __positive 
    global __negative 
    global __zero 

    f = open(fn, "r")
    for line in f:
        if float(line) > a:
            __positive = __positive + 1
        elif float(line)< a :
            __negative = __negative + 1
        else:
            __zero = __zero + 1
    f.close()
    print __positive, __negative, __zero, __positive+__negative+__zero

for i in range(0,8):
    parse_file(str(i)+'.txt')

print '+, -, 0'
print __positive, __negative, __zero, __positive+__negative+__zero
