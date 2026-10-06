
def main():
    n=int(input())
    rest=set(map(int, input().split()))
    total=n*(n+1)//2
    missnum=total-sum(rest)
    print(missnum)

if __name__ == "__main__":
    main()
