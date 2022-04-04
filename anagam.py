class Solution:
    def isAnagram(self,a,b):

        if len(a)!=len(b):
            return False
        x=[]
        y=[]
        for i in range(len(a)):
            x.append(a[i])
        for i in range(len(b)):
            y.append(b[i])
        x.sort()
        y.sort()
        if x==y:
            return True
        else:
            return False

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
