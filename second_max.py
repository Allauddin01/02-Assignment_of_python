lt=[10,9,5,6,7,8,8,9,10,10,9,8,7,5,6]
lr=[]
for i in lt:
    if i not in lr :
        lr.append(i)
lr.sort()
lr.remove(max(lr))
print(max(lr))

