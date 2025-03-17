import os

def get_folder_size(folder_path):
    total_size = 0
    try:
        with os.scandir(folder_path) as it:
            for entry in it:
                if entry.is_file():
                    total_size += entry.stat().st_size  # 累加文件大小
                elif entry.is_dir():
                    # 递归计算子文件夹大小
                    total_size += get_folder_size(entry.path)
    except PermissionError:
        print(f"权限不足，无法访问文件夹: {folder_path}")
    return total_size

def convert_size_to_gb(size_in_bytes):
    return size_in_bytes / (1024 ** 3)  # 转换为GB

def list_folder_sizes(root_path):
    folder_sizes = {}
    for item in os.listdir(root_path):
        item_path = os.path.join(root_path, item)
        if os.path.isdir(item_path):
            size_in_bytes = get_folder_size(item_path)  # 计算文件夹总大小
            size_in_gb = convert_size_to_gb(size_in_bytes)
            folder_sizes[item] = size_in_gb
    return folder_sizes

if __name__ == "__main__":
    path = input("请输入要遍历的路径: ")
    if os.path.exists(path) and os.path.isdir(path):
        folder_sizes = list_folder_sizes(path)
        # 按文件夹大小从大到小排序
        sorted_folder_sizes = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)
        for folder, size in sorted_folder_sizes:
            print(f"文件夹: {folder}, 大小: {size:.2f} GB")
    else:
        print("指定的路径不存在或不是一个目录。")