# -*- coding: utf-8 -*-

# gevent的使用方法
# 乱序输出,但这个例子并没有网络阻塞,并没有体现出协程
import gevent
# from gevent.threadpool import ThreadPool
from gevent import monkey

monkey.patch_all()
numbers = [x for x in xrange(100)]


def deal_run(id):
    while numbers:
        print ('"id:%s,use:%s"' % (id, numbers.pop(0)))


if __name__ == "__main__":
    my_team = []
    for i in xrange(10):
        my_team.append(gevent.spawn(deal_run, i))
    gevent.joinall(my_team)
    print('game over')
