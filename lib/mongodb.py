from mongoengine import connect

class MongoDB:
    def __init__(self, config):
        self.__db_connection = connect(host=config['db_connection_string'])
    
    @property
    def DB(self):
        return self.__db_conenction