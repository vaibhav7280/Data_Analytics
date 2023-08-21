import mysql.connector
from getpass import getpass

try:
    with mysql.connector.connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="uber_project",
    ) as connection:

        tpr_subs_query = "SELECT client_uuid, AVG(trip_distance_miles) AS avg_trips_per_rider FROM uber_tripdata WHERE is_subs_trip = 'TRUE' GROUP BY client_uuid;"

        with connection.cursor() as cursor:
            cursor.execute(tpr_subs_query)
            tpr_results = cursor.fetchall()
            
            for row in tpr_results:
                print(row)
except mysql.connector.Error as e:
    print("Error:", e)
