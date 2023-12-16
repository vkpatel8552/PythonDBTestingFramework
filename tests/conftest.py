import psycopg2
import psycopg2.extras
import pytest
import allure
from allure_commons.types import AttachmentType

from pages.DDLQueryPage import DDLQuery
from pages.DMLQueryPage import DMLPage
from utilities import ReadConfigurations


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope='class')
def setup_and_teardown(request):
    hostname = ReadConfigurations.read_configuration("DB_Info", "hostname")
    database = ReadConfigurations.read_configuration("DB_Info", "database")
    username = ReadConfigurations.read_configuration("DB_Info", "username")
    pwd = ReadConfigurations.read_configuration("DB_Info", "password")
    port_id = ReadConfigurations.read_configuration("DB_Info", "port_id")

    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id
        ) as conn:

            print("Successfully Connected to DB: ", database)

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                request.cls.conn = conn
                request.cls.cur = cur
    except Exception as error:
        print(error)
    yield
    if cur is not None:
        cur.close()
        print("Cursor Connection Closed")
    if conn is not None:
        conn.close()
        print("Database Connection Closed")


@pytest.fixture()
def create_department_table(request):
    create_department_query = '''
                create table if not exists department
                    (
                       deptcode   int PRIMARY KEY,
                       deptname   varchar(30) NOT NULL,
                       location   varchar(40) NOT NULL
                    );
            '''

    ddl_page = DDLQuery(request.cls.conn)
    ddl_page.createDBTable(create_department_query)
    print("DataTable: {0} created successfully".format("department"))
    yield
    ddl_page = DDLQuery(request.cls.conn)
    ddl_page.dropDBTable(table_name='department')
    print("DataTable: {0} dropped successfully".format("department"))
