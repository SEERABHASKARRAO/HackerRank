n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    a=input()
    if(a[0]=='p'):
        s.pop()
    elif(a[0]=='r'):
      if(int(a[-1]) in s):
        s.remove(int(a[-1]))
      else:
        continue
    elif(a[0]=='d'):
        s.discard(int(a[-1]))
print(sum(s))
