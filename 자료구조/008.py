import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0

for i in range(n):
    find = a[i]
    start = 0
    end = n - 1

    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue

        total = a[start] + a[end]

        if total == find:
            count += 1
            break
        elif total < find:
            start += 1
        else:
            end -= 1

print(count)
