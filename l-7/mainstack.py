class Stack:
    def __init__(self,n):
        self.stack=[]
        self.n=n#max amount of numbers

    def push(self,a):
        if len(self.stack)<self.n:
            self.stack.append(a)
        else:
            print("no,stack is feed up")

    def pop(self):
        if len(self.stack)==0:
            print("FEED STACK")
        else:
            self.stack.pop(-1)

    def how_much_stack_has_ate(self):
        print(len(self.stack))

    def what_stack_has_ate(self):
        print(self.stack)

hungry=Stack(5)
hungry.push(1)
hungry.push(3)
hungry.push(5)
hungry.push(2)
hungry.push(8)

hungry.what_stack_has_ate()

hungry.push(6)

hungry.pop()

hungry.what_stack_has_ate()


        