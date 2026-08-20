def delete(self,value):
    if self.head is none:
        printf("no data to delete")
    else:
        temp=self.head
        if temp and temp.data==value:
            self.head=temp.next
            printf("value deleted")
            return
        while temp.next and temp.next.data!=value:
            temp=temp.next
        if temp.next is none:
            printf("value not present")
        else:
            temp.next=temp.next.next
            print("value deleted")
