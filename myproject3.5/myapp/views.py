# myapp/views.py
from django.shortcuts import render, redirect
from .scraper import download_video
import os
from django.http import HttpResponse
from django.utils.encoding import escape_uri_path
from django.contrib import messages

bilibili_url = 'https://www.bilibili.com/'
youtube_watch_url = 'https://www.youtube.com/'

tiktok_url = 'https://www.tiktok.com/'
souhu_url = 'https://tv.sohu.com/'
youtube_shorts = 'https://www.youtube.com/shorts/'


def index(request):
    download_message = ''
    output_filename = ''
    if request.method == 'POST':
        video_url = request.POST.get('video_url', '')
        video_url = video_url.strip()
        if video_url.startswith(bilibili_url) or video_url.startswith(youtube_watch_url):
            website_type = 1
        elif video_url.startswith(tiktok_url) or video_url.startswith(souhu_url):
            website_type = 2
        else:
            website_type = 1000
        print(website_type)
        if website_type == 1 or website_type == 2:
            download_message, output_filename = download_video(video_url, website_type)
            print(download_message)
            print(output_filename)
            if str(output_filename).strip() == '1':
                messages.error(request, '下载失败')
                return redirect('/')
        else:
            messages.error(request, '无法读取，请输入有效的视频链接！')
            print(messages)
            return redirect('/')
    messages.success(request, download_message)
    return render(request, 'myapp/index.html',
                  {'output_filename': output_filename})


def download(request):
    file_name = request.GET.get('file_name')
    print(111111111)
    print(file_name)
    if str(file_name).strip() == '1':
        messages.error(request, '下载失败')
        return redirect('/')
    else:
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
                    print(file.encode('utf-8').decode('utf-8'))
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
                
                messages.error(request, '文件不存在')
                return redirect('/')
