import csv
import json
import re
import urllib.request


def main():
	fields = []
	rows = []
	postal_codes = []
	with open('IN.csv', 'r') as inp_file:
		csv_reader = csv.reader(inp_file, delimiter=',')
		fields = next(csv_reader)
		for row in csv_reader:
			rows.append(row)
			postal_codes.append(re.findall('^IN/([0-9]+)', row[0]))
		zips = []
		for postal_code in postal_codes:
			for zip in postal code:
				zips.append(zip)
		i = 0
		with open("code.csv", 'w') as out_file:
			csv_writer = csv.writer(out_file, delimiter=',')
			for zip in zips:
				url = f"https://nominatim.openstreetmap.org/search.php?q={zip}&format=jsonv2"
				fhand = urllib.request.urlopen(url)
				data_json = json.loads(fhand.read())
				lat = [item.get("lat") for item in data_json]
				lon = [item.get("lon") for item in data_json]
				if len(lat) == 0:
					continue
				while i<len(lat):
					if 8.06666<=lat[i]<=37.1 and 68.11666<=lon[i]<=97.41667:
						coordinates = [lat[i], lon[i]]
						print(coordinates)
						csv_writer.writerow(coordinates)
						break
					i+=1


if __name__ == '__main__':
	main()