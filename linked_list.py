#!/usr/bin/python3

from LinkedList.LinkedList import LinkedList

linked_list = LinkedList()

linked_list.insert_start(23)
linked_list.insert_start(33)
linked_list.insert_start(36)

linked_list.traverse()

print('\n\n ==== ')
linked_list.remove(23)
print(linked_list.size())
linked_list.traverse()

print('\n\n ==== ')
linked_list.insert_start('mbido')
linked_list.insert_end('nkwusi')


linked_list.traverse()
print(linked_list.size())