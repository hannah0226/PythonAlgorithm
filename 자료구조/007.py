import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = list(map(int, input().split()))
a.sort()

count = 0
i = 0
j = n-1

while i < j:
    if a[i] + a[j] > m:
        j -= 1
    elif a[i] + a[j] < m:
        i += 1
    elif a[i] + a[j] == m:
        count += 1
        i += 1
        j -= 1

print(count)