

class Stack:

    def __init__(self):
        self.list = []

    def isempty(self):
        if not self.list:
            return True
        else:
            return False

    def push(self, new_element):
        self.list.append(new_element)

    def pop(self):
        self.list.pop()
        return self.list[-1]

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)


def balance(brackets):
    if len(brackets) % 2 != 0:
        print('Несбалансировано')
    else:
        stack = Stack()
        additional = Stack()
        for bracket in brackets:
            stack.push(bracket)
        while not stack.isempty():
            while not stack.isempty() and (stack.peek() != '(' or '[' or '{'):
                additional.push(stack.peek())
                stack.pop()
            for i in range(1, additional.size()):
                if stack.peek() == additional.peek():
                    stack.pop()
                    additional.pop()
                else:
                    print('Несбалансировано')
        if stack.isempty():
            print('Сбалансировано')
        else:
            print('Несбалансировано')



balance('(((([{}]))))')