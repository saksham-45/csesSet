#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);
    printf("%lld\n", n);
    while(n!=1){
        if(n%2==0){
            n=n/2;
        } else{
            n=3*n+1;
        }
        printf("%lld\n", n);
    }
    return 0;
}