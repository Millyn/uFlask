#uFlask
---

免去配置, 直接使用, 多实例, 异步(不是很了解)

使用*uWsgi*, *Nginx* , *Python3*, *SQLALCHEMY*, *Gevent*

---

1. 首先创建本项目虚拟环境*virtualenv -p /usr/bin/python3 py3env&
2. 进入本项目的虚拟环境*source py3env/bin/activate*
3. 安装所需库*pip install -r requirements.txt*
4. 拷贝Nginx配置*sudo cp configure/nginx.conf /etc/nginx/conf.d/flask.conf*
5. 修改flask.conf内文件夹路径*sudo vim /etc/nginx/conf.d/flask.conf*
6. 重启nginx*service nginx restart*
7. 运行uwsgi*uwsgi configure/uwsgi.ini, uwsgi configure/uwsgi_2.ini* 同时运行2个Flask实例均衡负载.
8. 访问127.0.0.1:8001/example
PS. 终端运行uwsgi 是不会保留进程的, 你关掉终端进程即会结束并清楚.所以建议使用一些守护进程的工具来保持进程的运行.
---

变得容易.