def count(self):
    if self .head is none:
        print("no linked list")
    else:
        c=0
        temp=self.head
        while temp:
            c+=1
            temp=temp.next
        print(f"number of nodes={c}")
