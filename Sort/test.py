numbers = [5, 52, 57, 524, 589]

def solution(numbers):
    ans = 0
    for i in range(0, len(numbers)):
        target = str(numbers[i])
        save = numbers[i]
        if int(target) == -1:
            continue
        numbers[i] = -1
        target += str(solution(numbers))
        ans = max(int(target), int(ans))
        numbers[i] = int(save)
    return str(ans)

print(solution(numbers))


# 3 30 34 59