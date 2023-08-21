from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="uber_project",
    ) as connection:
        print(connection)
except Error as e:
    print(e)

TPR = "SELECT client_uuid, AVG(trip_distance_miles) AS avg_trips_per_rider FROM uber_tripdata GROUP BY client_uuid" with
uber_project.cursor() as cursor:
    cursor.execute(TPR)
