import analyze
import log_operate
import time

def main():
    #class setup
    ep = analyze.ep()
    logop = log_operate.logOp()
    
    #import settings
    set = logop.settingImport()
    for i in range(len(set)):
        set[i] = float(set[i])
    print(set)

    print("  YY    MM    DD    hh    mm    ss || lat              long                 elev           az                alt                rv               dist")
    while True:
        ep.tleFromSheet(set[0])   #fetch latest tle
        ep.analize(set[1], set[2], set[3]) #analize with given coords //leave blank for GND coords
        logop.pushData(ep.data)#update data to xl
        print(ep.data)
        time.sleep(1)
main()