from pages.BasePage import BasePage


class DMLPage(BasePage):

    def __init__(self, conn):
        super().__init__(conn)

    def executeSelectQuery(self, sql_query):
        self.executeSQLQuery(sql_query)
        return self.dbCur.fetchall()

    def insertQuery(self, table_name, values: list):
        query = ''
        for value in values:
            tuple_data = ''
            for table_data in value:
                tuple_data = tuple_data + "'" + str(table_data) + "',"
            tuple_data = "(" + tuple_data[:tuple_data.rfind(",")] + ")"
            query = query + tuple_data + ","
        insert_sql_query = '''
            Insert into {0} values {1};
        '''.format(table_name, query[:query.rfind(",")])
        self.executeSQLQuery(insert_sql_query)

    def updateDataDBTable(self, sql_query):
        self.executeSQLQuery(sql_query)

    def deleteDataDBTable(self, sql_query):
        self.executeSQLQuery(sql_query)