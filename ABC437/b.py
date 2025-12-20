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
    return

#覚えること
