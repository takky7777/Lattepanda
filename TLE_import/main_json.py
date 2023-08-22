import tle
import json_operate
import times

def main():
    ep = tle.ep()
    logop = json_operate.logOp()
    time = times.times()
    isupdated = False

    while True:
        H = time.getTime("H")
        if isupdated == False and H % 2 == 1:
            #import settings
            setting = logop.ConfImport()
            NORAD = setting[0]
            ep.updatetle(NORAD) #fetch new tle
            logop.pushTLE(NORAD, ep.tle_raw)  #new tle to xl
            print(ep.tle_name, "\n", ep.tle_line1, "\n", ep.tle_line2)
            isupdated = True
        elif isupdated == True and H % 2 == 0:
            isupdated = False

main()