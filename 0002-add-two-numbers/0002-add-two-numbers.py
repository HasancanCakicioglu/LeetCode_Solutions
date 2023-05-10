class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def getLengthOfNode(node):
        if (node==None):
            return 0
    
        length = 1
        while(node.next!=None):
            node = node.next
            length += 1
    
        return length

    @staticmethod
    def plus_finder(x):
        plus =0
        while x>=10:
            x = x-10
            plus = plus+1
        return plus

    @staticmethod
    def fillLinkedList(listNode, sumList):
        for i in range(len(sumList)):
            listNode.val = sumList[i]
            if i != len(sumList)-1:
                listNode.next = ListNode()
                listNode = listNode.next

    @staticmethod
    def addTwoNumbers(l1, l2):
        l1_len = Solution.getLengthOfNode(l1)
        l2_len = Solution.getLengthOfNode(l2)

        l1_list = l1
        l2_list = l2

        l1_values = []
        l2_values = []

        while l1_list != None:
            
            l1_values.append(l1_list.val)
            l1_list = l1_list.next

        while l2_list != None:
            l2_values.append(l2_list.val)
            l2_list = l2_list.next
        
        
        

        sumList = []
        plus = 0
        
        for i in range(max(l1_len,l2_len)):
            x = l1_values[i] if l1_len > i else 0
            y = l2_values[i] if l2_len > i else 0
            
            if (x+y+plus >= 10):
                
                
                    
                print(str(x)+" - "+str(y)+" - "+str(plus)+" - "+str(x+y+plus)+" *")
                sumList.append(x+y-10+plus)
                plus = Solution.plus_finder(x+y+plus)
            else:
                print(str(x)+" - "+str(y)+" - "+str(plus)+" - "+str(x+y+plus))
                sumList.append(x+y+plus)
                plus = 0
        if plus is not 0:
                sumList.append(plus)

        

        myNode = ListNode()
        Solution.fillLinkedList(myNode, sumList)

        return myNode

