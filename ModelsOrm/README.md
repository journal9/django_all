 - # Lines

## Contest 4 questions

 - - How would you rate your understanding and experience with threading, multiprocessing, or async programming in Python?
 - class Solution:
 -     # @param A : head node of linked list
 -     # @return the head node in the linked list
 -     def solve(self, A):
 -         if A==None:
 -             return None
 -         slow = A
 -         fast = A
 -         while True:
 -             slow = slow.next
 -             fast = fast.next.next
 -             if slow==fast:
 -                  - break
         - 
        l = A
 -         r = slow - 
        m = r
 -         while True:
 -             l = l.next
 -             m = r
 -             r = r.next
 -             if l==r:
 -                 break
 -         m.next - =None
        
 -     -   -   -    return A



 - class Solution:
 -     # @param A : list of integers
 -     # @return a list of integers
 -     def solve(self, A):
 -         stach = []
 -         ans=[0]*len(A)
 -         for i in range(len(A)-1,-1,-1):
 -             while not len(stach)==0 and A[stach[-1]]<=A[i]:
 -                 stach.pop()
 -             if len(stach)==0:
 -                 ans[i]=0
 -             else:
 -                 ans[i]=stach[-1]-i
 -             stach.append(i)
 -         ans[-1]=0
 -         return ans