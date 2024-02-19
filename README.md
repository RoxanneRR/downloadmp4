### 功能

Django项目，调用yl-dl模块下载视频，目前可用
* YouTube```https://www.youtube.com/``` ```https://www.youtube.com/shorts/```
* 哔哩哔哩```https://www.bilibili.com/```
* 搜狐视频```https://tv.sohu.com/```
* TikTok（不是抖音）```https://www.tiktok.com/```

### 环境

* Python3.8以上
* 安装[FFmpeg](https://ffmpeg.org//)，路径写入环境变量
* Python模块Django  youtube-dl  yt-dlp

### 运行
* 安装依赖项（可跳过）
```
pip install -r requirements.txt
```
* 运行
```
python manage.py runserver
```
* 如遇Django跨域问题，可修改```CSRF_TRUSTED_ORIGINS=["https://xxxx.com","http://xxxx.com"]```为部署的域名。
  
### 使用
* 进入网页输入链接点击下载即可。
* 如下载失败，请确认输入链接格式在支持范围。
* 如无法弹出下载框，推荐使用Chrome浏览器、Edge浏览器、Firefox浏览器下载。
* 如无法播放，推荐使用PotPlayer等解码功能较强的播放器。
  
### 示例
* [示例网站](http://dl.wenruxiaow.link)。
* 请不要使用代理连接示例网站。
