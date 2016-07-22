## Basic

# 1. Write a function print_numbers(n) to print the numbers from 1 to n.

def print_numbers(n, i = 1):
    if i <= n:
        print i
        print_numbers(n, i + 1)

print_numbers(10)


# 2. Write a function say_hello(names) that takes a list of names and says hello to each name in the list (prints them out using print statement).


def say_hello(names, i = 0):
    if i < len(names):
        print 'Hello, %s' % names[i]
        say_hello(names, i + 1)

say_hello(['DeeAnn', 'Cody', 'Tim', 'Kyle', 'Anthony', 'Matthew', 'Regan'])




## Linked Lists

# 1. Write a function ll_lookup(node, target) that returns a LLNode whose data equals target. For example, given the above setup, ll_lookup(one, 3) should return the LLNode associated with 3, while ll_lookup(one, 5) should return None, and ll_lookup(three, 1) should return None.


class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "LLNode(%r)" % self.data

one = LLNode(1)
two = LLNode(2)
one.next = two
three = LLNode(3)
two.next = three
four = LLNode(4)
three.next = four

def ll_lookup(node, target):
    if node:
        if node.data == target:
            return node
        elif node.data != target:
            node = node.next
            return ll_lookup(node, target)

print ll_lookup(one, 5)
