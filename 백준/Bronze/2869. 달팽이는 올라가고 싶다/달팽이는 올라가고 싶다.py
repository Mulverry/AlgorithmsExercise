a, b, v = map(int, input().split())

# 정상에 오르면 미끄러지지 않는다. a*time + (-b+a)*(time -1) = v
time = (v-b) / (a-b)
if time == int(time):
    print(int(time))
else:
    print(int(time) + 1) 