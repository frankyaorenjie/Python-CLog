__author__ = 'baniu.yao'

from CLog import CLog

class FooClass(object):

    def foo(self):
        log = CLog()
        log.write('hello world')

if __name__ == '__main__':
    fc = FooClass()
    fc.foo()
