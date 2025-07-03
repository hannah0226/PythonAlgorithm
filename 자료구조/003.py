import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
temp=0
array_sum = [0]

# 합배열 계산
for i in n_list:
    temp = temp + i
    array_sum.append(temp)

# 구간합 계산
for i in range(m):
    s, e = map(int, input().split())
    print(array_sum[e]-array_sum[s-1])