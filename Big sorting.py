n=int(input())
s=''
p=[]
for i in range(n):
    s=input()
    p.append(s)
p.sort(key=int)
for i in p:
    print(i)
