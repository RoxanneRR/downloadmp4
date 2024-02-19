import os


def delete_files_in_downloads_folder():
    # 指定 Downloads 文件夹路径
    downloads_folder = 'downloads'

    # 检查 Downloads 文件夹是否存在
    if not os.path.exists(downloads_folder):
        print("Downloads 文件夹不存在。")
        return

    try:
        # 获取 Downloads 文件夹下的所有文件和文件夹列表
        files_in_downloads = os.listdir(downloads_folder)

        # 遍历文件列表，删除每个文件
        for file in files_in_downloads:
            file_path = os.path.join(downloads_folder, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

        print("Downloads 文件夹下的所有文件已成功删除。")
    except Exception as e:
        print("删除文件时出现错误：", e)
