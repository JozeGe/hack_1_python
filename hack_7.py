"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = [5,4,3,2,1,0]
    inicio = 0
    while(inicio <= 5):
     inicio += 1
    return result

r = fn_hack_7()
print(r)   