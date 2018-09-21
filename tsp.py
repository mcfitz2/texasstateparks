import time, re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options


locations = [{"latitude":32.240614, "longitude":-99.879079, "park_id":609, "park_name":'ABILENE SP'}, 
{"latitude":33.231561, "longitude":-94.267788, "park_id":347, "park_name":'ATLANTA SP'}, 
{"latitude":30.944829, "longitude":-103.785147, "park_id":451, "park_name":'BALMORHEA SP'}, 
{"latitude":29.269859, "longitude":-103.755349, "park_id":283, "park_name":'BARTON WARNOCK VISITOR CENTER'}, 
{"latitude":30.11412, "longitude":-97.25987, "park_id":511, "park_name":'BASTROP SP'}, 
{"latitude":29.755968, "longitude":-95.08974, "park_id":607, "park_name":'BATTLESHIP TEXAS SHS'}, 
{"latitude":26.186987, "longitude":-98.381888, "park_id":38, "park_name":'BENTSEN RIO GRANDE SP'}, 
{"latitude":29.418054, "longitude":-103.989751, "park_id":602, "park_name":'BIG BEND RANCH SP'}, 
{"latitude":32.229574, "longitude":-101.48968, "park_id":437, "park_name":'BIG SPRING SP'}, 
{"latitude":30.096782, "longitude":-98.43459, "park_id":591, "park_name":'BLANCO SP'}, 
{"latitude":33.544812, "longitude":-96.145404, "park_id":280, "park_name":'BONHAM SP'}, 
{"latitude":29.380798, "longitude":-95.594658, "park_id":122, "park_name":'BRAZOS BEND SP'}, 
{"latitude":30.090088, "longitude":-97.188874, "park_id":86, "park_name":'BUESCHER SP'}, 
{"latitude":32.691647, "longitude":-94.17923, "park_id":54, "park_name":'CADDO LAKE SP'}, 
{"latitude":34.439742, "longitude":-101.051622, "park_id":603, "park_name":'CAPROCK CANYONS SP'}, 
{"latitude":32.607341, "longitude":-96.996281, "park_id":356, "park_name":'CEDAR HILL SP'}, 
{"latitude":28.473589, "longitude":-98.34845, "park_id":386, "park_name":'CHOKE CANYON SP'}, 
{"latitude":32.266556, "longitude":-97.55685, "park_id":405, "park_name":'CLEBURNE SP'}, 
{"latitude":31.049131, "longitude":-98.483592, "park_id":475, "park_name":'COLORADO BEND SP'}, 
{"latitude":33.345489, "longitude":-95.668599, "park_id":100, "park_name":'COOPER LAKE SP DOCTORS CREEK'}, 
{"latitude":33.28966, "longitude":-95.652852, "park_id":96, "park_name":'COOPER LAKE SP SOUTH SULPHUR'}, 
{"latitude":34.107097, "longitude":-99.748691, "park_id":170, "park_name":'COPPER BREAKS SP'}, 
{"latitude":33.010936, "longitude":-94.693999, "park_id":223, "park_name":'DAINGERFIELD SP'}, 
{"latitude":30.599926, "longitude":-103.925934, "park_id":241, "park_name":'DAVIS MOUNTAINS SP'}, 
{"latitude":29.929326, "longitude":-100.942938, "park_id":164, "park_name":'DEVILS RIVER SNA'}, 
{"latitude":30.037411, "longitude":-100.113774, "park_id":147, "park_name":'DEVILS SINKHOLE SNA'}, 
{"latitude":32.251511, "longitude":-97.81219, "park_id":18, "park_name":'DINOSAUR VALLEY SP'}, 
{"latitude":33.814601, "longitude":-96.60951, "park_id":149, "park_name":'EISENHOWER SP'}, 
{"latitude":30.505381, "longitude":-98.819844, "park_id":195, "park_name":'ENCHANTED ROCK SNA'}, 
{"latitude":26.126411, "longitude":-97.956518, "park_id":674, "park_name":'ESTERO LLANO GRANDE SP'}, 
{"latitude":31.761169, "longitude":-96.070204, "park_id":515, "park_name":'FAIRFIELD LAKE SP'}, 
{"latitude":26.579705, "longitude":-99.142373, "park_id":518, "park_name":'FALCON SP'}, 
{"latitude":30.483045, "longitude":-95.983961, "park_id":39, "park_name":'FANTHORP INN SHS'}, 
{"latitude":31.189837, "longitude":-95.98588, "park_id":46, "park_name":'FORT BOGGY SP'}, 
{"latitude":29.542525, "longitude":-104.326809, "park_id":23, "park_name":'FORT LEATON SHS'}, 
{"latitude":31.569973, "longitude":-96.543936, "park_id":135, "park_name":'FORT PARKER SP'}, 
{"latitude":33.20615, "longitude":-98.156969, "park_id":440, "park_name":'FORT RICHARDSON SP AND SHS'}, 
{"latitude":31.905102, "longitude":-106.498015, "park_id":176, "park_name":'FRANKLIN MOUNTAINS SP'}, 
{"latitude":29.190784, "longitude":-94.95953, "park_id":236, "park_name":'GALVESTON ISLAND SP'}, 
{"latitude":29.590745, "longitude":-99.739754, "park_id":439, "park_name":'GARNER SP'}, 
{"latitude":28.656494, "longitude":-97.385362, "park_id":72, "park_name":'GOLIAD SP'}, 
{"latitude":28.128064, "longitude":-96.98838, "park_id":524, "park_name":'GOOSE ISLAND SP'}, 
{"latitude":29.571323, "longitude":-98.753246, "park_id":277, "park_name":'GOVERNMENT CANYON SNA'}, 
{"latitude":29.876074, "longitude":-98.504058, "park_id":225, "park_name":'GUADALUPE RIVER SP'}, 
{"latitude":29.631061, "longitude":-99.191801, "park_id":228, "park_name":'HILL COUNTRY SNA'}, 
{"latitude":31.917325, "longitude":-106.043785, "park_id":259, "park_name":'HUECO TANKS SP AND SHS'}, 
{"latitude":30.620676, "longitude":-95.527726, "park_id":369, "park_name":'HUNTSVILLE SP'}, 
{"latitude":30.592877, "longitude":-103.943596, "park_id":145, "park_name":'INDIAN LODGE'}, 
{"latitude":30.739195, "longitude":-98.370808, "park_id":279, "park_name":'INKS LAKE SP'}, 
{"latitude":29.612137, "longitude":-100.448173, "park_id":529, "park_name":'KICKAPOO CAVERN SP'}, 
{"latitude":33.758069, "longitude":-98.395571, "park_id":178, "park_name":'LK ARROWHEAD SP'}, 
{"latitude":33.049185, "longitude":-95.092292, "park_id":615, "park_name":'LK BOB SANDLIN SP'}, 
{"latitude":31.858162, "longitude":-99.029785, "park_id":545, "park_name":'LK BROWNWOOD SP'}, 
{"latitude":27.545412, "longitude":-99.440528, "park_id":85, "park_name":'LK CASA BLANCA INTERNATIONAL SP'}, 
{"latitude":32.324143, "longitude":-100.932756, "park_id":367, "park_name":'LK COLORADO CITY SP'}, 
{"latitude":28.063249, "longitude":-97.873889, "park_id":105, "park_name":'LK CORPUS CHRISTI SP'}, 
{"latitude":30.647915, "longitude":-95.004646, "park_id":401, "park_name":'LK LIVINGSTON SP'}, 
{"latitude":32.832393, "longitude":-98.030831, "park_id":219, "park_name":'LK MINERAL WELLS SP'}, 
{"latitude":30.310412, "longitude":-96.628643, "park_id":496, "park_name":'LK SOMERVILLE SP BIRCH CREEK'}, 
{"latitude":30.289681, "longitude":-96.663069, "park_id":504, "park_name":'LK SOMERVILLE SP NAILS CREEK'}, 
{"latitude":32.844839, "longitude":-95.999885, "park_id":463, "park_name":'LK TAWAKONI SP'}, 
{"latitude":31.927534, "longitude":-97.36204, "park_id":104, "park_name":'LK WHITNEY SP'}, 
{"latitude":29.851282, "longitude":-97.693625, "park_id":601, "park_name":'LOCKHART SP'}, 
{"latitude":29.826021, "longitude":-99.586952, "park_id":264, "park_name":'LOST MAPLES SNA'}, 
{"latitude":30.237728, "longitude":-98.626319, "park_id":563, "park_name":'LYNDON B. JOHNSON SP AND SHS'}, 
{"latitude":32.277951, "longitude":-94.573318, "park_id":388, "park_name":'MARTIN CREEK LAKE SP'}, 
{"latitude":30.842882, "longitude":-94.171966, "park_id":398, "park_name":'MARTIN DIES JR. SP'}, 
{"latitude":30.18058, "longitude":-97.722127, "park_id":83, "park_name":'MCKINNEY FALLS SP'}, 
{"latitude":31.889266, "longitude":-97.702365, "park_id":570, "park_name":'MERIDIAN SP'}, 
{"latitude":31.548434, "longitude":-95.240357, "park_id":594, "park_name":'MISSION TEJAS SP'}, 
{"latitude":31.65764, "longitude":-102.831223, "park_id":616, "park_name":'MONAHANS SANDHILLS SP'}, 
{"latitude":29.888953, "longitude":-96.875351, "park_id":619, "park_name":'MONUMENT HILL/KREISCHE BREWERY'}, 
{"latitude":31.324698, "longitude":-97.469686, "park_id":384, "park_name":'MOTHER NEFF SP'}, 
{"latitude":27.684299, "longitude":-97.176746, "park_id":433, "park_name":'MUSTANG ISLAND SP'}, 
{"latitude":29.586683, "longitude":-97.576914, "park_id":503, "park_name":'PALMETTO SP'}, 
{"latitude":34.907317, "longitude":-101.642426, "park_id":588, "park_name":'PALO DURO CANYON SP'}, 
{"latitude":30.299393, "longitude":-98.243377, "park_id":185, "park_name":'PEDERNALES FALLS SP'}, 
{"latitude":32.873976, "longitude":-98.554457, "park_id":210, "park_name":'POSSUM KINGDOM SP'}, 
{"latitude":32.364436, "longitude":-95.992895, "park_id":127, "park_name":'PURTIS CREEK SP'}, 
{"latitude":33.362765, "longitude":-97.016783, "park_id":269, "park_name":'RAY ROBERTS LK SP ISLE DU BOIS'}, 
{"latitude":33.395298, "longitude":-97.050908, "park_id":217, "park_name":'RAY ROBERTS LK SP JOHNSON BRANCH'}, 
{"latitude":25.987, "longitude":-97.564, "park_id":275, "park_name":'RESACA DE LA PALMA SP'}, 
{"latitude":31.466649, "longitude":-100.536018, "park_id":404, "park_name":'SAN ANGELO SP'}, 
{"latitude":29.738206, "longitude":-95.077949, "park_id":406, "park_name":'SAN JACINTO BATTLEGROUND SHS'}, 
{"latitude":29.679497, "longitude":-94.025391, "park_id":434, "park_name":'SEA RIM SP'}, 
{"latitude":29.7001, "longitude":-101.313058, "park_id":448, "park_name":'SEMINOLE CANYON SP AND SHS'}, 
{"latitude":29.868455, "longitude":-95.168196, "park_id":460, "park_name":'SHELDON LAKE SP'}, 
{"latitude":30.446816, "longitude":-99.805268, "park_id":487, "park_name":'SOUTH LLANO RIVER SP'}, 
{"latitude":29.818394, "longitude":-96.110549, "park_id":560, "park_name":'STEPHEN F. AUSTIN SP'}, 
{"latitude":32.481326, "longitude":-95.295037, "park_id":175, "park_name":'TYLER SP'}, 
{"latitude":30.255164, "longitude":-94.162737, "park_id":600, "park_name":'VILLAGE CREEK SP'}, 
{"latitude":30.323581, "longitude":-96.154854, "park_id":327, "park_name":'WASHINGTON ON THE BRAZOS SHS'}, 
{"latitude":31.812314, "longitude":-106.483857, "park_id":506, "park_name":'WYLER AERIAL TRAMWAY '}]
def parseJS(s):
	r = re.compile(r'javascript\:return ShowCalendarSearch\(\'(\d+)\',\'.+\',\'.+\'\);')
	m = re.match(r, s)
	if m:
		return m.group(1)
	else:
		return None
def park_location(park_id):
	for park in locations:
		if park_id == park["park_id"]:
			return park
	return {"latitude":None, "longitude":None}


chrome_options = Options()  
chrome_options.add_argument("--headless")  
driver = webdriver.Chrome('/Users/micahfitzgerald/Dropbox/Code/TSP/chromedriver', chrome_options=chrome_options)  # Optional argument, if not specified will search path.
driver.get('https://texas.reserveworld.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('ctl00$TopMenu1$btnContinueMenu')
search_box.submit()
time.sleep(5) # Let the user actually see something!


park_select = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$lstParks'))
park_values = [int(i) for i in [opt.get_attribute("value") for opt in park_select.options]]
for park_id in park_values[24:]:
	park_select = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$lstParks'))
	park_select.deselect_all()
	park_select.select_by_value(str(park_id))
	driver.find_element_by_name('ctl00$ContentPlaceHolder1$btnSearch').click()
	loc = park_location(park_id)
	time.sleep(10)
	try:
		table = driver.find_element_by_id("ctl00_ContentPlaceHolder1_ParksList")
		info = []
		for row in table.find_elements_by_tag_name('tr'):
			cell = row.find_elements_by_tag_name("td")
			vals = [ i or "" for i in [c.text if (c and c.text and len(c.text) > 0) else c.get_attribute('onclick') for c in cell ]]
			if vals:
				#print(vals)
				info.append({"location":{"lat":loc["latitude"], "lng":loc["longitude"]}, "park_name":vals[0], "park_id":park_id, "camp_type":vals[1], "camp_name":vals[2], "camp_id":vals[3]})

		for index in range(len(info)):
			if not info[index]["park_name"]:
				info[index]["park_name"] = info[index-1]["park_name"]
			if info[index]["camp_id"]:
				info[index]["camp_id"] = parseJS(info[index]["camp_id"])
		########################
		### Push camp data to DB



		#########################
	except NoSuchElementException:
		err = driver.find_element_by_id("ctl00_ContentPlaceHolder1_LblErrorMessage")
		pass

driver.quit()