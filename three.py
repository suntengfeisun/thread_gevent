# -*- coding: utf-8 -*-


# gevent的使用方法
# 有网络请求才能体现出gevent的优势
from gevent import monkey;

monkey.patch_all()
import gevent
import requests
import time

urls = ['https://www.python.org/', 'https://www.baidu.com/', 'https://github.com/']


def deal_run(url, id):
    print('%s:GET: %s' % (id, url))
    req = requests.get(url)
    data = req.content
    print('%s:%d bytes received from %s.' % (id, len(data), url))


if __name__ == "__main__":
    start_time = time.time()
    my_team = []
    if urls:
        for i in range(3):
            my_team.append(gevent.spawn(deal_run,urls.pop(0), 1))
        gevent.joinall(my_team)
    end_time = time.time()
    print('game over,use:%ss' % (end_time - start_time))
