import os

env_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')

with open(env_file_path, 'r') as env_file:
    env_vars = dict(
        line.strip().split('=') for line in env_file if '=' in line
    )

database_name = env_vars.get('MYSQL_DATABASE')

sql_content = f"""CREATE DATABASE {database_name};

USE {database_name};
"""

sql_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'create_schema.sql')

with open(sql_file_path, 'w') as sql_file:
    sql_file.write(sql_content)