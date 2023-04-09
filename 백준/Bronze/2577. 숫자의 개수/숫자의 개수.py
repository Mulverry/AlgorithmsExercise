a = int(input())
b = int(input())
c = int(input())

mul = a*b*c
str_list = list(str(mul))

print(str_list.count("0"))

for i in range(1, 10):
    print(str_list.count(f"{i}"))