x, y, w, h = map(int,input().split())

def distance(x, y, w, h):
    print(min(x, y, w-x, h-y))


distance(x, y, w, h)