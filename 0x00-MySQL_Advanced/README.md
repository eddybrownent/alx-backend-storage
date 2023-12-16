0x00. MySQL advanced
Back-end
SQL
MySQL

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to create tables with constraints
How to optimize queries by adding indexes
What is and how to implement stored procedures and functions in MySQL
What is and how to implement views in MySQL
What is and how to implement triggers in MySQL

More Info
Comments for your SQL file:
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
Use “container-on-demand” to run MySQL
Ask for container Ubuntu 18.04 - Python 3.7
Connect via SSH
Or via the WebTerminal
In the container, you should start MySQL before playing with it:More Info
Comments for your SQL file:
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
Use “container-on-demand” to run MySQL
Ask for container Ubuntu 18.04 - Python 3.7
Connect via SSH
Or via the WebTerminal
In the container, you should start MySQL before playing with it
