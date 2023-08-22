import json
import os
from pathlib import Path
import times

#fetch sources
time = times.times()
cd = Path.cwd()


class logOp:
    def __init__(self):
        #get path for GSSdata.xlsx
        absolute_path = os.path.dirname(__file__)
        LATTEPANDA = Path(absolute_path).parent
        LOG = os.path.join(LATTEPANDA, "GSSdata")
        self.TLE = os.path.join(LOG, "TLE.json")
        self.SC = os.path.join(LOG, "SAT_COORDS.json")
        self.CONF = os.path.join(LOG, "GSE_config.json")


    def pushData(self, data):
        with open(self.SC) as f:
            dic = json.load(f)
            elms = len(dic)

        print("hoge,",data)
        #fetch time
        c_time = time.getTime('all')


        dic[elms + 1] = {
            "Time":{
                "Year":c_time[0],
                "Month":c_time[1],
                "Day":c_time[2],
                "Hour":c_time[3],
                "Minute":c_time[4],
                "Second":c_time[5]
            },
            "NORAD":data[0],
            "COORDS":{
                "LAT":data[1],
                "LONG":data[2],
                "ELEV":data[3],
                "AZ":data[4],#Azimuth
                "ALT":data[5],#Altitude(仰角)
                "RV":data[6],#Range Velocity(相対速度)
                "DIST":data[7]
            }
        }

        with open(self.SC, mode = 'w') as f:
            json.dump(dic, f, indent=4)


    def getTLE(self, NORAD):
        with open(self.TLE, mode = 'r') as f:
            dic = json.load(f)
            elms = len(dic)

        for row in reversed(range(1, elms + 1)):
            print(row, str(NORAD), dic[str(row)]["TLE"]["NORAD ID"])
            #find matching NORAD
            if dic[str(row)]["TLE"]["NORAD ID"] == str(NORAD):
                break
            #get TLE val
        NORAD = dic[str(row)]["TLE"]["NORAD ID"]
        name = dic[str(row)]["TLE"]["LINE 0"]
        line1 = dic[str(row)]["TLE"]["LINE 1"]
        line2 = dic[str(row)]["TLE"]["LINE 2"]
        print(NORAD, name, line1, line2)
        return [NORAD, name, line1, line2]


    def ConfImport(self):
        with open(self.CONF, 'r') as f:
            dic = json.load(f)
        setting = [dic['NORAD'], dic['LAT'], dic['LONG'], dic['ALT']]
        return setting
