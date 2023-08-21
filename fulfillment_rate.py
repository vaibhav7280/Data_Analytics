import mysql.connector
from getpass import getpass

try:
    with mysql.connector.connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="uber_project",
    ) as connection:

        fulfillment_rate = "SELECT client_uuid, COUNT(CASE WHEN status = 'completed' THEN 1 ELSE NULL END) AS completed_trips, COUNT(*) AS total_trips, (COUNT(CASE WHEN status = 'completed' THEN 1 ELSE NULL END) / COUNT(*)) * 100 AS fulfillment_rate FROM uber_tripdata GROUP BY client_uuid;"

        with connection.cursor() as cursor:
            cursor.execute(fulfillment_rate)
            fulfillment_rate_results = cursor.fetchall()
            
            print("Fulfillment Rate by Rider:")
            for row in fulfillment_rate_results:
                print("Client UUID:", row[0])
                print("Completed Trips:", row[1])
                print("Total Trips:", row[2])
                print("Fulfillment Rate (%):", row[3])
                print()

except mysql.connector.Error as e:
    print("Error:", e)
