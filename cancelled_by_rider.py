import mysql.connector
from getpass import getpass

try:
    with mysql.connector.connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="uber_project",
    ) as connection:

        cancelled_by_rider= '''SELECT client_uuid, COUNT(CASE WHEN status = 'rider_canceled' THEN 1 ELSE NULL END) AS cancelled_by_rider, COUNT(*) AS total_trips,(COUNT(CASE WHEN status = 'rider_canceled' THEN 1 ELSE NULL END) / COUNT(*)) * 100 AS cancellation_rate_by_rider FROM uber_tripdata GROUP BY client_uuid;'''

        with connection.cursor() as cursor:
            cursor.execute(cancelled_by_rider)
            cancelled_by_rider_results = cursor.fetchall()
            
            print("Cancellation Rate by Rider:")
            for row in cancelled_by_rider_results:
                print("Client UUID:", row[0])
                print("Completed Trips:", row[1])
                print("Total Trips:", row[2])
                print("Cancellation Rate by Rider (%):", row[3])
                print()

except mysql.connector.Error as e:
    print("Error:", e)
