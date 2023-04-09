a = input()
b = input()

def cal(a, b):
    a = int(a)
    
    first = a * int(b[2])
    second = a * int(b[1])
    third = a * int(b[0])
    final = a * int(b)
    
    print(first, second, third, final, sep="\n")

cal(a, b)