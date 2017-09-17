#python 3

"""it deletes any duplicate
nodes from the list and returns the head of the updated list."""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Solution:
    #function that inserts a node
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
        
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next


    def removeDuplicates(self,head):
        if (head == None):
            return head
        else:
            start = head
            #while we don't come to the end
            
            
            while(start.next != None): 
                second = start.next
                #check current node's value with next node's value
                if (start.data != second.data):
                    
                    start = second
                else:
                    if (second.next == None):
                        start.next = None
                     #if repeated del next node, connect current node with
                     #next's next noce and check that node's value.
                    else:
                        start.next = second.next
                        # if you had written start = start.next you wouldn't have compared
                        # that start with its start.next value rather jumped to compare the following values
                        # so if it is 11 11 11 12, you would have found the first repeating 11s, and deleted second,
                        #but treates third as a new start and began comparing 11 with 12 but not the
                        #first 11 with the third 11. 
                        
       
        return head
    
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
  
  
  
  
  
  
  
  
  
