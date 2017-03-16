# -*- coding: utf-8 -*-


# 对比一下threading和gevent的差异

from gevent import monkey;

monkey.patch_all()
import gevent
import requests
import time
import threading


class MyTeam(threading.Thread):
    def __init__(self, user_id):
        threading.Thread.__init__(self)
        self.user_id = user_id

    def run(self):
        while urls:
            url = urls.pop(0)
            # print('%s:GET: %s' % (self.user_id, url))
            req = requests.get(url)
            data = req.content
            # print('%s:%d bytes received from %s.' % (self.user_id, len(data), url))


def use_threading():
    start_time = time.time()
    my_team = []
    for i in xrange(10):
        my_team.append(MyTeam(i))
    for one in my_team:
        one.start()
    for one in my_team:
        one.join()
    end_time = time.time()
    ues_time = end_time - start_time
    print('threading game over,use:%ss' % (ues_time))
    return ues_time


def use_gevent():
    urls = ['https://www.baidu.com/', 'https://www.sohu.com/', 'http://www.163.com/', 'http://www.qq.com/']
    start_time = time.time()
    my_team = []
    if urls:
        for i in range(len(urls)):
            my_team.append(gevent.spawn(deal_run, urls.pop(0), i))
        gevent.joinall(my_team)
    end_time = time.time()
    ues_time = end_time - start_time
    print('gevent game over,use:%ss' % (ues_time))
    return ues_time


def deal_run(url, id):
    # print('%s:GET: %s' % (id, url))
    req = requests.get(url)
    data = req.content
    # print('%s:%d bytes received from %s.' % (id, len(data), url))


if __name__ == "__main__":
    n = 10
    t = 0
    g = 0
    while 1:
        urls = ['https://www.baidu.com/', 'https://www.sohu.com/', 'http://www.163.com/', 'http://www.qq.com/']
        if n == 0:
            break
        time_1 = use_threading()
        time.sleep(5)
        time_2 = use_gevent()
        if time_1 > time_2:
            print('gevent good!')
            g += 1
        elif time_1 < time_2:
            print('threading good!')
            t += 1
        else:
            print('no!')
        n = n - 1
    print('t:g')
    print('%s:%s' % (t, g))
