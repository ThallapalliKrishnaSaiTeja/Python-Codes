l = list(map(int,input().split()))
m = []
for i in l:
    if l.count(i)==1:
        m.append(i)
print(m)
