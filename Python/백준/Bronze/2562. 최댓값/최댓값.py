A=[]
for i in range(9):
    B=(int(input()))
    A.append(B)
print(max(A))
print(A.index(max(A))+1)
