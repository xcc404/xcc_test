# 时间: 2026/10/18  19:15
import sys


def test_env_ok():
    assert sys.version_info[:2] == (3, 11)


# print(r'"t')
#
# print('''line1
# line2
# line3''')
#
# print("""line1
# line2
# line3""")
#
# s1 = 72
# s2 = 85
# r = s1 - s2
# print(f'{r:.1f}%')
#
# args = ['gcc', 'hello.c', 'world.c']
# match args:
#     # 如果仅出现gcc，报错:
#     case ['gcc']:
#         print('gcc: missing source file(s).')
#     # 出现gcc，且至少指定了一个文件:
#     case ['gcc', file1, *files]:
#         print('gcc compile: ' + file1 + ', ' + ', '.join(files))
#     # 仅出现clean:
#     case ['clean']:
#         print('clean')
#     case _:
#         print('invalid command.')
#
# age = 6
# match age:
#     case x if x < 10:
#         print(f'< 10 years old: {x}')
#     case 10:
#         print('10 years old.')
#     case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
#         print('11~18 years old.')
#     case 19:
#         print('19 years old.')
#     case _:
#         print('not sure.')
#
# print(hex(2002))
#
#
# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
#
#
# enroll('Adam', 'M', city='Tianjin')
#
#
# def show_args_kwargs(*args, **kwargs):
#     print(args, kwargs)
#
#
# show_args_kwargs()
#
#
# def mul(x, *y):
#     result = x
#     for i in y:
#         result *= i
#     return result
#
#
# # 测试
# print('mul(5) =', mul(5))
# print('mul(5, 6) =', mul(5, 6))
# print('mul(5, 6, 7) =', mul(5, 6, 7))
# print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
# if mul(5) != 5:
#     print('mul(5)测试失败!')
# elif mul(5, 6) != 30:
#     print('mul(5, 6)测试失败!')
# elif mul(5, 6, 7) != 210:
#     print('mul(5, 6, 7)测试失败!')
# elif mul(5, 6, 7, 9) != 1890:
#     print('mul(5, 6, 7, 9)测试失败!')
# else:
#     try:
#         mul()
#         print('mul()测试失败!')
#     except TypeError:
#         print('测试成功!')
#
#
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n - 1, a, c, b)
#         print(a, '-->', c)
#         move(n - 1, b, a, c)
#
#
# # 期待输出:
# # A --> C
# # A --> B
# # C --> B
# # A --> C
# # B --> A
# # B --> C
# # A --> C
# move(4, 'A', 'B', 'C')
#
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[:-2])
#
#
# def findMinAndMax(L):
#     if not L:
#         return (None, None)
#     mx = mn = L[0]
#     for i in L:
#         if i > mx:
#             mx = i
#         elif i < mn:
#             mn = i
#     return (mn, mx)
#
#
# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# for n in fib(6):
#     print(n)
#
#
# def triangles():
#     row = [1]
#     while True:
#         yield row
#         row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
#
#
# # 期待输出:
# # [1]
# # [1, 1]
# # [1, 2, 1]
# # [1, 3, 3, 1]
# # [1, 4, 6, 4, 1]
# # [1, 5, 10, 10, 5, 1]
# # [1, 6, 15, 20, 15, 6, 1]
# # [1, 7, 21, 35, 35, 21, 7, 1]
# # [1, 8, 28, 56, 70, 56, 28, 8, 1]
# # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
#
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# def add(x, y, f):
#     return f(x) + f(y)
#
#
# print(add(-5, 6, abs))

# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
#
#
# print(list(map(char2num, '13579')))


# from functools import reduce
#
#
# def prod(L):
#     return reduce(lambda x, y: x * y, L)
#
#
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# t = '0.456'
# print(float(t))
# print(type(float(t)))

# def createCounter():
#     x = 0
#     def counter():
#         nonlocal x
#         x += 1
#         return x
#
#     return counter
#
#
# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# import functools
#
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"正在执行: {func.__name__}...")
#         return func(*args, **kwargs)  # 执行原函数
#
#     return wrapper
#
#
# @log
# def add(a, b):
#     return a + b
#
#
# print(add(1, 2))
# print(add.__name__)

# import time, functools
#
#
# def metric(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         elapsed_ms = round((end_time - start_time) * 1000, 2)
#         print(f"{func.__name__} executed in {elapsed_ms} ms")
#         return result
#     return wrapper
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y


# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
# else:
#     print(True)


# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count += 1
#
#
# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

# 时间: 2026/10/21 16:14

# from functools import reduce
#
#
# def str2num(s):
#     # return int(s)
#     try:
#         return int(s)
#     except ValueError:
#         return float(s)
#
#
# def calc(exp):
#     ss = exp.split('+')
#     print(ss)
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
#
# main()

from abc import ABC, abstractmethod


class BaseApi(ABC):  # 1. 继承 ABC
    count = 0

    @abstractmethod  # 2. 标记为抽象方法
    def info(self):
        pass


BaseApi()
