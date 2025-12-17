# TODO edit this code

def main():
    # param
    n = int(input())
    # solve
    if n % 2 != 0:
        i = n + 1
    else:
        i = n
    while True:
        if i % n == 0:
            print(i)
            return
        i += 2
main()

#最適解
def gpt_main():
    n = int(input())
    print(n if n % 2 == 0 else n * 2)

# N が 偶数 のとき
# → すでに 2 で割り切れる
# → 答えは N

# N が 奇数 のとき
# → 2 で割り切れない
# → 2N が最小

#覚えること
#三項演算子
# a if a == 0 else a+1
# 真ん中の条件を満たすとき左、そうでなければ右