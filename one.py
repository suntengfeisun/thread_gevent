# -*- coding: utf-8 -*-

# threading的使用方法
# 乱序输出
import threading

numbers = [x for x in xrange(100)]


class MyTeam(threading.Thread):
    def __init__(self, user_id):
        threading.Thread.__init__(self)
        self.user_id = user_id

    def run(self):
        while numbers:
            print ('"id:%s,use:%s"' % (self.user_id, numbers.pop(0)))


if __name__ == "__main__":
    my_team = []
    for i in xrange(10):
        my_team.append(MyTeam(i))
    for one in my_team:
        one.start()
