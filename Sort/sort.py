array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []

    n = len(commands)

    for i in range(0, n - 1):
        for j in range(0, 2):
            brr = []
            brr = array[commands[i][0]-1:commands[i][1]]
            brr.sort()
            answer.append(brr[commands[i][2]-1])

    return answer

print(solution(array, commands))