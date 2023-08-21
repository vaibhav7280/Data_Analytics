import mysql.connector
from getpass import getpass

try:
    with mysql.connector.connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="uber_project",
    ) as connection:

        vehicle_utilization = """
    SELECT vehicle_capacity, AVG(trips_per_capacity) AS avg_utilization
    FROM (
        SELECT vehicle_capacity, COUNT(*) / vehicle_capacity AS trips_per_capacity
        FROM uber_tripdata
        GROUP BY vehicle_uuid
    ) AS trips_per_capacity_subquery
    GROUP BY vehicle_capacity;
    """

        with connection.cursor() as cursor:
            cursor.execute(vehicle_utilization)
            vehicle_utilization_results = cursor.fetchall()
            
            print("Vehicle Utilization:")
            for row in vehicle_utilization_results:
                print("Vehicle Capacity", row[0])
                print("avg_utilization:", row[1])
                print()

except mysql.connector.Error as e:
    print("Error:", e)
