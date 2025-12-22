def main():
    num = input()
    ans = ""
    for i in range(3):
        if num[i] == "1":
            ans += "9"
        else:
            ans += "1"
    print(int(ans))
main()

#最適解
def gpt_main():
    n = input()
    n = n.replace("1", "x")
    n = n.replace("9", "1")
    n = n.replace("x", "9")
    print(n)
    return

#覚えること
#文字列.replace(置き換え前, 置き換え後)
#文字列の中身を別の文字に置き換えるメゾット