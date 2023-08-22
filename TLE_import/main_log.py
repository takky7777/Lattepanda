import tle
import log_operate
import times

def main():
    ep = tle.ep()
    logop = log_operate.logOp()
    time = times.times()
    isupdated = False

    while True:
        H = time.getTime("H")
        
        #import settings
        setting = logop.settingImport()
        NORAD = setting[0]
        if isupdated == False and H % 2 == 0:
            ep.updatetle(NORAD) #fetch new tle
            logop.pushTLE(NORAD, ep.tle_raw)  #new tle to xl
            print(ep.tle_name, "\n", ep.tle_line1, "\n", ep.tle_line2)
            isupdated = True
        elif isupdated == True and H % 2 == 1:
            isupdated = False

main()