# SQL LeetCode Journey 

Tracking my SQL learning and problem-solving progress.

## Progress

* Started: June 2026
* Total Problems Solved: 8
* Easy: 8
* Medium: 0
* Hard: 0

---

## Solved Problems

| #    | Problem                                                                                                                                         | Difficulty | Topics                                         |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------------------------------------- |
| 584  | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/)                                                                   | Easy       | SELECT, WHERE, NULL Handling                   |
| 1683 | [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/)                                                                                 | Easy       | SELECT, WHERE, LENGTH()                        |
| 1378 | [Replace Employee ID With The Unique Identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/)                 | Easy       | LEFT JOIN                                      |
| 1068 | [Product Sales Analysis I](https://leetcode.com/problems/product-sales-analysis-i/)                                                             | Easy       | INNER JOIN                                     |
| 1581 | [Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/) | Easy       | LEFT JOIN, IS NULL, GROUP BY, COUNT(*)         |
| 577  | [Employee Bonus](https://leetcode.com/problems/employee-bonus/)                                                                                 | Easy       | LEFT JOIN, NULL Handling                       |
| 596  | [Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/)                                                     | Easy       | GROUP BY, HAVING, COUNT(*)                     |
| 1211 | [Queries Quality and Percentage](https://leetcode.com/problems/queries-quality-and-percentage/)                                                 | Easy       | GROUP BY, AVG(), ROUND(), Conditional Counting |

---

## SQL Topics Learned

### Basic Queries

* SELECT
* WHERE
* NULL Handling
* LENGTH()

### Joins

* INNER JOIN
* LEFT JOIN
* LEFT JOIN + IS NULL

### Aggregations

* COUNT(*)
* AVG()
* GROUP BY
* HAVING

### Conditional Aggregation

* COUNT(CASE WHEN condition THEN 1 END)
* SUM(CASE WHEN condition THEN 1 ELSE 0 END)
* AVG(condition)

### Formatting

* ROUND()

---

## Repository Structure

```text
Easy/
├── 584_Find_Customer_Referee.sql
├── 1683_Invalid_Tweets.sql
├── 1378_Replace_Employee_ID_With_The_Unique_Identifier.sql
├── 1068_Product_Sales_Analysis_I.sql
├── 1581_Customer_Who_Visited_But_Did_Not_Make_Any_Transactions.sql
├── 577_Employee_Bonus.sql
├── 596_Classes_More_Than_5_Students.sql
└── 1211_Queries_Quality_And_Percentage.sql

Notes/
├── Day_01.md
├── Day_02.md
├── Day_03.md
└── SQL_Patterns.md
```

---

## SQL Patterns Mastered

✅ Basic Filtering

✅ NULL Handling

✅ INNER JOIN

✅ LEFT JOIN

✅ LEFT JOIN + IS NULL

✅ GROUP BY

✅ HAVING

✅ COUNT(*)

✅ AVG()

✅ Conditional Counting

✅ Boolean Aggregation (`AVG(condition)`)

✅ ROUND()

---

## Current Focus

* ORDER BY
* LIMIT
* MAX()
* MIN()
* Highest / Lowest Problems
* Top N Problems
* Placement-Oriented SQL Patterns

---

## Goal

* Solve 100+ SQL Problems
* Master SQL for Placements
* Build Consistency Through Daily Practice
* Create a Strong SQL Portfolio on GitHub
* Maintain Daily Learning Notes

---

## Next Learning Roadmap

* 619 - Biggest Single Number
* 176 - Second Highest Salary
* 177 - Nth Highest Salary

Focus:

* ORDER BY
* LIMIT
* MAX / MIN
* First / Last Record Patterns
* Top-N Queries

````

Suggested commit message:

```bash
git add .
git commit -m "Add Queries Quality and Percentage solution and update progress"
git push origin main
````

Tomorrow we'll start the **Highest / Lowest / Top-N** pattern, which is one of the most frequently asked SQL topics in placements. 🚀
