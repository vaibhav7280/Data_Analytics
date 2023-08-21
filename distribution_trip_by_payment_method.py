import mysql.connector
from getpass import getpass

try:
    with mysql.connector.connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="uber_project",
    ) as connection:

        trips_by_payment_method= """
    SELECT payment_method, COUNT(*) AS num_trips
    FROM uber_tripdata
    GROUP BY payment_method;
    """

        with connection.cursor() as cursor:
            cursor.execute(trips_by_payment_method)
            trips_by_payment_method_results = cursor.fetchall()
            
            print("trips by payment method:")
            for row in trips_by_payment_method_results:
                print("Payment Method:", row[0])
                print("Number of Trips:", row[1])
                print()

except mysql.connector.Error as e:
    print("Error:", e)
