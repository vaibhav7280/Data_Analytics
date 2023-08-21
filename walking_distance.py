import mysql.connector
import pandas as pd
from getpass import getpass
import matplotlib.pyplot as plt

try:
    connection = mysql.connector.connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="uber_project",
    )

    walking_distance_query = """
    SELECT client_uuid, pickup_walking_distance_meters
    FROM uber_tripdata;
    """

    df = pd.read_sql_query(walking_distance_query, connection)

    # Define reasonable buckets for walking distance ranges
    bins = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    labels = ['0-100', '101-200', '201-300', '301-400', '401-500', '501-600', '601-700', '701-800', '801-900', '901-1000']

    # Calculate average walking distance by rider
    avg_distance_by_rider = df.groupby('client_uuid')['pickup_walking_distance_meters'].mean()

    # Calculate percentage of trips with corresponding walking distance bucket
    df['distance_bucket'] = pd.cut(df['pickup_walking_distance_meters'], bins=bins, labels=labels)
    percentage_by_bucket = df['distance_bucket'].value_counts(normalize=True) * 100

    # Plot average walking distance by rider
    plt.figure(figsize=(12, 6))
    avg_distance_by_rider.plot(kind='bar', color='blue')
    plt.xlabel('Rider')
    plt.ylabel('Average Walking Distance (meters)')
    plt.title('Average Walking Distance by Rider')
    plt.xticks(rotation=45)
    plt.show()

    # Plot percentage of trips with corresponding walking distance bucket
    plt.figure(figsize=(12, 6))
    percentage_by_bucket.plot(kind='bar', color='green')
    plt.xlabel('Walking Distance Bucket')
    plt.ylabel('Percentage of Trips (%)')
    plt.title('Percentage of Trips by Walking Distance Bucket')
    plt.xticks(rotation=45)
    plt.show()

except mysql.connector.Error as e:
    print("Error:", e)
finally:
    connection.close()
