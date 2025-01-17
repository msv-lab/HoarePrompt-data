import os
import argparse

def create_html_files(folder_name, file_count):
    """
    在指定目录下创建HTML文件
    :param folder_name: 目录名称
    :param file_count: 文件数量
    """
    # 构建目标目录路径
    target_directory = os.path.join(".", str(folder_name))

    # 确保目录存在，如果不存在则创建
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
        print(f"目录 '{target_directory}' 创建成功！")
    else:
        print(f"目录 '{target_directory}' 已存在！")

    # 创建指定数量的HTML文件
    for i in range(file_count):
        file_name = chr(65 + i) + ".html"  # 生成文件名 A.html, B.html, ...
        file_path = os.path.join(target_directory, file_name)

        # 写入简单的 HTML 模板
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"<!DOCTYPE html>\n<html>\n<head>\n<title>{file_name}</title>\n</head>\n<body>\n<h1>{file_name}</h1>\n</body>\n</html>")

        print(f"文件 '{file_name}' 创建成功！路径：{file_path}")

if __name__ == "__main__":
    # 设置命令行参数
    parser = argparse.ArgumentParser(description="在指定目录下创建HTML文件")
    parser.add_argument("folder_name", type=str, help="目录名称，例如：1919")
    parser.add_argument("file_count", type=int, help="要创建的HTML文件数量，例如：3")
    
    # 解析参数
    args = parser.parse_args()

    # 调用函数创建文件
    create_html_files(args.folder_name, args.file_count)
