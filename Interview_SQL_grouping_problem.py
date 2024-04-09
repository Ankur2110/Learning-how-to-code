# | ID | Firstname | Lastname | ReportsTo | Position | Age |
# |----|-----------|----------|-----------|----------|-----|
# | 1  | John      | Doe      | Manager   | Manager  | 35  |
# | 2  | Alice     | Smith    | Manager   | Assistant| 28  |
# | 3  | Bob       | Johnson  | Manager   | Assistant| 32  |
# | 4  | Emily     | Brown    | John      | Staff    | 25  |
# | 5  | Michael   | Lee      | John      | Staff    | 30  |
# | 6  | Sarah     | White    | Alice     | Staff    | 27  |
# | 7  | David     | Anderson | Bob       | Staff    | 33  |
# | 8  | Jessica   | Clark    | Bob       | Staff    | 29  |


# Return a table which lists all the persons who are being reported to, the average of people who report to them, and the total number of people who report
# to them

SELECT ReportsTo,
       COUNT(ID) AS Members,
       AVG(Age) AS `Average Age`
FROM maintable_27RXM
WHERE ReportsTo IS NOT NULL
GROUP BY ReportsTo
ORDER BY ReportsTo;


