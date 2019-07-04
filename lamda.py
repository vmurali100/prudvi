# some = lambda a: a+10;

# print(some(20))
#
# some2 = lambda a,b,c: a+b+c
#
# print(some2(20,40,30))

def calculate(a):
    return  lambda b: b*a

calc = calculate(10)

print(calc(20))