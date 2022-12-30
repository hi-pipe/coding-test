n = int(input())

answer = 1
n -= 1

while n > 0:
    n -= answer * 6
    answer += 1

print(answer)