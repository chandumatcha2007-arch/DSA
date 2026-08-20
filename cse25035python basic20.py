def insert_index(self,index,data):
    if index==0:
        self.insert_began(data)
        return
    elif index > self.count()or index<0:
        printf("invalid index")
        return
    new=node(data)
    temp=self.head
    for i in range(index-1):
        temp=temp.next
    new.next=temp.next
    temp.next=new
