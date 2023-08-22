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


    def pushTLE(self, NORAD, tle):
        with open(self.TLE) as f:
            dic = json.load(f)
            elms = len(dic)

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
            "TLE":{
                "NORAD ID":str(NORAD),
                "LINE 0":tle[0],
                "LINE 1":tle[1],
                "LINE 2":tle[2]
            }
        }

        with open(self.TLE, mode='w') as f:
            json.dump(dic, f, indent=4)
            #json.dump(dic, self.TLE, indent=4, seperators=(",",": "))


    def ConfUpdate(self, NORAD, LAT, LONG, ALT):
        dic = {
            "NORAD":NORAD,
            "LAT":LAT,
            "LONG":LONG,
            "ALT":ALT
        }
        with open(self.CONF, 'w') as f:
            json.dump(dic, f, indent=4)


    def ConfImport(self):
        with open(self.CONF, 'r') as f:
            dic = json.load(f)
        setting = [dic['NORAD'], dic['LAT'], dic['LONG'], dic['ALT']]
        return setting
    
