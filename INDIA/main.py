# import numpy as np # Can be used instead of 'math' module for faster calculations in 'dist' function
from math import *
import csv

'''
Based on Haversine Formula, distance between two points whose geocoordinates are (Lat1,Lon1) and (Lat2,Lon2) is given as 
2r*arcsin(sqrt(sin^2((Lat2-Lat1)/2)+cos(Lat1)*cos(Lat2)+sin^2((Lon2-Lon1)/2)))
'''

def dist(lat1, lon1, lat2, lon2):
	lat1, lon1, lat2, lon2 =  map(radians, [lat1, lon1, lat2, lon2])
	c = 2 * asin(sqrt(sin((lat2-lat1)/2)**2 + cos(lat1) * cos(lat2) * sin((lon2-lon1)/2)**2)) 
	r = 6371.137	#Radius of Earth at equator in kilometers
	return c * r

#Finding 10 Closest Pin Codes from the Given Pin Code
def closestLocations(lat1, lat2, in_file_loc):
	data=[]
	with open(in_file_loc, "r") as csv_file:
		csv_reader=csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			try:
				row[5]=dist(lat1, lon1, float(row[3]), float(row[4]))
			except ValueError: # For entries having no geocoordinates
				continue
			data.append(row)

		data=sorted(data, key=lambda abc:abc[5]) # Sorting the data in ascending order of distance

		print("Do you want to save the output data in a file? (Enter y/n)\n")
		ch=input()
		if ch=='y' :
			print("Output Database Location :\n")
			out_file_loc=input()
			try:
				with open(out_file_loc, "w", newline='') as f:
					csv_writer=csv.writer(f)
					lc=0
					for row in data:
						if lc<=10:
							if lc==0:
								row[1]=row[1].upper()
								row[2]=row[2].upper()
							csv_writer.writerow(row)
						lc+=1
			except FileNotFoundError :
				print("File not Found")
				sys.exit(1)
		elif ch!='n' :
			print("Taking it as a no")
		for row in data:
			if lc<=10:
				if lc==0:
					row[1]=row[1].upper()
					row[2]=row[2].upper()
				print(row)
			lc+=1

#Inputting File Location and Pin Code, checking whether they are valid, and calling the closestLocations function
def main():
	print("Input Database Location :\n")
	in_file_loc=input()
	try:
		with open(in_file_loc, "r") as csv_file:
			csv_reader=csv.reader(csv_file, delimiter=',')
			print("Enter Pin Code to find nearest locations - ")
			pincode=int(input())
			f=0
			next(csv_reader, None) 
			for row in csv_reader:
				if int(row[0]) == pincode :
					lat1=float(row[3])
					lon1=float(row[4])
					f=1
					break
			if f==1 :
				closestLocations(lat1, lon1, in_file_loc)
			else:
				print("Sorry, Pin Code is Not in the Database!") 
	except ValueError:
		print("Wrong Input")
	except FileNotFoundError :
		print("File not Found")

if __name__=='__main__':
	main()
