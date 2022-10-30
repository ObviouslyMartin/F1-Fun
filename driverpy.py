

class F1Driver():
    def __init__(self, driverId="", number="", code="", name=""):
        self.driverId, self.number, self.code, self.name = driverId, number, code, name
        self.qualifyingPosition = 0
        self.raceStartPosition = 0
        self.raceFinishPosition = 0
        self.constructor ="" 
        self.points = 0
        self.fastestLap = ""