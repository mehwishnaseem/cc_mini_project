import os
import pymysql


def insert_data():
    connection = pymysql.connect(host=os.environ.get('DB_HOST'),
                             port=3306,
                            user=os.environ.get('DB_USER'),
                            password=os.environ.get('DB_PASS'),
                            database='openuv')
    cursor = connection.cursor()
    query = "INSERT INTO `test` (`abc`,`def`) VALUES ('shanzay', 'atif')"
    cursor.execute(query)
    connection.commit()
    connection.close()

def insert_uv_index(uv, uv_max, uv_max_time, uv_time):
    connection = pymysql.connect(host=os.environ.get('DB_HOST'),
                             port=3306,
                            user=os.environ.get('DB_USER'),
                            password=os.environ.get('DB_PASS'),
                            database='openuv')
    cursor = connection.cursor()
    query = "INSERT INTO `uv_index` (`uv`,`uv_max`,`uv_max_time`,`uv_time`) VALUES (%s, %s, %s, %s)"
    cursor.execute(query,(uv, uv_max, uv_max_time, uv_time))
    connection.commit()
    connection.close()

if __name__ == '__main__':
    insert_uv_index(uv=1, uv_max=2, uv_max_time=3, uv_time=4)