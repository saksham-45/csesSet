def main():
        strr= input() 
        n =len(strr)
        mx_count=1
        for i in range(n):
            count=1
            for j in range(i+1,n):
                if strr[i]==strr[j]:
                    count+=1
            mx_count=max(count, mx_count)
        return mx_count
if __name__ == "__main__":
    print(main())

