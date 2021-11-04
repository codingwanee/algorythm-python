# 기본적인 최대공약수 구하는 방식
def greatest(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1        # i를 1만큼 감소시킴


print(greatest(126, 64))

# 유클리드 알고리즘

# 수학자로 유명한 유클리드(Euclid)의 발견에 따르면, 최대공약수에 다음과 같은 성질이 있다.
# a와 b의 최대공약수는 'b'와 'a를 b로 나눈 나머지'의 최대공약수와 같다. 즉, gcd(a, b) = gcd(b, a%b)
# 어떤 수와 0의 최대공약수는 자기 자신이다. 즉, gcd(n, 0) = n

def uclid(a, b):
    if b == 0:
        return a
    return uclid(b, a%b)




# 삽질버전
# 1) a의 약수를 모두 구한다
# 2) b의 약수를 모두 구한다
# 3) a, b의 약수 중 공약수를 모두 구한다
# 4) 공약수 중 최대값(최대공약수)를 반환한다
def solution(a, b):
    bufA = []
    bufB = []
    for i in range(a):
        if a % i == 0:
            bufA.append(i)
    for j in range(b):
        if b % j == 0:
            bufB.append(j)
    buffer = set()
    for i in bufA:
        for j in bufB:
            if bufA[i] == bufB[j]:
                buffer.add(bufA[i])
    return buffer