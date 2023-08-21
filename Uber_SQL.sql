SELECT client_uuid, AVG(trip_distance_miles) AS avg_trips_per_rider FROM uber_tripdata GROUP BY client_uuid;
use uber_project;
SELECT client_uuid, AVG(trip_distance_miles) AS avg_trips_per_rider FROM uber_tripdata WHERE is_subs_trip = 'TRUE' GROUP BY client_uuid;
SELECT client_uuid, AVG(avg_trips_per_rider) AS avg_trips_per_rider_subscription FROM (SELECT client_uuid, AVG(trip_distance_miles) AS avg_trips_per_rider FROM uber_tripdata WHERE is_subs_trip = 'TRUE' GROUP BY client_uuid) AS tpr_subquery;
SELECT client_uuid, 
    COUNT(CASE WHEN status = 'completed' THEN 1 ELSE NULL END) AS completed_trips,
    COUNT(*) AS total_trips,
    (COUNT(CASE WHEN status = 'completed' THEN 1 ELSE NULL END) / COUNT(*)) * 100 AS fulfillment_rate FROM uber_tripdata GROUP BY client_uuid;
SELECT client_uuid, (SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) / SUM(1)) * 100 AS fulfillment_rate FROM uber_tripdata GROUP BY client_uuid;
SELECT client_uuid, COUNT(*) AS total_trips FROM uber_tripdata GROUP BY client_uuid;
SELECT client_uuid, 
    COUNT(CASE WHEN status = 'rider_canceled' THEN 1 ELSE NULL END) AS cancelled_by_rider,
    COUNT(*) AS total_trips,
    (COUNT(CASE WHEN status = 'rider_canceled' THEN 1 ELSE NULL END) / COUNT(*)) * 100 AS cancellation_rate_by_rider FROM uber_tripdata GROUP BY client_uuid;
    SELECT driver_uuid, 
    COUNT(CASE WHEN status = 'driver_canceled' THEN 1 ELSE NULL END) AS cancelled_by_driver,
    COUNT(*) AS total_trips,
    (COUNT(CASE WHEN status = 'driver_canceled' THEN 1 ELSE NULL END) / COUNT(*)) * 100 AS cancellation_rate_by_driver
    FROM uber_tripdata WHERE driver_uuid !='' GROUP BY driver_uuid;
    SELECT HOUR(begintrip_date_time) AS hour_of_day,
       DAYOFWEEK(begintrip_date_time) AS day_of_week,
       COUNT(CASE WHEN status = 'completed' THEN 1 ELSE NULL END) AS completed_trips,
       COUNT(*) AS total_trips,
       (COUNT(CASE WHEN status = 'completed' THEN 1 ELSE NULL END) / COUNT(*)) * 100 AS fulfillment_rate
FROM uber_tripdata WHERE begintrip_date_time !=''
GROUP BY HOUR(begintrip_date_time), DAYOFWEEK(begintrip_date_time);
SELECT TIMESTAMPDIFF(MINUTE, request_date_time, begintrip_date_time) AS trip_duration,
       request_type
FROM uber_tripdata
WHERE request_type IN ('microscheduling', 'prescheduling');
SELECT HOUR(begintrip_date_time) AS hour_of_day,
DAYOFWEEK(begintrip_date_time) AS day_of_week,
COUNT(*) AS num_trips
FROM uber_tripdata WHERE begintrip_date_time !=''
GROUP BY HOUR(begintrip_date_time), DAYOFWEEK(begintrip_date_time);
SELECT payment_method, COUNT(*) AS num_trips
    FROM uber_tripdata
    GROUP BY payment_method;
SELECT vehicle_capacity, AVG(trips_per_capacity) AS avg_utilization
FROM (
        SELECT vehicle_capacity, COUNT(*) / vehicle_capacity AS trips_per_capacity
        FROM uber_tripdata WHERE vehicle_capacity !=''
        GROUP BY vehicle_uuid
    ) AS trips_per_capacity_subquery
    GROUP BY vehicle_capacity;
SELECT client_uuid, pickup_walking_distance_meters FROM uber_tripdata;
SELECT trip_distance_miles FROM uber_tripdata;
SELECT TIMESTAMPDIFF(MINUTE, begintrip_date_time, dropoff_date_time) AS trip_duration_minutes
FROM uber_tripdata;
SELECT  trip_distance_miles,
TIMESTAMPDIFF(MINUTE, begintrip_date_time, dropoff_date_time) AS trip_duration_minutes 
FROM uber_tripdata;