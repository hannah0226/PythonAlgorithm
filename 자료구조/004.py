import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0]*(n+1)] # 0행과 0열은 계산을 편하게 하기 위해 0으로 설정
D = [[0]*(n+1) for _ in range(n+1)] # [0,0,...,0]리스트를 n+1번 반복해서 2차원 배열 만듦

# 입력받아 A 채우기
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# 합배열 계산해서 D 채우기
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 구간 합 배열 출력
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)

