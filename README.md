python-chain-log
================

When I print log in python, what made me confused is that 'What this line of log comes from'. I think this is the circumstance almost every pythoner has encountered. If there is a way of logging, which can print the full stack of call-chain, it must be great. For this purpose, I write this small but userful module for python. I call this CLog which means Chain-Log.

What CLog do?
----------------

When you use CLog to print log, you can get the caller chain where you print log, such as 'Foo() --> foo1(name)'. How Clog does that? I use inspect module contained in Python 2.7 to get the complete frame in python run-time environment. A frame, briefly explained, is a collection of some piece of code. The details of frame are not going to be introduced here and you can find those in some articles describes the internal mechanism of Python.

How to use CLog
----------------

Since CLog is closely attached in Python internals, you just need to import this module and initialize it with a file name. And while you would like to print log, just use a 'write' method of instance. Let us see example.py.


class FooClass(object):

    def foo(self, text):
        log = CLog()
        log.write('hello world')

if __name__ == '__main__':
    fc = FooClass()
    fc.foo('def')

While you run python example.py, you will get 'test.log' in your PWD and its content is like:
2014-03-30 19:09:35,582 [example.py:FooClass() --> example.py:foo('def')] hello world

It is really cool. In log file, there is file name, class name, function name and its parameters. Every body is clearly where this log comes from and I think this will help pythoner a lot.

Why only 'write' method?
----------------------

There is only one method for writng logs, and no log level concept is available in CLog. Because I think it is not neccessary for this. A 'write' method is enough.

TODO
----------------------

Add option to use sysout for output logs. Currently, CLog only supports print logs to file.
