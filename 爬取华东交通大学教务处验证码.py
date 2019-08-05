import re  # 导入正则表达式模块
import requests  # python HTTP客户端 编写爬虫和测试服务器经常用到的模块
import random  # 随机生成一个数，范围[0,1]
import os #导入OS包
import time

# 定义函数方法
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) "
                        "AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1",
           }

url = 'http://xkxt.ecjtu.edu.cn'

cur_dir = 'D:\\img\\'

def spiderPic(pathword):

    list = '/servlet/code.servlet'
    print('正在爬取URL地址：' + str(url+list))
    try:
        pics = requests.get(url+list, timeout=20, headers=headers)  # 请求URL时间（最大10秒）
        print(pics.status_code)
        #print(pics.content)
    except requests.exceptions.ConnectionError:
        print('您当前请求的URL地址出现错误！')
    fq = open(cur_dir+pathword+'\\' + (pathword + '_' + str(random.randrange(0, 10000, 4)) + '.jpg'), 'wb')  # 下载图片，并保存和命名
    fq.write(pics.content)#存入图片到路径对应文件夹中
    fq.close()

# python的主方法
if __name__ == '__main__':
    flie = '验证码'
    path = 'D:\\img\\'+ flie + ''
    y = os.path.exists(path)#查看路径是否存在
    if y == 1:
        print('该文件已存在！')
    else:
        if os.path.isdir(cur_dir):
            os.mkdir(os.path.join(cur_dir, flie))#创建路径下输入文件夹名称+

    # 调用函数
    n = 0
    while (n < 1000):
        spiderPic(flie)
        n = n+1
