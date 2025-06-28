#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试文件计数器功能
"""

import os
import tempfile
import shutil
from pathlib import Path
from filecounter import count_files


def create_test_directory():
    """创建测试目录结构"""
    # 创建临时目录
    temp_dir = tempfile.mkdtemp()
    test_dir = Path(temp_dir) / "test_project"
    test_dir.mkdir()
    
    # 创建文件
    (test_dir / "file1.txt").touch()
    (test_dir / "file2.py").touch()
    (test_dir / "file3.md").touch()
    
    # 创建子目录
    subdir1 = test_dir / "subdir1"
    subdir1.mkdir()
    (subdir1 / "subfile1.txt").touch()
    (subdir1 / "subfile2.py").touch()
    
    # 创建更深层的子目录
    subdir2 = subdir1 / "subdir2"
    subdir2.mkdir()
    (subdir2 / "deepfile.txt").touch()
    
    # 创建另一个子目录
    subdir3 = test_dir / "subdir3"
    subdir3.mkdir()
    (subdir3 / "another_file.txt").touch()
    
    return test_dir


def test_filecounter():
    """测试文件计数器功能"""
    print("开始测试文件计数器...")
    
    # 创建测试目录
    test_dir = create_test_directory()
    print(f"创建测试目录：{test_dir}")
    
    try:
        # 测试非递归模式
        print("\n=== 测试非递归模式 ===")
        count = count_files(str(test_dir), recursive=False)
        print(f"非递归统计结果：{count} 个文件")
        expected_count = 3  # file1.txt, file2.py, file3.md
        assert count == expected_count, f"期望 {expected_count}，实际 {count}"
        print("✓ 非递归模式测试通过")
        
        # 测试递归模式
        print("\n=== 测试递归模式 ===")
        count = count_files(str(test_dir), recursive=True)
        print(f"递归统计结果：{count} 个文件")
        expected_count = 7  # 3个根目录文件 + 2个subdir1文件 + 1个subdir2文件 + 1个subdir3文件
        assert count == expected_count, f"期望 {expected_count}，实际 {count}"
        print("✓ 递归模式测试通过")
        
        # 测试不存在的目录
        print("\n=== 测试错误处理 ===")
        count = count_files("/nonexistent/directory", recursive=False)
        assert count == -1, "应该返回错误码 -1"
        print("✓ 错误处理测试通过")
        
        print("\n🎉 所有测试通过！")
        
    finally:
        # 清理测试目录
        shutil.rmtree(test_dir.parent)
        print(f"清理测试目录：{test_dir}")


if __name__ == "__main__":
    test_filecounter() 