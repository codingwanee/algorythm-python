# 최댓값 구하기
# 입력: 숫자가 n개 들어있는 리스트
# 출력: 숫자 n개 중 최댓값

def find_max(a):
    n = len(a)
    max = a[0]
    idx = 0
    for i in range(1, n):
        if a[i] > max:
            max = a[i]
            idx = i

    return i

a = [1, 3, 5, 7, 9]

print(find_max(a))



b = [0, 3, 4, 19, 72, 9]

def my_solution(b):
    n = len(b)
    b.sort()
    return b[n-1]

print(my_solution(b))


c = [0, 3, 4, 19, 72, 9]
def solution2(c):
    buffer = -1;
    for i in b:
        if i < i + 1:
            buffer = i
    return buffer

print(solution2(c))


numbers = list(map(int, input().split()))
print(my_solution(numbers))