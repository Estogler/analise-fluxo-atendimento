SELECT day_of_week, COUNT(*) as total
FROM atendimentos
GROUP BY day_of_week;

SELECT "no-show", AVG(waiting_days)
FROM atendimentos
GROUP BY "no-show";