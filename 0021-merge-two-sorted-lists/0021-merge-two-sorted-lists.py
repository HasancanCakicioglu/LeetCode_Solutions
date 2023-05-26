class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
        
class Solution:

    def adjustLinkedList(self,list1,list2,myNode):
        temp = myNode
        while list1 is not None or list2 is not None:
            if list1 is None:
                myNode.val = list2.val
                list2=list2.next
            elif list2 is None:
                myNode.val = list1.val
                list1=list1.next
            elif list1.val < list2.val:
                myNode.val = list1.val
                list1=list1.next
            else:
                myNode.val = list2.val
                list2=list2.next

            
            if (list1 != None or list2 !=None):
                print("girdi")
                myNode.next = ListNode()
                myNode = myNode.next
        return temp


    def mergeTwoLists(self,list1,list2):
        
        myNode= ListNode()
        if list1==None and list2==None:
            return None

        if list1 == ListNode() and list2 == ListNode():
            return ListNode()
        myNode = self.adjustLinkedList(list1,list2,myNode)
        

        return myNode