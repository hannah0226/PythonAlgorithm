n = input()
score_list = list(map(int, input().split()))

# (A/M*100 + B/M*100 + C/M*100)/3 = (A+B+C)*100/M/3
max_score = max(score_list)
sum = sum(score_list)

print(sum * 100/max_score/int(n))