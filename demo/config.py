import os

MYSQL_DSN = {
    'user': os.getenv('DEMO_MYSQL_USER', '<mysql_db_username>'),
    'password': os.getenv('DEMO_MYSQL_PASSWORD', '<mysql_db_password>'),
    'host': os.getenv('DEMO_MYSQL_HOST', '<mysql_db_host>'),
    'database': os.getenv('DEMO_MYSQL_DB', '<mysql_db_name>'),
}

PGSQL_DSN = {
    'user': os.getenv('DEMO_PGSQL_USER', '<postgresql_db_username>'),
    'password': os.getenv('DEMO_PGSQL_PASSWORD', '<postgresql_db_password>'),
    'host': os.getenv('DEMO_PGSQL_HOST', '<postgresql_db_host>'),
    'database': os.getenv('DEMO_PGSQL_DB', '<postgresql_db_name>'),
}
