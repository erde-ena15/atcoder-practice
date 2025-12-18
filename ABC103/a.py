def main():
    a = list(map(int, input().split()))
    # i,j,kはタスク番目を示している
    costs = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i != j and j != k and k != i:
                        costs.append(abs(a[j]-a[i]) + abs(a[k]-a[j]))
    print(min(costs))
main()


#覚えること
# abs()
# 絶対値を取る関数

#sorted(a, reverse=False)
# リストを昇順にソートする関数
# 降順にするにはreverse=Trueにする