# 时间: 2026/10/23 23:23
# INI格式配置

import configparser
import os


class MyConfig:
    """
    配置管理类。
    负责读取基础的 INI 配置文件、根据环境加载特定的配置，并支持环境变量覆盖。
    """

    def __init__(self):
        """
        初始化配置管理器。
        读取 baseconfig.ini 和 config_{env}.ini，并根据系统环境变量动态覆盖配置。
        """
        env = os.environ.get('APP_ENV', 'dev')
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_dir = os.path.join(base_dir, 'config_ini')

        self.config = configparser.ConfigParser()

        base_ini_path = os.path.join(config_dir, 'baseconfig.ini')
        self.config.read(base_ini_path)

        env_file = os.path.join(config_dir, f'config_{env}.ini')
        if os.path.exists(env_file):
            self.config.read(env_file)

        env_db_host = os.environ.get('DB_HOST')
        if env_db_host:
            if not self.config.has_section(env):
                self.config.add_section(env)  # 如果没有，先建个空段
            self.config.set(env, 'host', env_db_host)

        # self.config['DEFAULT'] = {'port': '9999', 'timeout': '30'}
        # self.config['dev'] = {'user': 'xcc', 'host': 'localhost', 'port': 22}
        # self.config['test'] = {}
        # self.config['test']['user'] = 'test_user'
        # self.config['test']['host'] = '192.168.x.x'
        # self.config['test']['port'] = '17890'
        # self.config.add_section('prod')
        # self.config.set('prod', 'user', value='prod_user')
        # self.config.set('prod', 'host', value='172.x.x.x')
        # self.config.set('prod', 'port', value='88')
        # with open('./config_ini/baseconfig.ini', 'w', encoding='utf-8') as f:
        #     self.config.write(f)

    def sections(self):
        """
        获取配置文件中所有的段落（Section）名称。

        Returns:
            list: 包含所有段落名称的列表。
        """
        return self.config.sections()

    def items(self, section):
        """
        获取指定段落下的所有键值对。

        Args:
            section (str): 段落名称。

        Returns:
            list: 包含 (键, 值) 元组的列表。
        """
        return self.config.items(section)

    def get(self, section, key):
        """
        获取指定段落下特定键的值，如果不存在则返回提示信息。

        Args:
            section (str): 段落名称。
            key (str): 键名。

        Returns:
            str: 对应的值，如果找不到则返回 '配置不存在'。
        """
        return self.config.get(section, key, fallback='配置不存在')


if __name__ == '__main__':
    c = MyConfig()
    print(c.sections())
    print(c.items('DEFAULT'))
    print(c.items('dev'))
    print(c.get('prod', 'host'))

    c.config['dev']['user'] = 'hacker'
    b = MyConfig()
    print(b.get('dev', 'user'))
    print(c)
