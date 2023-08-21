import mysql.connector
from getpass import getpass

try:
    with mysql.connector.connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="uber_project",
    ) as connection:

        fulfillment_rate_by_hour_week ='''SELECT HOUR(begintrip_date_time) AS hour_of_day,
       DAYOFWEEK(begintrip_date_time) AS day_of_week,
       COUNT(CASE WHEN status = 'completed' THEN 1 ELSE NULL END) AS completed_trips,
       COUNT(*) AS total_trips,
       (COUNT(CASE WHEN status = 'completed' THEN 1 ELSE NULL END) / COUNT(*)) * 100 AS fulfillment_rate
FROM uber_tripdata WHERE begintrip_date_time !=''
GROUP BY HOUR(begintrip_date_time), DAYOFWEEK(begintrip_date_time);'''

        with connection.cursor() as cursor:
            cursor.execute(fulfillment_rate_by_hour_week)
            fulfillment_rate_by_hour_week_results = cursor.fetchall()
            
            print("fulfillment rate by hour of day and by day of week:")
            for i in fulfillment_rate_by_hour_week_results:
                print("Hour of Day:", i[0])
                print("Day of Week:", i[1])
                print("Completed Trips:", i[2])
                print("Total Trips:", i[3])
                print("Fulfillment Rate (%):", i[4])
                print()

except mysql.connector.Error as e:
    print("Error:", e)
