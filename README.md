## Django搭建博客
使用Django快速搭建博客
### 要求
* Python: 2.X
* Django: 1.10.x
* Mysql

### 示例博客：<http://www.spiderpy.cn/blog>

### 特点

* 博客文章 markdown 渲染，代码高亮
* 三方社会化评论系统支持(网易云跟帖)
* 三种皮肤自由切换
* 阅读排行榜/最新评论
* 多目标源博文分享
* 博文归档
* 友情链接

### 下载
```
wget https://github.com/jhao104/django-blog/archive/master.zip
or
git clone git@github.com:jhao104/django-blog.git
```

### 安装
```
pip install -r requirements.txt  #安装所有依赖
setting.py配置自己的数据库
配置网易云跟帖：到https://manage.gentie.163.com/注册站点,将blog/models.py中的“http://www.spiderpy.cn”换成你注册的站点地址,将templates/message.html中的productKey换成你的APP KEY。否则无法正常显示跟帖
python manage.py makemigrations blog
python manage.py migrate
python manage.py runserver
```

浏览器中打开<http://127.0.0.1:8000/>即可访问

## 历史版本

* [黑白简约版](https://github.com/jhao104/django-blog/tree/v1.0)
