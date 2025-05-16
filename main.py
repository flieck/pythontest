# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
# 闭包比较复杂不容易理解


from Student import *
from Animal import *


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

# 函数参数是可变参数类型，计算累加和


def cal_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 内部函数()引用了lazy_sum()的参数和局部变量，当lazy_sum()返回函数sum()时，相关参数和局部变量都保存在了返回函数中，这种称为闭包（closure）的程序很有用


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum  # 返回函数

# 返回值是个列表
def count():
    fs = []
    # 每次循环输出1的平方，2的平方，3的平方，列表fs存放的数据类型是函数
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


def ff(x):
    return x*x


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2025-05-16')


def run_twice(Student111):
    Student111.run()
    Student111.run()


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    # 普通函数直接输出了结果
    print("普通函数直接输出了结果",cal_sum(1, 3, 5, 7, 9))
    print("输出闭包会发现不会输出结果，因为他的返回值是一个函数",lazy_sum(1, 3, 5, 7, 9))
    # 将函数的返回值，即一个函数赋值给了变量f
    f = lazy_sum(1, 3, 5, 7, 9)
    print(f.__class__)
    print(f())
    # 相当于函数指针类型
    print(lazy_sum(1, 3, 5, 7, 9)())
    # f1 f2相当于两个函数指针
    f1 = lazy_sum(1, 3, 5, 7, 9)
    f2 = lazy_sum(1, 3, 5, 7, 9)
    print(f1 is f2)
    f3, f4, f5 = count()# 返回的函数并没有立即执行，而是在调用了f3, f4, f5才会执行，所以每一次的执行结果都是9
    print(f3())
    print(f4())
    print(f5())

    r = map(ff, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))
    r1 = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r1))

    fff = now
    fff()
    print(now.__name__)
    print(fff.__name__)

    student1 = HHStudent('lee', 90)
    print(student1.get_grade())
    student1.print_score()
    print(student1.get_name())
    print(student1.get_score())

    student1.set_name("ma")
    student1.set_score(60)
    print(student1.get_name())
    print(student1.get_score())
    student1.run()

    student2 = Animal()

    run_twice(student1)  # student1是Animal的子类实例化而来，他执行的run方法就是重写之后的
    run_twice(student2)  # student2是Animal类实例化而来，他执行的run方法就是重写之前的

    print(dir(student1))
    print(dir(student2))

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
