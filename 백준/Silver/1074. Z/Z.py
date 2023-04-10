# 참고 : https://ggasoon2.tistory.com/11

def visit(N, r, c):
    # base
    if N == 0:
        return 0
    
    # recursive : n이 1일 때 z 이동방식 + n이 2배가 되면(x,y값이 2배로 늘면) 값은 4배가 됨.
    return 2*(r %2) + (c%2) + 4*visit(N-1, int(r/2), int(c/2))
    
    


N, r, c = map(int, input().split())
print(visit(N, r, c))
