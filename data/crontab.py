import time
from apscheduler.schedulers.background import BackgroundScheduler

from data.showdata import showdata

if __name__ == '__main__':

    scheduler = BackgroundScheduler()
    # 添加调度任务
    # 调度方法为 testdata，触发器选择 interval(间隔性)，间隔时长为 2s
    scheduler.add_job(showdata, 'interval', seconds=2)
    # 启动调度任务
    scheduler.start()

    while True:
        print(time.time())
        time.sleep(20)
