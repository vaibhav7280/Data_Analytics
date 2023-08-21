import mysql.connector
from getpass import getpass

try:
    with mysql.connector.connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="uber_project",
    ) as connection:

        trips_by_hour_day = """
    SELECT HOUR(begintrip_date_time) AS hour_of_day,
           DAYOFWEEK(begintrip_date_time) AS day_of_week,
           COUNT(*) AS num_trips
    FROM uber_tripdata
    GROUP BY HOUR(begintrip_date_time), DAYOFWEEK(begintrip_date_time);
    """

        with connection.cursor() as cursor:
            cursor.execute(trips_by_hour_day)
            trips_by_hour_day_results = cursor.fetchall()
            
            print("trips by hour day:")
            for row in trips_by_hour_day_results:
                print("Hour of Day:", row[0])
                print("Day of Week:", row[1])
                print("Number of Trips:", row[2])
                print()

except mysql.connector.Error as e:
    print("Error:", e)
