contacts={}
while True:
    print("\n1.ADD CONTACT ")
    print("\n2.VIEW ALL")
    print("\n3.SEARCH")
    print("\n4.DELETE")
    print("\n6.EXIT")
    choice=input("Enter Choice").strip()
    if choice=='1':
        name=input("Name :")
        phone=input("Phone : ")
        contacts[name]=phone
        print("Contact Saved!") 
    elif choice=='2':
        for name,phone in contacts.items():
            print(f"{name}:{phone}")
    elif choice=='3':
        name=input("Enter the Name:")
        if name in contacts:
            print(f"{name}'s phone:{contacts[name]}")
        else:
            print("contact is not found")
    elif choice=='4':
        name=input("Enter the Name to delete:")
        if name in contacts:
            del contacts[name]
            print("Deleted successfully")
        else:
            print("no such contact.")
    elif choice == '6':  # Fixed this line
        print("Exiting contact manager.")
        break

    else:
        print("Invalid Contact")

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()      # Dummy head of the returning list
        current = dummy
        carry = 0

        # Loop until both lists are exhausted and no carry remains
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # value from l1 node or 0 if None
            val2 = l2.val if l2 else 0  # value from l2 node or 0 if None

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
