# myapp/views.py
from django.shortcuts import render
from .scraper import download_video  # 确保从scraper.py导入download_video函数

def index(request):
    download_message = ''
    if request.method == 'POST':
        video_url = request.POST.get('video_url', '')
        # 调用download_video函数，并将结果存储在download_message变量中
        download_message = download_video(video_url)
    return render(request, 'myapp/index.html', {'download_message': download_message})