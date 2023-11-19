# SELECT c.login, COUNT (o.id)
         FROM "Couriers" AS c INNER JOIN "Orders" AS o ON o."courierId" = c.id
         WHERE o."inDelivery" = true
         GROUP BY c.login;

SELECT track,
       CASE
       WHEN finished = true THEN 2
       WHEN cancelled = true THEN -1
       WHEN o."inDelivery" = true THEN 1
       ELSE 0
       END AS status_value
       FROM "Orders" AS o;