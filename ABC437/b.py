# TODO edit this code


def main():
    h, w, n = map(int,input().split())
    aaa = [set(map(int, input().split())) for _ in range(h)]
    bb = set(int(input()) for _ in range(n))
    best_count = 0
    for aa in aaa:
        count = 0
        for a in aa:
            for b in bb:
                if a == b:
                    count += 1
        if best_count < count:
            best_count = count
    print(best_count)
main()

#最適解
def gpt_main():
    h, w, n = map(int, input().split())
    aaa = [set(map(int, input().split())) for _ in range(h)]
    bb = set(int(input()) for _ in range(n))
    print(max(len(aa & bb) for aa in aaa)) #len(aa & bb)その行に 何個 B が含まれているか
main()


#覚えること
#set は「重複しない要素の集まり」ex) s = {1, 2, 3}
#重複しない | 同じ値は1つだけ
#順番がない | インデックス `s[0]` は使えない
#高速       | `in` 判定がめちゃ速い       
# set の正体：ハッシュ表
# 値 → ハッシュ値（数字）に変換
# その数字を **住所（インデックス）**として使うだから速い