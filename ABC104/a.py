def main():
    # param
    n = int(input())
    # solve
    if n <1200:
        ans = "ABC"
    elif 1200 <= n < 2800:
        ans = "ARC"
    else:
        ans = "AGC"
    # answer
    print(ans)

main()

