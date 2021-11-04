def solution(n):
    answer = 0;
    for i in range(n+1):
        answer += i
    return answer

b = solution(10)
print(b)