# Nearest Postal Codes Calculator

Using a variety of modules namely- bs4, csv, json, pandas and urllib, I had created a Database of over 11,000 Indian Pin Codes with their respective Geocoordinates, from 3 different sources, using web scraping. Initially, I downloaded a raw Database containing a list of Indian Pin Codes along with highly erroneous geocoordinates (with frequent repetition) from Github[1] (Source #1) I had scraped Nominatam's OpenStreetMap[2] (Source #2), which yielded correct[3] geo coordinates of more than 50% values. This wasn't satisfactory so I went ahead and designed a program which surfed Google[4] (Source #3) for geo coordinates and returned the result of Google's Featured Snippet. Using this method, I was able to get a separate database which was about 76% correct*. Finally, I had edited the "Featured Snippet Database" by replacing the 24% incorrect values by the respective ones from the "OSM Database". All in all, I could achieve an overall correct values' percentage of 94%, which can still be improved further, but manually.

Upon completion of the database, I had executed a code in Python, which gave the list of 10 nearest Pin Codes from the value entered, for which, I had used the Haversine formula and the knowledge of the database that I had created earlier.

Did the same for Canadian postal codes Database [5].



	[1]	https://github.com/sanand0/pincode/blob/master/data/IN.csv

	[2]	https://nominatim.openstreetmap.org/ui/search.html

	[3] 	The number of correct geo coordinates were found out by checking two main conditions:
		i 	If the geo coordinates were of a location within the range of India, ie. within 8°4'N - 37°6'N latitude and 68°7'E - 97°25'E longitude (to simply eliminate 			    such values and replace them)
		ii 	If condition i is satisfied, coordinates were rechecked to find whether they lie within their respective state boundaries (for such values, their 				counterparts were compared and action was taken accordingly)

	[4]	www.google.com

	[5]	https://www.serviceobjects.com/blog/free-zip-code-and-postal-code-database-with-geocoordinates/
