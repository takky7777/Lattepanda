from datetime import datetime as dt

class times:
    def __init__(self) -> None:
        pass
    
    def getTime(self, mode):
        now = dt.now()
        #time formatting
        if mode == "all":
            return [now.strftime("%y"), now.strftime("%m"), now.strftime("%d"), now.strftime("%H"), now.strftime("%M"), now.strftime("%S")]
        if mode == "H":
            return int(now.strftime("%H"))