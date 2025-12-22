# TODO edit this code


def main():
    data = []
    t = int(input())
    for i in range(t):
        n = int(input())
        temp = [list(map(int,input().split())) for _ in range(n)]
        data.append(temp)
    
    ans = []
    for dat in data:
        pt = []
        total = 0
        for da in dat:
            pt.append(da[1] + da[0])
            total += da[0]
        ans_temp = len(dat)
        total_power = 0 
        pt.sort()
        while pt and total >= total_power:
            total_power += pt.pop()
            ans_temp -= 1
        ans.append(ans_temp)
    for a in ans:
        print(a)
main()

def fixed_main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        pt = []
        total_power = 0  # ← ΣP

        for _ in range(n):
            W, P = map(int, input().split())
            pt.append(W + P)
            total_power += P

        pt.sort()

        used = 0
        count = 0
        for c in pt:
            if used + c <= total_power:
                used += c
                count += 1
            else:
                break

        print(count)

main()


#最適解
def gpt_main():
    return

#覚えること
