#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件计数器
统计指定文件夹下的文件数量（不包括文件夹）
支持递归统计子目录中的文件
"""

import os
import sys
import argparse
from pathlib import Path


def count_files(directory_path, recursive=False):
    """
    统计指定目录下的文件数量
    
    Args:
        directory_path (str): 目录路径
        recursive (bool): 是否递归统计子目录中的文件
        
    Returns:
        int: 文件数量
    """
    try:
        # 将路径转换为Path对象
        path = Path(directory_path)
        
        # 检查路径是否存在
        if not path.exists():
            print(f"错误：路径 '{directory_path}' 不存在")
            return -1
            
        # 检查是否为目录
        if not path.is_dir():
            print(f"错误：'{directory_path}' 不是一个目录")
            return -1
            
        # 统计文件数量
        file_count = 0
        
        if recursive:
            # 递归统计所有子目录中的文件
            for item in path.rglob('*'):
                if item.is_file():
                    file_count += 1
        else:
            # 只统计当前目录下的文件（不包括子目录）
            for item in path.iterdir():
                if item.is_file():
                    file_count += 1
                
        return file_count
        
    except PermissionError:
        print(f"错误：没有权限访问目录 '{directory_path}'")
        return -1
    except Exception as e:
        print(f"错误：{e}")
        return -1


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="统计指定文件夹下的文件数量（不包括文件夹）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例：
  python filecounter.py .                    # 统计当前目录下的文件数
  python filecounter.py /path/to/directory   # 统计指定目录下的文件数
  python filecounter.py . -r                 # 递归统计当前目录及子目录下的文件数
  python filecounter.py /path/to/directory -r -v  # 递归统计并显示详细信息
        """
    )
    
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="要统计的目录路径（默认为当前目录）"
    )
    
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="递归统计子目录中的文件"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="显示详细信息"
    )
    
    args = parser.parse_args()
    
    # 获取绝对路径
    directory = os.path.abspath(args.directory)
    
    if args.verbose:
        mode = "递归统计" if args.recursive else "仅统计当前目录"
        print(f"正在{mode}目录：{directory}")
    
    # 统计文件数量
    file_count = count_files(directory, args.recursive)
    
    if file_count >= 0:
        if args.verbose:
            mode_desc = "（包括子目录）" if args.recursive else "（仅当前目录）"
            print(f"目录 '{directory}' 中共有 {file_count} 个文件{mode_desc}")
        else:
            print(file_count)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main() 