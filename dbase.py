import os
import pymysql


def insert_data(city, lat, lng):
    connection = pymysql.connect(host=os.environ.get('DB_HOST'),
                             port=3306,
                            user=os.environ.get('DB_USER'),
                            password=os.environ.get('DB_PASS'),
                            database='openuv')
    cursor = connection.cursor()
    query = "INSERT INTO `city` (`city`, `lat`, `lng`) VALUES (%s, %s, %s)"
    cursor.execute(query, (city, lat, lng))
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

def select_data(name):
    connection = pymysql.connect(host=os.environ.get('DB_HOST'),
                             port=3306,
                            user=os.environ.get('DB_USER'),
                            password=os.environ.get('DB_PASS'),
                            database='openuv')
    cursor = connection.cursor()
    query = "SELECT city, lat, lng FROM city WHERE city like %s"
    cursor.execute(query, (name))
    records = cursor.fetchall() # (('Reading', 51.4542, -0.9731),)
    connection.close()
    return records[0][1], records[0][2]


if __name__ == '__main__':
    # insert_uv_index(uv=1, uv_max=2, uv_max_time=3, uv_time=4)
    select_data('Reading')