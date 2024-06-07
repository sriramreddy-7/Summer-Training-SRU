# l=[2,1,2,2]
# l=[6,6,6,6,7]
# l=[1,1,1,2,2,2]
# k=len(l)//2
# for i in range(len(l)):
#     if l.count(l[i])>k:
#         print(l[i])
#         break
# else:
#     print(1)
# s=set(l)
# c=0
# k=len(l)//2
# for i in range(len(l)):
#
# l=[4,8,2,4,4,8,4]
# maxe=max(l)
# maxe=maxe+1
# ht=[0]*maxe
# if l==[]:
#     print(-1)
# for i in range(len(l)):
#     if ht[l[i]] in ht:
#         ht[l[i]]+=1
#     else:
#         ht[l[i]]=1
# print(ht)
# for j in range(len(ht)):
#     if ht[j]>len(l)//2:
#         print(j)
#         break

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         t=head
#         while(t!=None and t.next!=None):
#             if t.next.val==val:
#                 if t.next.next==None:
#                     t.next=None
#                 else:
#                     t.next=t.next.next
#             t=t.next
#         return head
n=7
l=[0,5,3,6,7,2,1]
# maxe=max(l)
# maxe=maxe+1
# ht=[0]*maxe
# if l==[]:
#     print(-1)
# for i in range(len(l)):
#     if ht[l[i]] in ht:
#         ht[l[i]]+=1
#     else:
#         ht[l[i]]=1
# for j in range(len(ht)):
#     if ht[j]==0:
#         print(j)

se=sum(l)
sl=((n)*(n+1))//2
print(sl-se)
