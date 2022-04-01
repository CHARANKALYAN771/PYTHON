# complexity O(N)
class Solution:
   
   def check(self,A,B,N):
       isSame = True
       
       A = sorted(A)
       B = sorted(B)
       
       for i,j in zip(A,B):
           if ( i != j):
               isSame = False
               break
       
       return isSame