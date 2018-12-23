'''
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''
import pdb
class ListNode:
	def __init__(self,val=None):
		self.val=val
		self.next=None
class solution:
	def DeleteListNode(self,head,targetVal=None):
		head_list = head
		if head==None:
			return 
		if head.next==None:
			head=None
		while head.val!=targetVal:
			head=head.next
			if head==None:
				print('cannot find the target value %d' % targetVal)
				return False
				break
		ptr = head
		head=head.next
		ptr.val=head.val
		head.val=targetVal
		ptr.next=head.next
		while head_list!=None:
			print(head_list.val)
			head_list=head_list.next
		return True


		return False

s=solution()
node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
flag=s.DeleteListNode(node1,7)
print(flag)
flag=s.DeleteListNode(None)
print(flag)
