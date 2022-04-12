class Solution:

    def maxSubArraySum(self,arr,N):
        if arr[0]>0:
            m=arr[0]
        else:
            m=max(arr)
        x=0
        for i in range(N):
            x=x+arr[i]
            if x<0:
                x=0
            elif m<x:
                m=x
        return m

import math
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()