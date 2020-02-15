# coding=utf-8
"""
问题：使用python实现单例模式
方法1:使用模块实现单例模式

Python 的模块就是天然的单例模式，
模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象。
"""

from question_2_1_module import singleton

if __name__ == '__main__':
    obj1=singleton
    obj2=singleton
    print(obj1 is obj2)