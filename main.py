class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack == []:
            return True
        else:
            return False

    def push(self, string):
        for item in string:
            self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def balanceString(self, string):
        index = 0
        for item in string:
            if item == '(' or item == '{' or item == '[':
                index += 1
            elif item == ']' or '}' or ')':
                index -= 1
            if string[0] == ')' or string[0] == '}' or string[0] == ']':
                return print('Неправильная вложенность скобок!')
        if index == 0:
            return print('Сбалансированно!')
        else:
            return print('Несбалансированно!')


string = '[([])((([[[]]])))]{()}'
string2 = '[[{())}]'
string3 = '))(('

stack = Stack()
stack.push(string)
print(stack.is_empty())
print(stack.stack)
print(stack.pop())
print(stack.peek())
print(stack.stack)
print(stack.size())
stack.balanceString(string)
