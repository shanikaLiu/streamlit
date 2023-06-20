# 执行爬虫文件并记录日志
import logging
import os


def logger(path):

    standard_format = "%(asctime)s [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s"

    # 如果不存在定义的日志目录就创建一个

    if os.path.exists(path):

        print(f'>>> log path {path} existed.')

    else:

        print(f'>>> log path {path} created.')

        os.makedirs(path)

    logging.basicConfig(
                        filename=os.path.join(path,'log.log'),
                        filemode='a',
                        format=standard_format,
                        level=logging.INFO
                        )

    logger = logging.getLogger(__name__)  # 生成一个log实例

    return logger