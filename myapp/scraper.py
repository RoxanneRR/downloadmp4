# myprojecr2.0\myapp\scraper
import subprocess
import os

import re


def extract_filename(output):
    # 定义正则表达式来匹配文件路径部分
    pattern = r'Destination:\s+(.+\.mp4)'

    # 使用 re 模块中的 search 函数来查找匹配的部分
    match = re.search(pattern, output)

    # 如果找到匹配的部分，则返回文件路径，否则返回 None
    if match:
        filepath = match.group(1)
        return filepath
    else:
        return None


def extract_video_filename(full_path):
    # 使用 os.path 模块获取文件名
    filename = os.path.basename(full_path)
    print(filename)
    return filename


def download_video(url):
    # 获取当前脚本文件的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 获取当前目录的父目录
    parent_dir = os.path.dirname(current_dir)

    # 构建downloads目录的路径，使其位于当前目录的上一级
    download_dir = os.path.join(parent_dir, 'downloads')

    # 创建downloads目录，如果它不存在
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    # 尝试使用yt-dlp下载视频
    # yt_dlp_command = ['yt-dlp', url]
    yt_dlp_command = ['yt-dlp', '-o', os.path.join(download_dir, '%(title)s.%(ext)s'), url]
    try:
        result = subprocess.run(yt_dlp_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,
                                check=True)
        output = result.stdout.strip()
        print(output)
        output_filename = extract_filename(output)
        print(output_filename)
        print(2222)
        video_filename = extract_video_filename(output_filename)
        print(video_filename)
        if result.stderr:
            return f"Error with yt-dlp: {result.stderr}"
        return '下载成功 : ' + video_filename, video_filename
    except subprocess.CalledProcessError as e:
        # yt-dlp下载失败，尝试使用youtube-dl
        print('yt-dlp下载失败，尝试使用youtube-dl...')
        youtube_dl_command = ['youtube-dl', url]
        try:
            result = subprocess.run(youtube_dl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    universal_newlines=True, check=True)
            if result.stderr:
                return f"Error with youtube-dl: {result.stderr}"
            return f'下载成功!'
        except subprocess.CalledProcessError as e:
            return f'下载失败: {e.stderr}', 1
    except Exception as e:  # 捕获其他所有异常
        return f'未知错误: {str(e)}', 1


