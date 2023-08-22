import ephem
from satellite_tle import fetch_tle_from_celestrak

GST = ephem.Observer()

class ep:
    def __init__(self) -> None:
        pass
    
    def updatetle(self, norad_id):
        self.tle_raw = fetch_tle_from_celestrak(norad_id)
        self.tle_name= self.tle_raw[0]
        self.tle_line1 = self.tle_raw[1]
        self.tle_line2 = self.tle_raw[2]