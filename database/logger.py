import logging as lg
import sys

sys.tracebacklimit = 0


class Logs:
    try:
        sys.tracebacklimit = 0

        def __init__(self):
            self.logger = lg.getLogger(__name__)
            self.logger.setLevel(lg.INFO)
            formatter = lg.Formatter('%(module)s:: %(asctime)s :: %(levelname)s :: %(message)s')
            file_handler = lg.FileHandler('E:/University Application/mylogs.log')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
    except Exception as e:
        raise Exception("Something is wrong with basicconfig")

    def debug(self, log):
        try:
            return self.logger.debug(log)
        except Exception as e:
            print("logs.INFO is not working")

    def info(self, log):
        try:
            return self.logger.info(msg=log)
        except Exception as e:
            print("logs.INFO is not working")

    def warning(self, log):
        try:
            return self.logger.warning(log)
        except Exception as e:
            print("logs.WARNING is not working")

    def error(self, log):
        try:
            return self.logger.error(log)
        except Exception as e:
            print("logs.ERROR is not working")

    def critical(self, log):
        try:
            return self.logger.critical(log)
        except Exception as e:
            print("logs.CRITICAL is not working")

    def exception(self, log):
        try:
            return self.logger.exception(log)
        except Exception as e:
            print("logs.EXCEPTION is not working")


