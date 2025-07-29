연도 = int(input())

if 연도 % 4 == 0 and 연도%100!=0 :
    print("1")
elif 연도 % 400 == 0 :
    print("1")
else :
    print("0")


