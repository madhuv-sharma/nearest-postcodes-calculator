from flask import Flask, redirect, request, jsonify
from flask_cors import CORS, cross_origin
from flask_ngrok import run_with_ngrok
from math import *
import json
import pandas as pd


app = Flask(__name__)
cors = CORS(app)
run_with_ngrok(app)
app.config['JSON_SORT_KEYS'] = False


def error_handle(error_message, code=1, status=500, mimetype='application/json'):
    return Response(json.dumps({"success" : False, "message": error_message, "data": { "modelname": "" }, "code": code }), status=status, mimetype=mimetype)


def success_handle(output, status=200, mimetype='application/json'):
    return Response(output, status=status, mimetype=mimetype)


def dist(lat1, lon1, lat2, lon2):
	lat1, lon1, lat2, lon2 =  map(radians, [lat1, lon1, lat2, lon2])
	c = 2 * asin(sqrt(sin((lat2-lat1)/2)**2 + cos(lat1) * cos(lat2) * sin((lon2-lon1)/2)**2)) 
	r = 6371.137
	return c * r


def getClosestLocs(lat1, lat2, di):
	data=[]
	for row in csv_reader:
		try:
			row[5]=dist(lat1, lon1, float(row[3]), float(row[4]))
		except ValueError:
			continue
		data.append(row)
	data=sorted(data, key=lambda abc:abc[5])
	for row in data:
		if lc<=10:
			if lc==0:
				row[1]=row[1].upper()
				row[2]=row[2].upper()
			print(row)
		lc+=1


@app.route('/')
def welcome():
	return 'Welcome!'


@app.route('/index')
def index():
	return '''
	/api/calc to find nearest 10 Indian Postal Codes
	'''


@app.route("/api/calc", methods=['POST', 'GET'])
@cross_origin()
def calc():
	if request.method == 'POST':
		code = ['110001', '110002', '110003', '110004', '110005', '110006', '110007', '110008', '110010', '110011', '110012', '110013', '110014', '110015', '110016', '110017', '110018', '110019', '110020', '110021', '110022', '110023', '110024', '110025', '110026', '110027', '110028', '110029', '110030', '110031', '110032', '110033', '110034', '110035', '110036', '110037', '110038', '110039', '110040', '110041', '110042', '110043', '110044', '110045', '110046', '110047', '110048', '110049', '110051', '110052', '110053', '110054', '110055', '110056', '110057', '110058', '110059', '110060', '110061', '110062', '110063', '110064', '110065', '110066', '110067', '110070', '110071', '110072', '110073', '110081', '110082', '110083', '110084', '110088', '110091', '110092', '110093', '110094', '110096', '121001', '121002', '121005', '121006', '121007', '121101', '121102', '122001', '122005', '122015', '122016', '122050', '122101', '122103', '122104', '122105', '122106', '122107', '122108', '122109', '122211']
		place = ['Connaught Place', 'Darya Ganj', 'Aliganj', 'Rashtrapati Bhawan', 'Lower Camp Anand Parbat', 'Bara Tooti', 'Birla Lines', 'Patel Nagar', 'Delhi Cantt', 'Nirman Bhawan', 'Inderpuri', 'Hazrat Nizamuddin', 'Jangpura', 'Zakhira', 'Hauz Khas', 'Malviya Nagar', 'Vishnu Garden', 'Nehru Place', 'Flatted Factories Complex', 'Malcha Marg', 'Postal Saving Bureau', 'Kidwai Nagar', 'Lajpat Nagar', 'Jamia Nagar', 'Punjabi Bagh', 'J-6 Block Rajouri Garden', 'Naraina Industrial Estate', 'Himayunpur Extn', 'T B Hospital', 'Gandhi Nagar', 'Shahdara', 'Adarsh Nagar', 'Pitampura', 'Inderlok', 'Alipur', 'Gurgaon Road', 'A F Rajokari', 'Bawana', 'Sanoth', 'Nangloi', 'Badli', 'Najafgarh', 'Badarpur T P Station', 'Palam Enclave', 'Nangal Rava', 'Arjan Garh', 'Kailash', 'Andrews Ganj', 'Azad Nagar', 'Wazirpur Phase Iii', 'Zafrabad', 'Civil Lines', 'Paharganj', 'Shakurbasti', 'Munirka', 'Janakpuri', 'Uttam Nagar', 'New Rajinder Nagar', 'Bijwasan', 'Hamdard Nagar', 'Paschim Vihar', 'Hari Nagar Be Block', 'East Of Kailash', 'R K Puram', 'D D A Munirka', 'Vasant Kunj', 'Chhawla', 'Jharoda Kalan', 'Ujwa', 'Kanjhawala', 'Khera Kalan', 'Mangolpuri Block A', 'Kutubgarh', 'Shalimar Bagh', 'Himmatpuri', 'Shakarpur', 'Nand Nagri A Block', 'Gokulpuri', 'Bhajanpura', 'Faridabad', 'Faridabad', 'Faridabad Sector 22', 'Industrial Estate', 'Faridabad', 'Tigaon', 'Palwal', 'Gurgaon Kutchery', 'Air Force Gurgaon', 'Gurgaon Palampur Road', 'Dundahera', 'Manesar', 'Badshahpur', 'Sohna(Gurgaon)', 'Ferozepur Jhirka', 'Taura', 'Dharuhera', 'Nuh', 'Nagina', 'Daulatabad (Gurgaon)', 'Palmar']
		state = ['New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'New Delhi', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Uttar Pradesh', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana', 'Haryana']
		latitude = ['28.6327', '28.6352', '28.5916', '28.6142', '28.6557', '28.6611', '28.6786', '28.6482', '28.5929', '28.6041', '28.6282', '28.5891', '28.5793', '28.6589', '28.5472', '28.5279', '28.6436', '28.5347', '28.5388', '28.5884', '28.5641', '28.5748', '28.5684', '28.5621', '28.6683', '28.6465', '28.6318', '28.5647', '28.4957', '28.6508', '28.6866', '28.7236', '28.693', '28.6738', '28.8222', '28.5441', '28.5132', '28.8002', '28.8349', '28.6697', '28.7506', '28.6117', '28.5007', '28.5966', '28.6041', '28.4718', '28.5479', '28.5624', '28.6569', '28.6895', '28.6757', '28.6904', '28.6456', '28.6812', '28.5616', '28.6217', '28.6218', '28.6354', '28.5351', '28.51', '28.6699', '28.6259', '28.5678', '28.5674', '28.5433', '28.5124', '28.5613', '28.6838', '28.5709', '28.7344', '28.7762', '28.6925', '28.7579', '28.7122', '28.6079', '28.6362', '28.6974', '28.7157', '28.5953', '28.39', '28.4194', '28.37', '28.3734', '28.389', '28.3799', '28.1373', '28.4555', '28.4362', '28.4964', '28.5079', '28.3555', '28.3637', '28.1739', '27.7465', '28.23355', '28.20552', '28.0775', '27.9395', '28.41443', '28.09']
		longitude = ['77.2196', '77.2469', '77.2318', '77.196', '77.1875', '77.2346', '77.1916', '77.1641', '77.1218', '77.2116', '77.1494', '77.2568', '77.2585', '77.1458', '77.2003', '77.2089', '77.087', '77.2602', '77.2754', '77.1859', '77.1737', '77.1991', '77.2416', '77.2857', '77.1365', '77.1169', '77.1388', '77.2003', '77.1665', '77.2676', '77.2922', '77.1757', '77.1351', '77.1643', '77.1718', '77.116', '77.1093', '77.0355', '77.0899', '77.0569', '77.142', '76.9787', '77.3152', '77.0826', '77.098', '77.1315', '77.2376', '77.2231', '77.2823', '77.1754', '77.2596', '77.2275', '77.2111', '77.1211', '77.1559', '77.0883', '77.0558', '77.1857', '77.0566', '77.2355', '77.1069', '77.1143', '77.2616', '77.1873', '77.1683', '77.137', '77.0021', '76.9709', '76.9058', '77.011', '77.1002', '77.0884', '77.1998', '77.159', '77.3055', '77.2922', '77.3156', '77.278', '77.3119', '77.298', '77.3669', '77.2693', '77.3353', '77.3181', '77.4358', '77.4243', '77.0219', '77.0305', '77.0593', '77.0752', '76.941', '77.0219', '77.0795', '76.9413', '76.93231', '76.7953', '77.0334', '77.0334', '77.31521', '76.9567']
		di = {'code': code, "place": place, "state": state, "latitude": latitude, "longitude": longitude}
		try:
			if 'text' not in request.text :
				return error_handle('Please send image files.')
			pincode = request.text.get('text')
			f = 0
			for row in csv_reader:
				if int(row[0]) == pincode :
					lat1 = float(row[3])
					lon1 = float(row[4])
					f = 1
					break
			if f == 1 :
				getClosestLocs(lat1, lon1, di)
			else:
				print("Sorry, Pin Code is Not in the Database!") 
		except Exception as e:
			response = {
			'success': False,
			'status code': 500,
			'message': str(e),
			}
			resp = jsonify(response)
			return resp 
		return

	return '''
	<!DOCTYPE HTML>
	<title></title>
	<h1>Enter Postal Code whose nearest Locations are to be found</h1>
	<form method=post enctype=multipart/form-data>
	<input type=text name=text>
	<input type=submit value=Upload>
	</form>
	'''


app.run(debug=True)