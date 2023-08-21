import mysql.connector
from getpass import getpass

try:
    with mysql.connector.connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="uber_project",
    ) as connection:

        distribution_trip_request_type = '''SELECT TIMESTAMPDIFF(MINUTE, request_date_time, begintrip_date_time) AS trip_duration,
        request_type
        FROM uber_tripdata
        WHERE request_type IN ('microscheduling', 'prescheduling');'''

        with connection.cursor() as cursor:
            cursor.execute(distribution_trip_request_type)
            distribution_trip_request_type_results = cursor.fetchall()
            
            print("distribution trip request type:")
            for row in distribution_trip_request_type_results:
                print("Trip Duration:", row[0])
                print("Request Type:", row[1])
                print()

except mysql.connector.Error as e:
    print("Error:", e)
