

bool isPalindrome(int x){
    long reveresed=0;
    int n;
    n=x;
    while(n>0){
        int temp;
        temp=n%10;
        reveresed=reveresed*10+temp;
        n=n/10;
    }
    if(reveresed==x)
        return true;
    else
        return false;

}