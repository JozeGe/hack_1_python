"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    inicio = 1
    while(inicio < 6):
        result.insert(inicio, "@")
        inicio += 2
    return result

r = fn_hack_9()
print(r)



  