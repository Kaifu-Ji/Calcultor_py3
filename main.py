# coding:utf8
# author: Kaifu Ji
# date : 20/03/17
# describe: This program is a calculator
#           use as python3 main.py "your expression(for example 1 + 2 * 3 / (2 ^ 7))"
#           return the value of this expression support "+ - / * ^ () number and minus number"
#           return FORMAT ERROR when expression is invalid
#           return VALUE ERROR when /0 happened
#           return INPUT ERROR when unsupported character

import sys


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def toArray(self):
        return self.items

def operator_compare(x,y):
    operator = {
        None: -5,
        '(': -1,
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1,
        '^': 2
    }
    return operator.get(x) - operator.get(y)


def remove_space(s: str) -> list:
    arr = []
    for i in s:
        if i is not ' ':
            arr.append(i)
    new_arr = []
    temp = ''
    op = {'+', '-', '*', '/', '^', '(', ')'}
    canMinus = False
    for item in arr:
        if canMinus and item == '-':
            temp += item
            canMinus = False
            continue
        if ('0' <= item <= '9') or item == '.':
            temp += item
            canMinus = False
        else:
            if item not in op:
                return "INPUT ERROR"
            if temp is not '':
                try:
                    new_arr.append(float(temp))
                except:
                    return "FORMAT ERROR"
                temp = ''
            new_arr.append(item)
            canMinus = True
    if temp is not '':
        new_arr.append(float(temp))
    return new_arr


def calculate(s):
    arr = remove_space(s)
    if type(arr) is str:
        return arr
    s1 = Stack()
    s2 = Stack()
    for item in arr:
        if type(item) is float:
            s1.push(item)
        else:
            if item == '(':
                s2.push(item)
            elif item == ')':
                while(1):
                    op = s2.pop()
                    if op == '(':
                        break
                    s1.push(op)
                    if op is None:
                        return "FORMAT ERROR"
            else:
                while(1):
                    if operator_compare(item,s2.peek()) >= 0:
                        s2.push(item)
                        break
                    else:
                        op = s2.pop()
                        s1.push(op)
    while (not s2.isEmpty()):
        op = s2.pop()
        if op == '(':
            return "FORMAT ERROR"
        else:
            s1.push(op)
    s3 = Stack()
    reverseNotation = s1.toArray()
    for item in reverseNotation:
        if type(item) is float:
            s3.push(item)
        else:
            if s3.size() < 2:
                return "FORMAT ERROR"
            else:
                op2 = s3.pop()
                op1 = s3.pop()
                result = None
                if item == '+':
                    result = op1 + op2
                elif item == '-':
                    result = op1 - op2
                elif item == '*':
                    result = op1 * op2
                elif item == '/':
                    if op2 == 0:
                        return 'VALUE ERROR'
                    else:
                        result = op1 / op2
                elif item == '^':
                    result = op1 ** op2
                s3.push(result)
    if s3.size() > 1:
        return "FORMAT ERROR"
    else:
        result_str = str(s3.pop())
        index = result_str.find('.')
        if result_str[0] == '-':
            if result_str[1] == '0':
                index = 0
            else:
                index -= 1
        elif result_str[0] == '0':
            index -= 1
        return round(float(result_str),10 -index)

def main():
    print(calculate(sys.argv[1]))

if __name__ == '__main__':
    main()
