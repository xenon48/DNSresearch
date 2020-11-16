import numpy as np

def mysql(direction):
    import pymysql
    import pandas as pd
    from sshtunnel import SSHTunnelForwarder
    from os.path import expanduser

    home = expanduser('~')

    sql_hostname = 'localhost'
    sql_username = 'root'
    sql_password = ''
    sql_main_database = 'perl'
    sql_port = 3306
    ssh_host = '10.36.65.1'
    ssh_user = '***'
    ssh_password = '***'
    ssh_port = 22
    sql_ip = '127.0.0.1'

    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_password=ssh_password,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        conn = pymysql.connect(host='127.0.0.1', user=sql_username,
                passwd=sql_password, db=sql_main_database,
                port=tunnel.local_bind_port)
        query = '''SELECT VERSION();'''
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM traffic WHERE src_port = '53'")
        arr = np.array(cursor.fetchall())
        cursor.close()
        data = pd.read_sql_query(query, conn)
        conn.close()
    return arr



