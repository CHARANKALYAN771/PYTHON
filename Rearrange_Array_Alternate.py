class Solution:

    def rearrange(self,arr, n): 
        
        x=[]
        y=[]
        z=[]
        for i in range(int(n/2)):
            x.append(arr[i])
        for j in range(int(n/2),n):
            y.append(arr[j])
        y.reverse()
        k=0
        l=0
        for i in range(n):
            if i%2==0:
                # k=0
                z.append(y[k])
                k+=1
            elif i%2!=0:
                # l=0
                z.append(x[l])
                l+=1
        # return arr
        for i in range(n):
            arr[i]=z[i]


import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
