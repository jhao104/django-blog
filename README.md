## Django搭建博客
使用Django快速搭建博客
### 要求
* Python: 2.X
* Django: 1.8.2
* Mysql

### 示例博客：<http://pyspider.site:8000/>（国外服务器，较慢）
### 特点
* 博客文章 markdown 渲染，代码高亮
* 多说评论支持
* 页面特效

### 下载
```
wget https://github.com/jhao104/django-blog/archive/master.zip
or
git clone git@github.com:jhao104/django-blog.git
```
### 安装
```
pip install -r requirements.txt  #安装所有依赖
setting.py配置自己的数据库和多说
python manage.py migrate
python manage.py runserver
```
浏览器中打开<http://127.0.0.1:8000/>即可访问