import os
from pymongo import MongoClient
import psutil
import numpy as np
import platform
import threading
import geocoder
import cpuinfo
from datetime import datetime
import requests
from uuid import getnode as get_mac
import ssl
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()
#MONGODB_URI = os.environ['MONGODB_URI']

# Connect to your MongoDB cluster:
client = MongoClient("mongodb://joshus:gEaxdmptTLkKHyhP@cluster0-shard-00-00.zky6k.mongodb.net:27017,cluster0-shard-00-01.zky6k.mongodb.net:27017,cluster0-shard-00-02.zky6k.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-gaba9t-shard-0&authSource=admin&retryWrites=true&w=majority", ssl = True, ssl_cert_reqs=ssl.CERT_NONE)

# List all the databases in the cluster:
#for db_info in client.list_database_names():
	#print(db_info)

db = client['co2_data']
collections = db.list_collection_names()
co2data = db['co2dataset']

db2 = client['VC_data']
collections = db2.list_collection_names()
vc_data = db2['VC Dataset']

seconds = 60
def get_cpu_data(): 
    CPU_usage = []
    #Input number of seconds over which you wish to measure CPU usage
    #tdp = int(input('What is the tdp of your system?'))
    vers = str(input('What is the version of the platform you are running on? (ex. 1.4.00.11161.)'))
    no_people = int(input('How many people are in the call?'))
    VC = str(input('What VC platform are you using?'))
    video = str(input('Video(yes/no)?'))
    vback = str(input('Virtual Background (yes/no)?'))

    if VC == 'TEAMS' or VC == 'teams' or VC == 'Microsoft Teams' or VC == 'Microsoft teams' or VC == 'microsoft teams' or VC == 'microsoft Teams':
        VC = 'Teams'
    if (VC =='Zoom' or VC == 'ZOOM') and platform.system() == 'Darwin':
        VC = 'zoom'
    if (VC =='zoom' or VC == 'ZOOM' or VC == ' zoom' or VC == ' Zoom' or VC == ' ZOOM') and platform.system() == 'Windows':
        VC = 'Zoom'

    try:
        pids = []
        pid = 0
        for proc in psutil.process_iter():
            if VC in proc.name():
                pids.append(proc.pid)
            if 'TeamsUpdater' in proc.name():
                pid = proc.pid
        
        if pid in pids:
            pids.remove(pid)
        print(VC, 'has',len(pids), 'different processes')
    except psutil.AccessDenied:
        print('There has been an error finding the VC process')
    
        
    #This tells us how many threads we will need
    CPU_usage1 = []
    CPU_usage2 = []
    CPU_usage3 = []
    CPU_usage4 = []
    CPU_usage5 = []
    CPU_usage6 = []
    CPU_usage7 = []
    CPU_usage8 = []
    CPU_usage9 = []
    CPU_usage10 = []
    
    def Process1():
        p = psutil.Process(pids[0])
        for i in range(seconds): 
            cpu = p.cpu_percent(1)
            CPU_usage1.append(cpu)
    
            #print('The CPU usage is: ', cpu,'%')
    
    def Process2():
        p = psutil.Process(pids[1])
        for i in range(seconds): 
            cpu = p.cpu_percent(1)
            CPU_usage2.append(cpu)
    
            #print('The CPU usage1 is: ', cpu1,'%')
    def Process3():
        p = psutil.Process(pids[2])
        for i in range(seconds): 
            cpu = p.cpu_percent(1)
            CPU_usage3.append(cpu)
    
            #print('The CPU usage is: ', cpu,'%')
    
    def Process4():
        p = psutil.Process(pids[3])
        for i in range(seconds): 
            cpu = p.cpu_percent(1)
            CPU_usage4.append(cpu)
    
            #print('The CPU usage1 is: ', cpu1,'%')
    def Process5():
        p = psutil.Process(pids[4])
        for i in range(seconds): 
            cpu = p.cpu_percent(1)
            CPU_usage5.append(cpu)
    
            #print('The CPU usage is: ', cpu,'%')
    
    def Process6():
        p = psutil.Process(pids[5])
        for i in range(seconds): 
            cpu = p.cpu_percent(1)
            CPU_usage6.append(cpu)
    
            #print('The CPU usage1 is: ', cpu1,'%')
            
    def Process7():
        p = psutil.Process(pids[6])
        for i in range(seconds): 
            cpu = p.cpu_percent(1)
            CPU_usage7.append(cpu)
    
            #print('The CPU usage is: ', cpu,'%')
    
    def Process8():
        p = psutil.Process(pids[7])
        for i in range(seconds): 
            cpu = p.cpu_percent(1)
            CPU_usage8.append(cpu)
    
            #print('The CPU usage1 is: ', cpu1,'%')
    def Process9():
        p = psutil.Process(pids[8])
        for i in range(seconds): 
            cpu = p.cpu_percent(1)
            CPU_usage9.append(cpu)
            
    def Process10():
        p = psutil.Process(pids[9])
        for i in range(seconds): 
            cpu = p.cpu_percent(1)
            CPU_usage10.append(cpu)
            
        
    
    t1 = threading.Thread(target=Process1, name='t1')
    if len(pids) >1:
        t2 = threading.Thread(target=Process2, name='t2') 
    if len(pids) >2:
        t3 = threading.Thread(target=Process3, name='t3')
    if len(pids) >3:
        t4 = threading.Thread(target=Process4, name='t4') 
    if len(pids) >4:
        t5 = threading.Thread(target=Process5, name='t5')
    if len(pids)>5:
        t6 = threading.Thread(target=Process6, name='t6') 
    if len(pids)>6:
        t7 = threading.Thread(target=Process7, name='t7')
    if len(pids)>7:
        t8 = threading.Thread(target=Process8, name='t8') 
    if len(pids)>8:
        t9 = threading.Thread(target=Process9, name='t9')
    if len(pids)>9:
        t10 = threading.Thread(target=Process10, name='t10')
    
    t1.start()
    if len(pids)>1:
        t2.start()
    if len(pids)>2:
        t3.start()
    if len(pids)>3:
        t4.start()
    if len(pids)>4:
        t5.start()
    if len(pids)>5:
        t6.start()
    if len(pids)>6:
        t7.start()
    if len(pids)>7:
        t8.start()
    if len(pids)>8:
        t9.start()
    if len(pids)>9:
        t10.start()

    
    t1.join()
    if len(pids)>1:
        t2.join()
    if len(pids)>2:
        t3.join()
    if len(pids)>3:
        t4.join()
    if len(pids)>4:
        t5.join()
    if len(pids)>5:
        t6.join()
    if len(pids)>6:
        t7.join()
    if len(pids)>7:
        t8.join()
    if len(pids)>8:
        t9.join()
    if len(pids)>9:
        t10.join()
    
    
    CPU_usage_mean1 = np.mean(CPU_usage1)
    if len(pids)>1:
        CPU_usage_mean2 = np.mean(CPU_usage2)
    if len(pids)>2:
        CPU_usage_mean3 = np.mean(CPU_usage3)
    if len(pids)>3:
        CPU_usage_mean4 = np.mean(CPU_usage4)
    if len(pids)>4:
        CPU_usage_mean5 = np.mean(CPU_usage5)
    if len(pids)>5:
        CPU_usage_mean6 = np.mean(CPU_usage6)
    if len(pids)>6:
        CPU_usage_mean7 = np.mean(CPU_usage7)
    if len(pids)>7:
        CPU_usage_mean8 = np.mean(CPU_usage8)
    if len(pids)>8:
        CPU_usage_mean9 = np.mean(CPU_usage9)
    if len(pids)>9:
        CPU_usage_mean10 = np.mean(CPU_usage10)
    
    
    average = CPU_usage_mean1 
    if len(pids)>1:
        average += CPU_usage_mean2
    if len(pids)>2:
        average += CPU_usage_mean3
    if len(pids)>3:
        average += CPU_usage_mean4
    if len(pids)>4:
        average += CPU_usage_mean5 
    if len(pids)>5:
        average += CPU_usage_mean6
    if len(pids)>6:
        average += CPU_usage_mean7 
    if len(pids)>7:
        average += CPU_usage_mean8 
    if len(pids)>8:
        average += CPU_usage_mean9
    if len(pids)>9:
        average += CPU_usage_mean10
    print('The cpu usage is', average, '%')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    
    g = geocoder.ip('me')
    city = g.city
    country_loc = g.country

    print('Location:', city,',', country_loc)
    print('VC tested:', VC)
    print('VC version:', vers)
    OS = os.name
    system = platform.system()
    release = platform.release()

    print('The OS is',os.name, ', the system is', platform.system(),', the release is', platform.release())

    #print(platform.platform())

    brand = cpuinfo.get_cpu_info()['brand_raw']
    print('Processor:',brand)
     
    mac = get_mac()
     
    return average, city, country_loc, VC, vers, brand, mac, OS, system, release, dt_string, no_people,video, vback

print('The following script will run over 60 seconds')

average, city, country_loc, VC, vers, brand, mac, OS, system, release, dt_string, no_people, video, vback = get_cpu_data()




url = f'https://api.co2signal.com/v1/latest?countryCode={country_loc}'
myapitoken = '1bce54fa25d791fb'
headers = {'Accept': 'application/json', 'auth-token': myapitoken}


response = requests.get(url, headers = headers)
output = response.json()['data']['carbonIntensity']

print('The carbon intensity of', country_loc, 'is:',output, 'gCO2eq/kWh')

item_1 = {
"VC" : {
        "vc_name" : VC,
        "vc_version" : vers,
        "video" : video,
        "virtual_back" : vback,
        },
"date" : dt_string,
"cpu_info" : {
    "no_of_users" : no_people,
    "no_of_secs" : seconds,
    "cpu_usage" : average,
    },
"location" : {
    "Country" : country_loc,
    "City" : city,
    "carb_inten" : output,
    },
"device_info" : {
    "processor" : brand,
    "os" : OS,
    "system" : system,
    "release" : release,
    "machine_id" : mac,
    },
}

vc_data.insert_one(item_1)
