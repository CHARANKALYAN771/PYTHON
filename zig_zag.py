class Solution:

    def zigZag(self,arr, n):
        
        i=0
        while(i<n-1):
            if i%2==0 :
                if arr[i]>arr[i+1]:
                    t=arr[i]
                    arr[i]=arr[i+1]
                    arr[i+1]=t
            else:
                if arr[i]<arr[i+1]:
                    x=arr[i]
                    arr[i]=arr[i+1]
                    arr[i+1]=x
            i+=1

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.zigZag(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
