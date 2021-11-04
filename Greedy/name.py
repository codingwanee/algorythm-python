def solution(name):
    answer = 0

    n = len(name)

    # 최소한 n-1 만큼 커서 이동
    # A~Z는 총 26개
    # A ~ M 13개 / N ~ Z 13개
    #

    buffer = []

    for i in name:
        buffer.append(i)

    for i in range(0, n):
        if ord(buffer[i]) <= 77:
            answer += ord(buffer[i]) - 65
        else:
            answer += 26 - (ord(buffer[i]) - 65)







    return answer


name = "JEROEN"
print(solution(name))
