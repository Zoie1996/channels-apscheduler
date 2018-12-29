import random
import string
import time
import traceback, logging

import pymysql.cursors
from apscheduler.schedulers.background import BackgroundScheduler

connect_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'db': 'data',
    'charset': 'utf8',
    'port': 3306
}


def connect_mysql():
    """ 创建链接 """
    try:
        return pymysql.connect(cursorclass=pymysql.cursors.DictCursor, **connect_config)
    except Exception as e:
        logging.error(traceback.format_exc())
        logging.error("cannot create mysql connect")


def insertone(sql, param=None):
    """
    插入一条数据
    :param sql: sql语句
    :param param: string|tuple
    :return: id
    """
    con = connect_mysql()
    cur = con.cursor()

    lastrowid = 0
    try:
        cur.execute(sql, param)
        con.commit()
        lastrowid = cur.lastrowid
    except Exception as e:
        con.rollback()
        logging.error(traceback.format_exc())
        logging.error("[sql]:{} [param]:{}".format(sql, param))

    cur.close()
    con.close()
    return lastrowid


def savedata():
    username = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    sql_str = "insert into auth_user(username, password) values (%s, %s)"
    print("插入数据:", insertone(sql_str, (username, "123456")))


if __name__ == '__main__':

    scheduler = BackgroundScheduler()
    # 添加调度任务
    # 调度方法为 savedata，触发器选择 interval(间隔性)，间隔时长为 2s
    scheduler.add_job(savedata, 'interval', seconds=2)
    # 启动调度任务
    scheduler.start()

    while True:
        print(time.time())
        time.sleep(20)
