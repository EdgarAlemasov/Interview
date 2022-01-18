class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack == '':
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
        if len(string) % 2 == 1:
            return print('Несбалансированно')
        items = set('({[')
        match = {('{', '}'), ('(', ')'), ('[', ']')}
        for item in string:
            if item in items:
                stack.push(item)
            else:
                if stack.size() == 0:
                    return print('Несбалансированно')
                delete_item = stack.pop()
                if (delete_item, item) not in match:
                    return print('Несбалансированно')
        if stack.size() == 0:
            return print('Сбалансированно')


string = '[([])((([[[]]])))]{()}'
string2 = '[[{())}]'
string3 = '))(('

stack = Stack()
stack.balanceString(string)
stack.balanceString(string2)
stack.balanceString(string3)


