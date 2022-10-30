import string
import requests as req
import json

class ergast:
    def __init__(self):
        self.baseURL = "https://ergast.com/api/f1"
        print("DUN DUN DUN")
        print("neeeeeooowww...neeoow")
    
    def getPolePosition(self, season="current", round="last"):
        # returns json obj containing q1, q2, q3 times for the pole sitter for a given {season} and {round}
        try:
            res = req.get(f"{self.baseURL}/{season}/{round}/qualifying.json").json()
            pole = res["MRData"]["RaceTable"]["Races"][0]["QualifyingResults"][0]
            return pole
        except IndexError:
            return ""

    def getRaceWinner(self, season="current", round="last"):
        # returns json obj containing race results for Race winner during {season} season and {round} round
        # total race tme, fastestLap, average speed, constructor
        try:
            res = req.get(f"{self.baseURL}/{season}/{round}/results.json").json()
            winner = res["MRData"]["RaceTable"]["Races"][0]["Results"][0]
            return winner
        except IndexError:
            return ""

    def getFastestRaceLapTime(self, season="current", round="last"):
        # returns json obj containing fastest lap of the race for a given season and round >= 20004/1
        # driver num, position, points, constructor, time, grid(qualifying) pos, total time, avg speed
        try:
            res = req.get(f"{self.baseURL}/{season}/{round}/fastest/1/results.json").json()
            fastest = res["MRData"]["RaceTable"]["Races"][0]["Results"][0]
            return fastest
        except IndexError:
            return ""

    def getLapTimesForDriver(self, driver, lap, season="current", round="last"):
        try:
            res = req.get(f"{self.baseURL}/{season}/{round}/drivers/{driver}/laps/{lap}.json").json()
            time = res["MRData"]["RaceTable"]["Races"][0]["Laps"][0]["Timings"][0]
            return time
        except IndexError:
            return "0:0.000"

    def getDriverStandings(self, season="current"):
        try:
            res = req.get(f"{self.baseURL}/{season}/driverStandings.json").json()
            driverStandings = res["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
            return driverStandings
        except IndexError:
            return ""

    def getConstructorStandings(self, season="current"):
        try:
            res = req.get(f"{self.baseURL}/{season}/constructorStandings.json").json()
            constructorStandings = res["MRData"]["StandingsTable"]["StandingsLists"][0]["ConstructorStandings"]
            return constructorStandings
        except IndexError:
            return ""

    def getRaceResults(self, season="current", round="last"):
        try:
            res = req.get(f'{self.baseURL}/{season}/{round}/results.json').json()
            result = res["MRData"]["RaceTable"]["Races"][0]["Results"]
            return result
        except IndexError:
            return "" 
    
    def getQualifyingPosForDriver(self, season, round, driver=string):
        pass
    
    def getSeasonLength(self, season="current"):
        try:
            res = req.get(f'{self.baseURL}/{season}.json').json()
            result = res["MRData"]["total"]
            return result, res
        except IndexError:
            return ""