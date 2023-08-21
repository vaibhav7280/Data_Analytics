import mysql.connector
from getpass import getpass

try:
    with mysql.connector.connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="uber_project",
    ) as connection:

        trips_by_distance_and_duration = """
    SELECT  trip_distance_miles,
TIMESTAMPDIFF(MINUTE, begintrip_date_time, dropoff_date_time) AS trip_duration_minutes 
FROM uber_tripdata;
    """

        with connection.cursor() as cursor:
            cursor.execute(trips_by_distance_and_duration)
            trips_by_distance_and_duration_results = cursor.fetchall()
            
            print("Trips by Distance & Duration:")
            for row in trips_by_distance_and_duration_results:
                print("trip_distance_miles:", row[0])
                print("trip_duration_minutes:", row[1])
                print()

except mysql.connector.Error as e:
    print("Error:", e)
