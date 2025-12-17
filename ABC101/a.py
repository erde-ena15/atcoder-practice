# TODO edit this code

def main():
    # param
    str = input()
    num = 0
    for s in str:
        if s == "+":
            num += 1
        else:
            num -= 1
    # answer
    print(num)
main()

#最適解
def gpt_main():
    s = input()
    print(s.count('+') - s.count('-'))

#覚えること
#str.count("a")
#文字列やリストの中に、ある要素が何個あるか数えるメソッド
