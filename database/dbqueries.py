from configparser import ConfigParser

from database.logger import Logs

logs: Logs = Logs()


class Dbqueries:
    def fetch_query(self, section, element):
        try:
            """
            This Function helps us for fetching element from config File
            :param section: What section you want to access
            :param element: Key for the element you want to access from the file
            :return: returns the Value wrt the given Key
            """
            config = ConfigParser()
            config.read("resources/databasequeries.ini")
            result = config[section][element]
            logs.info(f"{element} from {section} from dbquery has been successfully accessed  ")
            return result
        except Exception as e:
            logs.exception(e)
