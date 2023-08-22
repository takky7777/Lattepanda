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
        self.TLE = os.path.join(LOG, "TLE.log")
        self.SC = os.path.join(LOG, "SAT_COORDS.log")
        self.CONF = os.path.join(LOG, "GSE_config.log")


    def pushTLE(self, NORAD, tle):
        with open(self.TLE, mode='a') as f:
            #fetch time
            c_time = time.getTime('all')
            #compress? data
            data = c_time
            data.append(str(NORAD))
            data.append(tle[0])
            data.append(tle[1])
            data.append(tle[2])
            opt_data = ''
            for e in data:
                opt_data += e
                opt_data += ","
            opt_data = opt_data[:len(opt_data) - 1]
            #data push
            f.writelines(opt_data + "\n")


    def settingImport(self):
        with open(self.CONF, 'r') as f:
            setting = []
            raw = f.readlines()[len(f.readlines())]
            setting = raw.split(",")
        return setting