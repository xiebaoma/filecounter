# filecounter

这个工具可以查看一个文件夹下下有多少文件

一个文件夹下可能有文件和文件夹。

这个程序可以只统计文件数有多少个。

## 功能特点

- 统计指定目录下的文件数量（不包括文件夹）
- 支持递归统计子目录中的文件
- 支持命令行参数
- 错误处理和权限检查
- 支持详细输出模式

## 安装

1. 确保你的系统已安装Python 3.6或更高版本
2. 克隆或下载此项目
3. 无需安装额外依赖（只使用Python标准库）

## 使用方法

### 基本用法

```bash
# 统计当前目录下的文件数（不包括子目录）
python filecounter.py

# 统计指定目录下的文件数（不包括子目录）
python filecounter.py /path/to/directory

# 递归统计当前目录及子目录下的文件数
python filecounter.py -r

# 递归统计指定目录及子目录下的文件数
python filecounter.py /path/to/directory -r
```

### 高级用法

```bash
# 显示详细信息
python filecounter.py -v

# 递归统计并显示详细信息
python filecounter.py -r -v

# 统计指定目录并显示详细信息
python filecounter.py /path/to/directory -v

# 递归统计指定目录并显示详细信息
python filecounter.py /path/to/directory -r -v

# 查看帮助信息
python filecounter.py -h
```

### 示例

```bash
# 统计当前目录（不包括子目录）
$ python filecounter.py
3

# 递归统计当前目录（包括子目录）
$ python filecounter.py -r
15

# 统计当前目录（详细模式，不包括子目录）
$ python filecounter.py -v
正在仅统计当前目录：C:\Users\username\Desktop\myfile\filecounter
目录 'C:\Users\username\Desktop\myfile\filecounter' 中共有 3 个文件（仅当前目录）

# 递归统计当前目录（详细模式，包括子目录）
$ python filecounter.py -r -v
正在递归统计目录：C:\Users\username\Desktop\myfile\filecounter
目录 'C:\Users\username\Desktop\myfile\filecounter' 中共有 15 个文件（包括子目录）

# 统计其他目录
$ python filecounter.py C:\Users\username\Documents
25

# 递归统计其他目录
$ python filecounter.py C:\Users\username\Documents -r
150
```

## 参数说明

- `directory`: 要统计的目录路径（可选，默认为当前目录）
- `-r, --recursive`: 递归统计子目录中的文件
- `-v, --verbose`: 显示详细信息
- `-h, --help`: 显示帮助信息

## 输出说明

- 默认模式：只输出文件数量
- 详细模式（-v）：显示统计的目录路径、文件数量和统计模式
- 错误情况：显示错误信息并返回非零退出码

## 统计模式

- **非递归模式**（默认）：只统计指定目录下的文件，不包括子目录中的文件
- **递归模式**（-r）：统计指定目录及其所有子目录中的文件

## 错误处理

程序会处理以下错误情况：
- 目录不存在
- 路径不是目录
- 权限不足
- 其他系统错误

## 系统要求

- Python 3.6+
- 支持的操作系统：Windows, macOS, Linux
