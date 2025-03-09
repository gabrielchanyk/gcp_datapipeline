import pymysql
import logging

secret_path = "/secrets/my_sql_pw"

# Read the secret value from the file
with open(secret_path, 'r') as secret_file:
    secret_value = secret_file.read().strip()

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="mysql-191e4b62-bellassignment55-04a3.g.aivencloud.com",
  password=secret_value,
  read_timeout=timeout,
  port=18533,
  user="avnadmin",
  write_timeout=timeout,
)
logging.info(secret_value)
  
try:
  cursor = connection.cursor()
  cursor.execute("DROP TABLE mytest")
#   cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
#   cursor.execute("SELECT * FROM mytest")
  print(cursor.fetchall())
finally:
  connection.close()