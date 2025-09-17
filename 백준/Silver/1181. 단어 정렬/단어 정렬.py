A=int(input())
words=[]
for i in range(A):
    B=input()
    words.append(B)
words=list(set(words))
words.sort(key=lambda x:(len(x),x))    
print('\n'.join(words))

