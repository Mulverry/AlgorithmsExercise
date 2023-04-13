n = input()
cycle = 0

if len(n) < 2:
    n = "0" + n 

tmp = n
     
while True:
   new = int(tmp[0]) + int(tmp[1]) 
   new = str(new)
   cycle += 1
   tmp = tmp[1] + new[(len(new)-1)]
        
   if tmp == n:
       print(cycle)
       break