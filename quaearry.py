class Quee:
    def __init__(self ):
        self.arr =[None] * 5
        self.font = 0
        self.rear = 0
        self.count =0
        self

    def insert(self , value):
        if  self.count < 5:
            self.arr[self.rear]=value
            self.rear+=1
            self.count+=1
        else:
            print("The Queae is full now")
    def top(self):
        if self.count <= 0:
            print("queee is empty")
        else:
            print(f'top value {self.arr[self.font]}')
    def pop(self):
        if self.count < 0:
            print("your quee is empty")
        else:
            print(self.arr[self.font])
            self.font+=1
            self.count -=1
q = Quee()
q.insert(5)
q.pop()
q.top()
q.insert(10)
q.top()



