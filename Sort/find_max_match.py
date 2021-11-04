def solution(numbers):
    answer = ''

    # 주어진 수의 첫번재 숫자를 구한다
    # 주어진 수 중에서 첫번째 숫자를 비교하여 가장 큰 수를 찾는다
    # 앞자리 숫자가 같으면 두번째 자리 숫자를 비교하여 순서를 정한다. x ...
    # 순서대로 붙인다

    # 주어진 수를 자릿수 별로 쪼개기

    n = len(numbers)

    global_buffer = []
    second_buffer = []

    # 자리수 쪼개기
    for i in range(0, n):
        buffer = []
        buffer.append(int(numbers[i] / 1000) % 10)
        buffer.append(int(numbers[i] / 100) % 10)
        buffer.append(int(numbers[i] / 10) % 10)
        buffer.append(int(numbers[i] / 1) % 10)

        # 저장하기
        global_buffer.append(buffer)

    # 첫번째 자리수 발라내기

    for i in range(0, 4):

    # 각 숫자들의 첫번째 자리수 비교 / 같은 수라면 그다음 숫자

    return answer