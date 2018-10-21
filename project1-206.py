#project 1
#jazmyn rivera
#F18

import os
import filecmp
from dateutil.relativedelta import *
from datetime import date


def getData(file):
# get a list of dictionary objects from the file
#Input: file name
#Output: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	infile = open(file, "r")
	dataList = []
	headers = infile.readline()
	lines = infile.readlines()
	for line in lines:
		values = line.split(",")
		first = values[0]
		last = values[1]
		email = values[2]
		grade = values[3]
		dob = values[4]

		dictionaryObject = {}

		dictionaryObject["First"] = first
		dictionaryObject["Last"] = last
		dictionaryObject["Email"] = email
		dictionaryObject["Grade"] = grade
		dictionaryObject["Dob"] = dob

		dataList.append(dictionaryObject)

	infile.close()
	return dataList

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	sort = sorted(data, key=lambda d: d[col], reverse=False)
	return sort[0]["First"] + " " + sort[0]["Last"]

def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	senior = 0
	junior = 0
	sophomore = 0
	freshman = 0
	for dictionary in data:
		if dictionary["Grade"] == "Senior":
			senior += 1
		if dictionary["Grade"] == "Junior":
			junior += 1
		if dictionary["Grade"] == "Sophomore":
			sophomore +=1
		if dictionary["Grade"] == "Freshman":
			freshman += 1
	histogramList = [('Senior', senior), ('Junior', junior), ('Sophomore', sophomore), ('Freshman', freshman)]

	sort = sorted(histogramList, key=lambda d: d[1], reverse=True)
	return sort
	
def findMonth(a):
# Find the most common birth month from this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	monthCounters = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0}
	for dictObject in a:
		date = dictObject["Dob"].split("/")
		month = date[0]
		monthCounters[month] = monthCounters[month] + 1
	maxMonths = max(monthCounters, key=lambda i: monthCounters[i])
	return int(maxMonths)

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as first,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	outfile = open(fileName,"w")
	sort = sorted(a, key=lambda d: d[col], reverse=False)
	for item in sort:
		outfile.write(item["First"] + ",")
		outfile.write(item["Last"] + ",")
		outfile.write(item["Email"] + ",")
		outfile.write("\n")
	outfile.close()
	

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	ageTotal = 0
	ageCounter = 0

	for dictionary in a:
		dateList =dictionary["Dob"].split("/")
		year = dateList[2]
		age = 2018 - int(year)
		ageTotal += age
		ageCounter += 1

	return(int(ageTotal / ageCounter))


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
