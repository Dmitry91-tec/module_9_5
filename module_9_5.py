class StepValueError(ValueError):
    pass

class Iterator:

    pointer = int

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = self.start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        x = self.pointer
        if self.step>0 and self.pointer<=self.stop:
            self.pointer += self.step
            return x
        if self.step<0 and self.pointer>=self.stop:
            self.pointer += self.step
            return x
        raise StepValueError()

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

try:
    iter2 = Iterator(-5, 1)
    for i in iter2:
        print(i, end=' ')
except StepValueError:
    print('')

try:
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')
except StepValueError:
    print('')

try:
    iter4 = Iterator(5, 1, -1)
    for i in iter4:
        print(i, end=' ')
except StepValueError:
    print('')

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
except StepValueError:
    print('')
