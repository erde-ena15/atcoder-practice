def main():
    # param
    num = list(map(int, input().split()))
    big_num = ""
    ans = 0
    while len(big_num) < 2:
        for i, n in enumerate(num):
            if n == max(num[0],num[1],num[2]):
                big_num+= str(num[i])
                num[i] = -99
                if len(big_num) == 2:
                    break
    # answer
    for i in range(0,3):
        if num[i] != -99:
            ans = int(big_num) + num[i]
            break
    print(ans)


#自分のコードの最適解
# def main():
#     num = sorted(map(int, input().split()))
#     big_num = str(num[2]) + str(num[1])
#     print(int(big_num) + num[0])


#最適解
# def gpt_main():
#     a = sorted(map(int, input().split()))
#     print(a[0] + a[1] + 10 * a[2])


#覚えること
# リスト.remove(2) ex) 2を削除する
# 指定した 値 を削除

# リスト.pop(1) ex) インデックス1を削除する
# インデックスで削除


#番外
# _の意味　ex)for _ in range(3)
# _ は 「この変数使いません」 という慣習

#リスト内包表記　ex)[int(input()) for _ in range(3)]
#これは ↓ と 完全に同じ
# nums = []
# for _ in range(3):
#     nums.append(int(input()))

