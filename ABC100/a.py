# TODO edit this code

def main():
    a,b = map(int, input().split())

    cakes=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # solve
    for i in range(a):
        if cakes[14] == 1 or cakes[15] == 1:
            break
        for j in range(16):
            if cakes[j] != 1:
                if j == 0 and cakes[15] != 1 and cakes[j+1] != 1:
                    cakes[j] = 1
                    i+=1
                    break
                elif j == 15 and cakes[0] != 1 and cakes[j-1] != 1:
                    cakes[j] = 1
                    i+=1
                    break
                elif cakes[j-1] != 1 and cakes[j+1] != 1:
                    cakes[j] = 1
                    i+=1
                    break
    if i != a:          
        print(":(")
        return
    i = 0
    for i in range(b):
        if cakes[14] == 2 or cakes[15] == 2:
            break
        for j in range(16):
            if cakes[j] != 0:
                continue
            if cakes[j] != 2:
                if j == 0 and cakes[15] != 2 and cakes[j+1] != 2:
                    cakes[j] = 2
                    i+=1
                    break
                elif j == 15 and cakes[0] != 2 and cakes[j-1] != 2:
                    cakes[j] = 2
                    i+=1
                    break
                elif cakes[j-1] != 2 and cakes[j+1] != 2:
                    cakes[j] = 2
                    i+=1
                    break
    if i != b:          
        print(":(")
        return
    print("Yay!")
    # print(cakes)
main()

#最適解
def gpt_main():
    a, b = map(int, input().split())

    if max(a, b) <= 8:
        print("Yay!")
    else:
        print(":(")

# 判定条件
# それぞれの人について、

# A ≤ 8

# B ≤ 8

# が両方満たされていれば、
# 2 人を交互に並べたり、空き切れを挟むことで必ず配置できます。
