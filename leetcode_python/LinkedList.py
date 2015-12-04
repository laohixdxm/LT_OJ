class ListNode():
  def __init__(self, x):
    self.val = x
    self.next = None


def linkedlist(listOfNode): 
  for i in range(len(listOfNode)):
    listOfNode[i].next = listOfNode[i+1]
  return listOfNode


def output_list(head):
  node = head
  i=0
  while(node!=None):
    print(node.val, "->", end="")
    node = node.next
    i+=1
    if(i==10):
      break
  print()


nodeA = ListNode(1)
nodeB = ListNode(1)
nodeC = ListNode(2)
#print(nodeC.val)

list1 = linkedlist([nodeA, nodeB, nodeC])
#print(list1[0].val)
output_list(list1[0])