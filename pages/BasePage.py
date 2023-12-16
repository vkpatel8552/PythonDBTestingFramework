import psycopg2
from multipledispatch import dispatch

class BasePage:

    def __init__(self, conn):
        self.dbConn = conn
        self.dbCur = self.dbConn.cursor()

    @dispatch(str)
    def executeSQLQuery(self, sql_query: str):
        self.dbCur.execute(sql_query)
        self.commitSQL()

    @dispatch(str, tuple)
    def executeSQLQuery(self, sql_query: str, values: tuple):
        self.dbCur.execute(sql_query, values)
        self.commitSQL()

    def commitSQL(self):
        self.dbConn.commit()
