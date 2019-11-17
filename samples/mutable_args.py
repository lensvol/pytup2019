import sys


def func(l=[], d={}, b=42):
    print(l)
    print(d)

    a = None


class A(object):
    def f(self, a=[42]):
        print(a)
