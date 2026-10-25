# 时间: 2026/10/19 17:50
class User:
    """
    用户类，用于表示系统中的用户信息。

    Attributes:
        count (int): 类属性，记录创建的 User 实例总数。
        type (str): 类属性，表示用户类型（默认 normal）。
    """
    count = 0
    type = 'normal'

    def __init__(self, name, gender, idc):
        """
        初始化 User 实例。

        Args:
            name (str): 用户名。
            gender (str): 性别（存为受保护属性 _gender）。
            idc (str): 身份码（存为私有属性 __idc）。
        """
        self.name = name
        self._gender = gender
        self.__idc = idc
        User.count += 1

    def __str__(self):
        return f'User名称：{self.name}'

    def __repr__(self):
        return f'User(name={self.name!r})'

    def _encrypt(self):
        """
        内部加密/拼接方法（受保护方法，仅限类内部使用）。

        将用户的 name、idc、gender 拼装成特定格式的字符串。

        Returns:
            str: 拼接后的数据字符串。
        """
        return '000-' + self.name + '-111-' + self.__idc + '-222-' + self._gender

    def post(self):
        """
        提交用户数据。

        调用内部 _encrypt 方法获取加密数据，并打印提交状态。
        """
        data = self._encrypt()
        print(data)
        print('已提交')


if __name__ == '__main__':
    print(User.count)
    u = User('song', 'male', '440xxxxxxxxxxxxxxx')
    print(User.count)
    u2 = User('bing', 'female', '440xxxxxxxxxxxxxxx')
    print(User.count)

    u.type = 'vip'
    print(u.type, u2.type, User.type)

    print(u)
    print([u])
    u.post()
