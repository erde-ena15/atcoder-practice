def main():
    num = int(input())
    n = num
    s = 0
    while True:
      s += n % 2
      n = n // 2
      if n == 0:
         break
    print("Yes" if num % s == 0 else "No")
main()

 # i = 0
    # print(len(s1))
    # for i in range(len(s1)):
    #    s2+=s1[len(s1)-i-1]
    # print(int(s2))
#最適解

#覚えること
#str.count("a")
#文字列やリストの中に、ある要素が何個あるか数えるメソッド
