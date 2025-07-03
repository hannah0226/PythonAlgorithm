import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0]*n
C = [0]*m
S[0] = A[0]
answer = 0

# 배열 합 계산
for i in range(1,n):
    S[i] = S[i-1] + A[i]

# 배열 합 각 원소에 나머지 연산
for i in range(n):
    M = S[i] % m
    if M == 0:
        answer += 1
    C[M] += 1 # C인덱스 = 나머지 값 (나머지가 같은 숫자의 개수 세기)

# 나머지가 같은 인덱스 중 2개 뽑는 경우의 수 구하기
for i in range(m):
    if C[i]>1:
        answer += (C[i] * (C[i] - 1) // 2) # /는 float로 계산되므로 // 정수로 계산

print(answer)
