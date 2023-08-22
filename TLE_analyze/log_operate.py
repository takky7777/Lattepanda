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


    def pushData(self, data):
        with open(self.SC, mode = 'a') as f:
            payload = ",".join(data)
            f.writelines(payload + '\n')


    def getTLE(self, NORAD):
        with open(self.TLE, mode = 'r') as f:
            raw = f.readlines()
            maxr = len(raw)
            #find matching NORAD
            for row in reversed(range(maxr)):
                vals = raw[row].split(",")
                if vals[6] == NORAD:
                    break
            #get TLE val
            NORAD = vals[6]
            name = vals[7]
            line1 = vals[8]
            line2 = vals[9]
        return [NORAD, name, line1, line2]


    def settingImport(self):
        with open(self.CONF, 'r') as f:
            setting = []
            raw = f.readlines()[len(f.readlines())]
            setting = raw.split(",")
        return setting
