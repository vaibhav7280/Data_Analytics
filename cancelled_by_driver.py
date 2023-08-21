import mysql.connector
from getpass import getpass

try:
    with mysql.connector.connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="uber_project",
    ) as connection:

        cancelled_by_driver = '''SELECT driver_uuid, 
    COUNT(CASE WHEN status = 'driver_canceled' THEN 1 ELSE NULL END) AS cancelled_by_driver,
    COUNT(*) AS total_trips,
    (COUNT(CASE WHEN status = 'driver_canceled' THEN 1 ELSE NULL END) / COUNT(*)) * 100 AS cancellation_rate_by_driver
    FROM uber_tripdata WHERE driver_uuid !='' GROUP BY driver_uuid;'''

        with connection.cursor() as cursor:
            cursor.execute(cancelled_by_driver)
            cancelled_by_driver_results = cursor.fetchall()
            
            print("cancelled_by_driver:")
            for row in cancelled_by_driver_results:
                print("Client UUID:", row[0])
                print("Completed Trips:", row[1])
                print("Total Trips:", row[2])
                print("Fulfillment Rate (%):", row[3])
                print()

except mysql.connector.Error as e:
    print("Error:", e)
