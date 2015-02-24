Let's say I have two tables, and I want to make one function in python that compares them and produce one list from the combination of both of them based on the second column, but without duplicates.

Table1.csv
ra,br
ah,b
ai,c
aa,d

Table2.csv
ra,b
ah,r
ai,a
za,d

My code:

from pandas import DataFrame, read_csv
import pandas as pd

# imported the two lists
Table1 = pd.read_csv("Table1.csv", header = None)
Table2 = pd.read_csv("Table2.csv", header = None)

final = []
for row1 in Table1[1]:
	for row2 in Table2[1]:
		if row1 == row2:
			print("a")
			break
		else:
			final.append(row2)
			print("b")
	final.append(row1)
		

The output I am having:
b
b
b
b
a
b
b
b
b
b
b
b
a

Therefore the problem with this function is in the "else" part, which is printing each item of Table2 for every combination. How could I constrain this function to print each item only one time?
