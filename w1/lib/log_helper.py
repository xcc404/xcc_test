# 时间: 2026/10/22 17:32
import logging
from logging.handlers import TimedRotatingFileHandler
import sys
import os


class MyLogger:
    """
    自定义日志管理类。
    实现控制台与文件的双重输出，支持日志文件按天滚动（保留7天），并防止日志重复记录。
    """

    def __init__(self):
        """
        初始化 Logger 对象。
        配置日志级别、输出格式、控制台打印以及文件存储（绝对路径）。
        """
        # logging.basicConfig(
        #     level=logging.INFO,
        #     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        #     filename='app.log',
        #     encoding='utf-8'
        # )
        # self.logger = logging.getLogger(__name__)
        self.logger = logging.getLogger('log_helper')
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        if not self.logger.handlers:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            log_file_path = os.path.join(base_dir, 'app.log')

            # 双输出
            console_handler = logging.StreamHandler(sys.stdout)
            file_handler = TimedRotatingFileHandler(
                filename=log_file_path,
                when='D',
                interval=1,
                backupCount=7,
                encoding='utf-8'
            )

            # 模块名 [%(name)s 记录器的名字] [%(filename)s 调用了该logger的py文件的名字]
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            file_handler.setFormatter(formatter)

            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def log_debug(self, msg):
        """
        记录 DEBUG 级别的日志。

        Args:
            msg (str): 日志信息内容。

        Returns:
            None
        """
        return self.logger.debug(msg)

    def log_info(self, msg):
        """
        记录 INFO 级别的日志。

        Args:
            msg (str): 日志信息内容。

        Returns:
            None
        """
        return self.logger.info(msg)


if __name__ == '__main__':
    ml = MyLogger()
    print(ml.logger)
    ml.logger.debug('debug')
    ml.log_info('info')
    print(ml.logger.handlers)
    print(ml.logger.propagate)
    print(logging.getLogger().handlers)
