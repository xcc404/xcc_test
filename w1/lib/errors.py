# 时间: 2026/10/21 16:14
import functools


class BaseError(Exception):
    """所有业务异常的基类。"""
    pass


class EnvError(BaseError):
    """环境相关的异常基类（如配置缺失、环境不可用等）。"""
    pass


class DataError(BaseError):
    """数据相关的异常基类（如测试数据缺失等）。"""
    pass


class ApiError(BaseError):
    """接口相关的异常基类（如接口响应错误等）。"""
    pass


class ConfigNotFoundError(EnvError):
    """
       配置文件未找到异常。

       Attributes:
           msg (str): 错误提示信息。
           cfg (str): 预期的配置文件名称或标识。
       """

    def __init__(self, msg, cfg='xxx'):
        """
        初始化配置未找到异常。

        Args:
            msg (str): 错误提示信息。
            cfg (str, optional): 预期的配置文件名称，默认为 'xxx'。
        """
        super().__init__(msg)
        self.msg = msg
        self.cfg = cfg

    def __str__(self):
        """
        返回异常的字符串表示形式。

        Returns:
            str: 包含异常类名、错误信息和配置标识的格式化字符串。
        """
        return f'{type(self).__name__}: {self.msg} | valid congid: {self.cfg}'


class EnvUnavailableError(EnvError):
    """测试环境不可用异常。"""
    pass


class EnvVarMissingError(EnvError):
    """环境变量缺失异常。"""
    pass


class TestDataNotFoundError(DataError):
    """测试数据未找到异常。"""
    pass


class ApiResponseError(ApiError):
    """API 响应异常。"""
    pass


def error_capture(func):
    """
    统一异常捕获与包装装饰器。

    捕获被装饰函数抛出的业务异常，并将其统一包装为 RuntimeError 抛出。
    同时通过 `from e` 保留原始异常的因果链，方便后续排查。

    Args:
        func (Callable): 被装饰的原始函数。

    Returns:
        Callable: 包装后的内部函数 wrapper。

    Raises:
        RuntimeError: 当捕获到 ConfigNotFoundError 时，抛出带有“配置错误”前缀的 RuntimeError。
        RuntimeError: 当捕获到其他 BaseError 子类时，抛出带有“业务执行失败”前缀的 RuntimeError。
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ConfigNotFoundError as e:
            raise RuntimeError(f"配置错误：{e}") from e
        except BaseError as e:
            raise RuntimeError(f"业务执行失败，请检查配置！底层原因：{e}") from e

    return wrapper


@error_capture
def test_func():
    """
    测试异常捕获装饰器的函数。

    抛出一个测试环境不可用的异常，以验证装饰器的捕获与包装逻辑。

    Raises:
        EnvUnavailableError: 测试环境不可用异常。
    """
    # raise ConfigNotFoundError("配置文件丢了！")
    raise EnvUnavailableError("测试环境不可用！")


if __name__ == '__main__':
    test_func()
