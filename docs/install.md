## 安装文档

### 源码安装

* 下载代码

```shell script
git clone https://github.com/jhao104/django-blog.git
```

* 安装依赖

```shell script
pip install -r requirements.txt
```

* 配置

    * 修改数据库配置

```shell script

django_blog.settings.py
```

   * 配置畅言(评论需要)

登录畅言http://changyan.kuaizhan.com/, 注册你的站点并配置完毕,
修改 `templates/blog/component/changyan.html` 内容，替换在畅言中生成的js。
畅言js位置: 畅言管理后台-》安装畅言-》通用代码安装-》自适应安装代码, 替换现有代码

* 初始化

```shell script
python manage.py makemigrations blog
python manage.py migrate
```

* 启动

```shell script
python manage.py runserver
```

生产部署和一般Django应用无异,可自行搜索。

 