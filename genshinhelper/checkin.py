# checkin.py
import os
import genshinhelper as gh

cookie = os.environ.get('COOKIE')
if not cookie:
    print('请设置 COOKIE 环境变量')
    exit(1)

g = gh.Genshin(cookie)
result = g.sign()
print(result)