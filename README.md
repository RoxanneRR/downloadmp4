### 功能

Django项目，调用yl-dl模块下载视频，目前可用
* YouTube
* 哔哩哔哩
* 搜狐视频
* TikTok（不是抖音）

### 环境

* Python3.8以上
* 安装[FFmpeg](https://ffmpeg.org//)，路径写入环境变量
* Python模块Django  youtube-dl  yt-dlp

### 运行
* 安装依赖项（可选）
```
pip install -r requirements.txt
```
* 运行
```
python manage.py runserver
```
### 使用

* 进入网页输入链接点击下载即可。
* 目前对```https://b23.tv/```开头的短链接解析不好，建议还原为如```https://www.bilibili.com```样式的长链接后再输入。
* 如无法下载，推荐使用Chrome浏览器、Edge浏览器、Firefox浏览器下载。
* 如无法播放，推荐使用PotPlayer等解码功能较强的播放器。
* 如遇Django跨域问题，可修改```CSRF_TRUSTED_ORIGINS=["https://xxxx.com","http://xxxx.com"]```为部署的域名。

### 示例

[示例网站](http://dl.wenruxiaow.link)
