from collections import deque
import copy

class Painting:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

p1 = Painting("Starry Night", "Vincent van Gogh", 1889)
p2 = Painting("Mona Lisa", "Leonardo da Vinci", 1503)
p3 = Painting("The Persistence of Memory", "Salvador Dalí", 1931)


class Stack(deque):
    
    def push(self, item):
        self.append(item)

    def pop(self):
        popped = self[-1]
        del self[-1]
        return popped

    def peek(self):
        return self[-1]

    def size(self):
        return len(self)

    def is_empty(self):
        return len(self) == 0

paint = Stack()
paint.push(p1)
paint.push(p2)
paint.push(p3)


def fpby(stack, limit):
    copy_past = stack.copy()
    res = Stack()
    while not copy_past.is_empty():
        item = copy_past.pop()
        if item.year > limit:
            res.append(item)
            print("+1") # debug-строка
    return res


fpby(paint, 1888)