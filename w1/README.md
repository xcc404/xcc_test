# W1 基础 API 测试组件 (lib 包)

这是一个封装了基础 API、配置读取、错误处理和日志模块的 Python 库。

## 📁 目录结构
- `lib/`：核心包代码
  - `base_api.py`：基础类定义
  - `config.py`：INI 配置文件读取封装
  - `errors.py`：自定义异常类
  - `log_helper.py`：日志辅助模块
  - `config_ini/`：存放配置文件
- `test_smoke.py`：冒烟测试脚本

## 🚀 快速开始

### 1. 安装依赖
无需第三方依赖，使用 Python 标准库。

### 2. 如何使用
```python
from lib.base_api import BaseApi
from lib.config import MyConfig

# 读取配置
cfg = MyConfig()
print(cfg.get('dev', 'host'))

# 实例化 API
api = BaseApi(name='xcc', idc='12345')
print(api.name)