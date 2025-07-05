n = int(input())
count = 1 # n 숫자만 뽑는 경우의 수 미리 추가
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum < n:
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1

print(count)