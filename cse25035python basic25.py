def dequeue(self):
    if self.front==-1 or self.front >self.rear:
        print("Queue underflow")
    else:
        x=self.queue[self.front]
        self.queue[self.front]=None
        self.front+=1
        print(f"{x} deleted from the queue")

        #Reset queue when it become empty
        if self.front>self.rear:
            self.front=-1
            self.rear=-1

def peek(self):
    if self.front==-1:
        print("Queue is empty")
    else:
        print("Front element:",self.queue[self.front])

    def display(self):
        if self.front==-1:
            print("Queue is empty")
        else:
            print("the elements of the queue are:")
            for i in range(self.front,self.rear + 1):
                print(self.queue[i])
