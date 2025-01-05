import os

def create_folders(start, end):
    """
    在当前目录下生成从 start 到 end 的文件夹
    :param start: 起始编号
    :param end: 结束编号
    """
    if start > end:
        print("起始编号不能大于结束编号！")
        return

    for folder_name in range(start, end + 1):
        folder_path = os.path.join(".", str(folder_name))
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"文件夹 '{folder_name}' 创建成功！")
        else:
            print(f"文件夹 '{folder_name}' 已存在！")

if __name__ == "__main__":
    # 生成从 1919 到 2053 的文件夹
    create_folders(1919, 2053)
