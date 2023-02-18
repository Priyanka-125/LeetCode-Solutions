class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r = []
        w = []
        b = []

        for i in range(len(nums)):
            if nums[i] == 0:
                r.append(0)

            if nums[i] == 1:
                w.append(1)

            if nums[i] == 2:
                b.append(2)
	
        nums.clear()
        nums.extend(r)
        nums.extend(w)
        nums.extend(b)
        
        '''
        #include <stdio.h>

int main()
{
    int n,nums[100],r=0,b=0,g=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&nums[i]);
        if(nums[i]==0){
            r+=1;
        }
        else if(nums[i]==1){
            b+=1;
        }
        else{
            g+=1;
        }
    }
    for(int i=0;i<n;i++){
        if(r>0){
            nums[i]=0;
            r-=1;
        }
        else if(b>0){
            nums[i]=1;
            b-=1;
        }
        else{
            nums[i]=2;
            g-=1;
        }
    }
    for(int i=0;i<n;i++){
        printf("%d ",nums[i]);
    }
}'''
        