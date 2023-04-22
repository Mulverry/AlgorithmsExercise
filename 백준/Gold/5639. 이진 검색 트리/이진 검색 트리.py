import sys
sys.setrecursionlimit(10**9)
        
def postorder(start, end): # start, end : 시작인덱스, 끝 인덱스 / arr[start]는 루트노드
    if start > end:
        return
    
    Right = end + 1  # Right는 오른쪽 트리의 시작 노드의 인덱스. 루트노드보다 큰 값이 존재하지 않을 경우를 대비하여 일부러 end보다 큰 값을 넣었다.
    
    for i in range(start+1, end+1): #루트노드 다음부터 end까지
        if arr[start] < arr[i]: #루트노드보다 큰 값이 있다면
            Right = i #오른쪽트리의 시작노드의 인덱스를 바로 i로 바꾼다
            break
        
    postorder(start+1, Right-1) # 왼쪽 트리 순회:
    postorder(Right, end) # 오른쪽 트리 순회: 만약 루트노드보다 큰 값이 없어서 Right = end+1라면 postorder에서 start>end가 되므로 자동으로 아무것도 없이 리턴.
    print(arr[start]) # 루트노드는 마지막 출력


input = sys.stdin.readline
arr = []

while True: #try 실행할 코드, except 예외처리. 예외가 발생하면 바로 except로 감.
    try:
        arr.append(int(input()))
    except:
        break

postorder(0, len(arr)-1) # 시작인덱스, 끝인덱스