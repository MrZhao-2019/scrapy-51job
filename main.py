# 这个是定时启动的脚本

import os
import time

while True:
    os.system("scrapy crawl qiancheng")  # 相当于在命令行执行命令
    time.sleep(30)  # 休息30秒


