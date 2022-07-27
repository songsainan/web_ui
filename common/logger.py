import logging
import os.path
import time
from common.path import LOG_DIR


class Logger:
    @classmethod
    def create_logger(cls):
        logger = logging.getLogger('my_logger')
        logger.setLevel('DEBUG')
        now_time = time.strftime('%Y%m%d%H%M%S')
        log_name = now_time + '.log'

        # 输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel('DEBUG')
        logger.addHandler(sh)

        # 输出到文件
        fh = logging.FileHandler(filename=os.path.join(LOG_DIR, log_name), encoding='utf-8')
        fh.setLevel('DEBUG')
        logger.addHandler(fh)

        # 设置输出格式
        formater = logging.Formatter('%(levelname)s :%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(message)s')

        # 绑定输出渠道
        sh.setFormatter(formater)
        fh.setFormatter(formater)
        return logger


log = Logger.create_logger()
