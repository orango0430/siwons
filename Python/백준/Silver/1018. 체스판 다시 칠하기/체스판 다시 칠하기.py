A,B=map(int,input().split())
S=[input() for _ in range(A)]        
def repaint_count(x, y):
    count_w = 0  
    count_b = 0  
    for i in range(8):
        for j in range(8):
            current = S[x + i][y + j]
            if (i + j) % 2 == 0:
                if current != 'W':
                    count_w += 1
                if current != 'B':
                    count_b += 1
            else:
                if current != 'B':
                    count_w += 1
                if current != 'W':
                    count_b += 1
    return min(count_w, count_b)
min_paint = float('inf')
for i in range(A - 7):
    for j in range(B - 7):
        min_paint = min(min_paint, repaint_count(i, j))
print(min_paint)
