checkList = [0]*4 # A,C,G,T의 최소 개수
myList = [0]*4 # 현재 윈도우 내 A,C,G,T의 개수
checkSecret = 0 # 현재까지 조건을 만족한 문자의 종류 개수

# 새로 들어오는 문자 처리 함수
def myadd(c):
    global checkList, myList, checkSecret

    if c=='A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c=='C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c=='G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c=='T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

# 제거되는 문자 처리 함수
def myremove(c):
    global checkList, myList, checkSecret

    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

# 최소 등장 횟수가 0이면 자동으로 조건 만족
for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

# 초기 P 부분 문자열 처리
for i in range(P):
    myadd(A[i])

if checkSecret == 4:
    Result += 1

# 슬라이딩 윈도우 이동하며 결과 세기
for i in range(P,S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)