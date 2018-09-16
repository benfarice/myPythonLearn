print "Hello There !! My Name is Youssef Imzoughene "
p =[1,2]
q = [3,4]
p.append(q)
print len(p)

def print_all_elements(p):
    i = 0
    while i<len(p):
        print p[i]
        i = i + 1
print_all_elements(p)