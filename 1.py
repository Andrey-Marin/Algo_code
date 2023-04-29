def gis(n, a):
    inf = float('inf')
    dp = [inf] + [-inf] * n
    prev = [0] * (n + 1)
    pos = [-1] * (n + 1)
    length = 0

    for i in range(n):
        j = binary_search(dp, n, a[i])
        if dp[j - 1] >= a[i] > dp[j]:
            dp[j] = a[i]
            pos[j] = i
            prev[i] = pos[j - 1]
            length = max(length, j)

    print(length, ' - length')

    ans = []
    ans_index = []
    p = pos[length]
    while p != -1:
        ans_index.append(p+1)
        ans.append(a[p])
        p = prev[p]

    print(*ans_index[::-1], ' - ans_index', )
    print(*ans[::-1], ' - ans')


def binary_search(d, n, x):
    left = 0
    right = n
    while left + 1 < right:
        middle = (left + right) // 2
        if d[middle] < x:
            right = middle
        else:
            left = middle
    return right


def main():
    '''Поиск наибольшей невозврастающей подпоследовательности с бин. поиском
    с восстановлением ответа и индексов'''
    n = int(input())
    a = [int(x) for x in input().split()]
    gis(n, a)


if __name__ == '__main__':
    main()

