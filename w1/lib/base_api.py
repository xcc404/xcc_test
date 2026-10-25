# 时间: 2026/10/20 17:24


class BaseApi:
    """
    基础API类，用于统计所有实例的数量。

    Attributes:
        count (int): 类级别的计数器，记录实例总数。
    """
    count = 0

    def __init__(self, name, idc):
        """
        初始化基础API实例。

        Args:
            name (str): 用户名。
            idc (str): 身份码（会作为私有属性保存）。
        """
        self.name = name
        self.__idc = idc
        # BaseApi.count += 1
        type(self).count += 1

    @property
    def idc(self):
        """
        获取用户的身份码（只读属性）

        Returns:
            str: 用户的身份码。
        """
        return self.__idc

    def __str__(self):
        """
        返回对象的字符串表示（面向用户）。

        Returns:
            str: 格式化后的用户名字符串。
        """
        return f'用户名：{self.name}'

    def __repr__(self):
        """
        返回对象的官方字符串表示（面向开发者，用于调试）。

        Returns:
            str: 格式化后的类名及实例属性。
        """
        return f'BaseApi(name={self.name!r})'

    def info(self):
        """打印用户的姓名和身份码信息。"""
        print(f'姓名：{self.name} | 身份码：{self.__idc}')


class Worker(BaseApi):
    """
    普通工作者类，继承自 BaseApi。
    仅作为基础子类，未做额外扩展。
    """
    pass


class Manager(Worker):
    """
    管理员类，继承自 Worker。

    Attributes:
        _gender (str): 性别（受保护的属性）。
    """

    def __init__(self, name, idc, gender):
        """
        初始化管理员实例。

        Args:
            name (str): 姓名。
            idc (str): 身份码。
            gender (str): 性别。
        """
        super().__init__(name, idc)
        self._gender = gender


class Teacher(Worker):
    """
    教师类，继承自 Worker。
    重写了 info 方法以输出任职学校。
    """

    def info(self, school='xxx'):
        """
        打印教师信息及任职学校。

        Args:
            school (str,optional): 任职学校名称，默认为 'xxx'。
        """
        super().info()
        print(f'任职于{school}')


class Student(Worker):
    """
    学生类，继承自 Worker。
    提供专属的学生信息打印方法。
    """
    def s_info(self, school):
        """
        打印学生详细信息及就读学校。

        Args:
            school (str): 就读学校名称。
        """
        print(f'姓名：{self.name} | 学号：{self.idc} | 就读于{school}')
    # def info(self, school):
    #     print(f'来自{school}')


def show(obj):
    """
    多态演示函数。接收任意对象并调用其 info 方法。

    Args:
        obj (BaseApi): 继承了 BaseApi 的实例对象。
    """
    obj.info()


if __name__ == '__main__':
    # ----继承----
    w = Worker('song', '312000xxxx')
    print(w)
    print([w])
    print(w.count)
    w.info()
    m = Manager('bing', '312000xxxx', 'male')
    print(w.count)
    print(m.count)
    t = Teacher('du', '312000xxxx')
    t.info()
    t.info('tank')
    print(w.count)
    print(m.count)
    print(t.count)
    s = Student('lin', '312000xxxx')
    s.s_info('air')
    print(w.count)
    print(m.count)
    print(t.count)
    print(s.count)
    # ----多态----
    show(w)
    show(m)
    show(t)
    show(s)
