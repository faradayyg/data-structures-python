#!/usr/bin/python3

from LinkedList.Node import Node

class LinkedList(object):

  def __init__(self):
    self.head = None
    self.counter = 0

  # Time complexity of O(1) for inserting at start
  def insert_start(self, data):
    self.counter += 1
    new_node = Node(data)
    if self.head is None: 
      self.head = new_node
    else:
      new_node.next_node = self.head
      self.head = new_node

  #Time Complexity of O(N)
  def traverse(self):
    actual_node = self.head

    while actual_node is not None:
      print("%r " % actual_node.data)
      actual_node = actual_node.next_node

  #Normally should be O(N) but O(1) here coz we factored size into the transversal 
  def size(self): 
    return self.counter

  #Worst case of O(N) for inserting
  def insert_end(self, data):
    self.counter += 1

    if self.head is None:
      self.insert_start(data)
      return
    
    new_node = Node(data)
    actual_node = self.head

    if actual_node.next_node is None: 
      actual_node.next_node = new_node

    else: 
      while actual_node.next_node is not None:
        actual_node = actual_node.next_node

      actual_node.next_node = new_node

  def remove(self, data): 
    self.counter -= 1
    
    if self.head is not None:
      if data == self.head.data: 
        self.data = self.head.next_node

      else: 
        self.head.remove(data, self.head)
    else:
      return
