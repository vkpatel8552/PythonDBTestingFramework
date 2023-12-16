from pages.DDLQueryPage import DDLQuery
from pages.DMLQueryPage import DMLPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestDML(BaseTest):
    table_name = 'department'

    """
    Test Case to verify DML-insert data
    """

    def test_insert_single_data_department_table(self):
        dml_page = DMLPage(self.conn)
        values = [(10, 'FINANCE', 'EDINBURGH')]
        dml_page.insertQuery(self.table_name, values)
        assert_department_table_query = '''
            select * from {0}; 
        '''.format(self.table_name)
        record = dml_page.executeSelectQuery(assert_department_table_query)
        assert record == values, "Data is not inserted into the table"

    """
        Test Case to verify DML-insert multiple data 
    """
    def test_insert_multiple_data_department_table(self):
        dml_page = DMLPage(self.conn)
        values = ExcelUtils.get_data_from_excel("testData/FivetranData.xlsx", "InsertData")
        dml_page.insertQuery(self.table_name, values)
        assert_department_table_query = '''
                select * from {0}; 
            '''.format(self.table_name)

        record = dml_page.executeSelectQuery(assert_department_table_query)
        for i in range(len(values)):
            record_data = record[i]
            actual_data = values[i]
            for j in range(len(record_data)):
                assert str(actual_data[j]) == str(record_data[j]), "Data is not inserted into the table"

    """
       Test Case to verify DML-update data
       """

    def test_update_data_department_table(self):
        dml_page = DMLPage(self.conn)
        values = ExcelUtils.get_data_from_excel("testData/FivetranData.xlsx", "InsertData")
        dml_page.insertQuery(self.table_name, values)

        sql_query = '''
            Update {0}
            Set location = 'Miami'
            where deptcode = '10';
        '''.format(self.table_name)
        dml_page.updateDataDBTable(sql_query)

        assert_department_table_query = '''
               select location from {0} where deptcode='10';
           '''.format(self.table_name)
        record = dml_page.executeSelectQuery(assert_department_table_query)
        assert str(record[0][0]) == 'Miami', "Data is not updated in given table"

    """
       Test Case to verify DML-delete data
       """

    def test_delete_data_department_table(self):
        dml_page = DMLPage(self.conn)
        values = ExcelUtils.get_data_from_excel("testData/FivetranData.xlsx", "InsertData")
        dml_page.insertQuery(self.table_name, values)
        assert_department_table_query = '''
                      select count(*) from {0};
                  '''.format(self.table_name)
        before_delete_count = dml_page.executeSelectQuery(assert_department_table_query)

        sql_query = '''
            Delete from {0}
            where deptcode = '10';
        '''.format(self.table_name)
        dml_page.deleteDataDBTable(sql_query)

        after_delete_count = dml_page.executeSelectQuery(assert_department_table_query)
        assert before_delete_count > after_delete_count, "Record doesn't deleted from database"

