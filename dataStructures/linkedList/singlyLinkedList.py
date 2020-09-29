class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode

    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next


    
#firstNode=Node("john")
#linkedLst=LinkedList()
#linkedLst.insert(firstNode)
#secondNode=Node("Ben")
#linkedLst.insert(secondNode)
#thirdNode=Node("agath")
#linkedLst.insert(thirdNode)
#linkedLst.printList()
#print(thirdNode.data)
#print(thirdNode.data)
#print(thirdNode.data)

ll=LinkedList()#note:class LinkedList should be initialized like
        #this we cannot directly use
        #ll.insert(Node(input('enter your name')))
        #this wont work
        
def createLinkdList(num):
    for i in range(num):
        ll.insert(Node(input('enter your name')))

createLinkdList(int(input('enter size of node')))

ll.printList()
