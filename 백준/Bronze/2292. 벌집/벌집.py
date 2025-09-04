import sys
input = sys.stdin.readline
n = int(input())
layer = 1 # 고리번호
end = 1 # 고리의 끝 번호
while n > end:
    end += 6*layer
    layer += 1
print(layer)