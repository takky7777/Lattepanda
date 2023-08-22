from datetime import datetime as dt


class times:
    def __init__(self) -> None:
        pass

    def getTime(self, mode):
        now = dt.utcnow()
        if mode == "all":
            return [int(now.strftime("%y")), int(now.strftime("%m")), int(now.strftime("%d")), int(now.strftime("%H")), int(now.strftime("%M")), int(now.strftime("%S"))]
        if mode == "time":
            return now
