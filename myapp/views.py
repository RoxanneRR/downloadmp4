# myapp/views.py
from django.shortcuts import render
from .scraper import download_video
import os
from django.http import HttpResponse
from django.utils.encoding import escape_uri_path


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


def index(request):
    delete_files_in_downloads_folder()
    download_message = ''
    output_filename = ''
    if request.method == 'POST':
        video_url = request.POST.get('video_url', '')
        # 调用download_video函数，并将结果存储在download_message变量中
        download_message, output_filename = download_video(video_url)
        print(download_message)
        print(output_filename)
    return render(request, 'myapp/index.html',
                  {'download_message': download_message, 'output_filename': output_filename})


def download(request):
    file_name = request.GET.get('file_name')
    print(111111111)
    print(file_name)
    if file_name:
        output_filename = os.path.join('downloads', file_name)
        if os.path.exists(output_filename):
            with open(output_filename, 'rb') as video_file:
                response = HttpResponse(video_file.read(), content_type='application/octet-stream')
                response[
                    'Content-Disposition'] = f'attachment; filename="{escape_uri_path(os.path.basename(output_filename))}"'
            # 先设置响应内容，然后删除源文件
            os.remove(output_filename)
            return response
        else:
            # 遍历downloads文件夹，找到名字中包含file_name的文件
            for file in os.listdir('downloads'):
                if file_name in file:
                    # 如果找到匹配的文件，返回文件路径
                    file_path = os.path.join('downloads', file)
                    with open(file_path, 'rb') as video_file:
                        response = HttpResponse(video_file.read(), content_type='application/octet-stream')
                        response[
                            'Content-Disposition'] = f'attachment; filename="{escape_uri_path(os.path.basename(file_path))}"'
                    # 先设置响应内容，然后删除源文件
                    os.remove(file_path)
                    return response

            return HttpResponse('文件不存在')
