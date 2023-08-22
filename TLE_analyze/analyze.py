import ephem
from math import degrees as deg
import json_operate
import times

logop = json_operate.logOp()
t = times.times()

class ep:
    def __init__(self):
        pass

    def tleFromSheet(self, NORAD):
        tle = logop.getTLE(NORAD)   #fetch tle
        if tle == None:#in case empty
            print("ERROR	:getTLE FAULT")
            return 0
        #load tle
        self.tle_norad = tle[0]
        self.tle_name = tle[1]
        self.tle_line1 = tle[2]
        self.tle_line2 = tle[3]

    def analize(self, lat='37.1322056', lon='140.7658389', elevation=76):
        # set observer inform
        GST = ephem.Observer()
        GST.lat, GST.lon, GST.elevation = lat, lon, elevation
        c_time = t.getTime('all')
        GST.date = t.getTime('time')

        # TLE set
        name = self.tle_name
        line1 = self.tle_line1
        line2 = self.tle_line2

        # calc satellite position
        sat = ephem.readtle(name, line1, line2)
        sat.compute(GST)

        self.lat = deg(sat.sublat)
        self.long = deg(sat.sublong)
        self.elev = sat.elevation

        self.az = deg(sat.az)
        self.alt = deg(sat.alt)

        self.rv = sat.range_velocity
        self.dist = sat.range

        self.data = [self.tle_norad, self.lat, self.long, self.elev, self.az, self.alt, self.rv, self.dist]
        for i in range(len(self.data)):
            if type(self.data[i]) != str:
                self.data[i] = str(self.data[i])