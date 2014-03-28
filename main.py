__author__ = 'frankyao'

from Log import Log

class FooClass(object):

    def foo(self):
        log = Log()
        log.write('hello world')

if __name__ == '__main__':
    fc = FooClass()
    fc.foo()
