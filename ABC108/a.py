def main():
    # param
    n = int(input())
    # answer
    ans = 0
    for i in range(2, n + 1, 2):
        for j in range(1, n + 1, 2):
            ans += 1
    print(ans)
main()

#最適解
def main():
    K = int(input())
    even = K // 2
    odd = K - even
    print(even * odd)

main()

#解説
# 選ぶ順番は考慮しない
# → (偶数, 奇数) は一意
# 偶数と奇数は 独立に選べる
# 組み合わせ数 = 掛け算

#覚えること
#range(stop) ex) range(5)　0 から 4 まで
#0からstopまでループする

#range(start, stop) ex) range(2, 5)　2, 3, 4
#startからstopまでループする

#range(start, stop, step) ex) range(1, 10, 2) 1, 3, 5, 7, 9
#startからstopまでstepずつループする

# // 整数除算　ex）5 // 2 = 2
#少数部分を切り捨てる
