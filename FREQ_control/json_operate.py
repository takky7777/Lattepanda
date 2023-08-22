import json
import os
from pathlib import Path

#fetch sources
cd = Path.cwd()


class logOp:
    def __init__(self):
        #get path for GSSdata.xlsx
        GSSdata_path = Path(__file__).resolve().parent.parent / "GSSdata"
        self.conf = GSSdata_path / "GSE_config.json"
        self.SC = GSSdata_path / "SAT_COORDS.json"


    def GetMode(self):
        with open(self.conf, 'r') as f:
            dic = json.load(f)
        MODE = dic["MODE"]["FREQ_AUTO"]
        return MODE
    

    def GetFreq(self):
        with open(self.conf, 'r') as f:
            dic = json.load(f)
        freq = [dic["MANUAL"]["UP_FREQ"], dic["MANUAL"]["DOWN_FREQ"]]
        return freq
    

    def GetRV(self):
        with open(self.SC, 'r') as f:
            dic = json.load(f)
            rows = len(dic)
        rv = float(dic[str(rows)]["COORDS"]["RV"])
        return rv
            



hoge = logOp()