import sys 



__positive=0
__negative=0
__zero=0

a = 0.05
a = 0 
def parse_file(fn):
    print fn
    global __positive 
    global __negative 
    global __zero 

    f = open(fn, "r")
    for line in f:
        if float(line) > a:
            __positive = __positive + 1
        elif float(line)< 0-a :
            __negative = __negative + 1
        else:
            __zero = __zero + 1
    f.close()
    #print __positive, __negative, __zero, __positive+__negative+__zero

parse_file(sys.argv[1])

print '\t+, -, 0'
print '\t',__positive, __negative, __zero

