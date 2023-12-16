from pages.DDLQueryPage import DDLQuery
from pages.DMLQueryPage import DMLPage
from tests.BaseTest import BaseTest


class TestDDL(BaseTest):
    table_name = 'department'

    """
    Test Case to verify DDL-Create Table Operation
    """

    def test_create_department_table(self):
        dml_page = DMLPage(self.conn)
        assert_department_table_query = '''
            select exists( 
                select 1 from information_schema.tables
                where table_name = '{0}')
                as table_existence;
        '''.format(self.table_name)

        record = dml_page.executeSelectQuery(assert_department_table_query)
        assert record[0].__contains__(True), "DataTable:'{0}' doesn't exist in Database".format(self.table_name)

    """
    Test Case to verify DDL-Alter Table Add Column Operation
    """

    def test_add_new_column_dbtable(self):
        ddl_page = DDLQuery(self.conn)
        dml_page = DMLPage(self.conn)
        column_name = 'isNew'
        ddl_page.alterDBTable(self.table_name, 'add', column_name, 'boolean')
        assert_department_column_query = '''
                   select exists( 
                       select '{0}' from information_schema.columns
                       where table_name = '{1}')
                       as table_existence;
               '''.format(column_name, self.table_name)

        record = dml_page.executeSelectQuery(assert_department_column_query)
        assert record[0].__contains__(True), "Column:'{0}' added successfully in Datatable.".format(column_name)

    """
    Test Case to verify DDL-Alter Table Alter Column Operation
    """

    def test_alter_existing_column_dbtable(self):
        ddl_page = DDLQuery(self.conn)
        dml_page = DMLPage(self.conn)
        column_name = 'location'
        ddl_page.alterDBTable(self.table_name, 'alter', column_name, 'char(100)')
        assert_department_column_query = '''
                       select data_type from information_schema.columns
                       where table_name = '{0}' 
                       and column_name = '{1}'
               '''.format(self.table_name, column_name)

        record = dml_page.executeSelectQuery(assert_department_column_query)
        print(record)
        assert record[0].__contains__(
            'character'), "Datatype of Column:'{0}' changed successfully in Datatable.".format(column_name)
