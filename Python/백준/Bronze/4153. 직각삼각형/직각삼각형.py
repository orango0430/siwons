result=[]
while True:
    try: 
        A,B,C=map(int,input().split())
        if A == 0 and B == 0 and C == 0 :
            break
        nums=[A,B,C]
        nums.sort()
        if (nums[0]**2) + nums[1]**2 == nums[2]**2 :
            result.append('right')
        else :
            result.append('wrong')
    except :
        break
print("\n".join(result))
    