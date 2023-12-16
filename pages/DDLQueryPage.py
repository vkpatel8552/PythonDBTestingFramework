from pages.BasePage import BasePage


class DDLQuery(BasePage):

    def __init__(self, conn):
        super().__init__(conn)

    def createDBTable(self, sql_query):
        self.executeSQLQuery(sql_query)

    def alterDBTable(self, table_name, operation, column_name, datatype=None):
        query = ''
        if operation == 'add':
            query = 'add {0} {1}'.format(column_name, datatype)
        elif operation == 'drop':
            query = 'drop column {0}'.format(column_name)
        elif operation == 'alter':
            query = 'alter column {0} Type {1}'.format(column_name, datatype)
        alter_sql_query = '''
            alter table {0} {1}
        '''.format(table_name, query)
        self.executeSQLQuery(alter_sql_query)

    def dropDBTable(self, table_name):
        drop_sql_query = 'DROP TABLE {0}'.format(table_name)
        self.executeSQLQuery(drop_sql_query)
