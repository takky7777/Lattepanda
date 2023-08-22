import pathlib
import json_operate

hoge = pathlib.Path(__file__).resolve().parent.parent / ""

class FreqCtrl():
    def __init__(self) -> None:
        self.json_log = json_operate.logOp()


    def GetFreq(self):
        MODE = self.json_log.GetMode()
        MODE = 1
        freq = self.json_log.GetFreq()
        freq_u = freq[0]
        freq_d = freq[1]
        rv = self.json_log.GetRV()
        if MODE == True: #AUTO
            COM_DIR = "UPLINK"
            freq_u = doppler_shift(COM_DIR, freq_u, rv)

            COM_DIR = "DOWNLINK"
            freq_d = doppler_shift(COM_DIR, freq_d, rv)
        return [freq_u, freq_d]
    

def doppler_shift(COM_DIR, freq, rv):
    speed_of_light = 299792458  #mps
    if COM_DIR == "DOWNLINK":
        shifted_freq = speed_of_light / (speed_of_light - rv) * freq
    elif COM_DIR == "UPLINK":
        shifted_freq = (speed_of_light - rv) / speed_of_light * freq      #Unconfirmed
    return shifted_freq


def debug():
    hoge = FreqCtrl()
    freq = hoge.GetFreq()
    print("REMINDER:THE FREQs USED HERE ARE DUMMIES")
    print("UPLINK :", freq[0], "\nDWNLINK ;", freq[1])


debug()