import logging as lg
class Logs:
    def basicconfig(self):
        try:
            '''
            this is the basic configuration for the logger
            '''
            lg.basicConfig(filename="logs.log",
                                  level=lg.INFO,
                                  format='%(module)s:: %(asctime)s :: %(levelname)s :: %(message)s')

        except Exception as e:
            raise Exception("Something is wrong with basicconfig")

    def info(self, log):
        try:
            self.basicconfig()
            return lg.info(log)
        except Exception as e:
            print("logs.INFO is not working")

    def warning(self, log):
        try:
            self.basicconfig()
            return lg.warning(log)
        except Exception as e:
            print("logs.WARNING is not working")

    def error(self, log):
        try:
            self.basicconfig()
            return lg.error(log)
        except Exception as e:
            print("logs.ERROR is not working")

    def critical(self, log):
        try:
            self.basicconfig()
            return lg.critical(log)
        except Exception as e:
            print("logs.CRITICAL is not working")

    def exception(self, log):
        try:
            self.basicconfig()
            return lg.exception(log)
        except Exception as e:
            print("logs.EXCEPTION is not working")
