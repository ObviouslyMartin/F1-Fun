from ergastWrapper import ergast # from <file_name> import <class> || <function>
from f1parser import F1Parser

api = ergast()
f1parser = F1Parser()

def test_getRaceResults():
    res = api.getRaceResults()
    # a.getNamesAndPosFromRes(res)
    print(res)


def test_getDriverStandings():
    res = api.getDriverStandings()
    print(res[1])

def test_f1parser():
    f1parser.createDrivers(api.getRaceResults(2022, 11))


def test_getLaptimesForDriver():
    res = api.getLapTimesForDriver("Sainz", 2)
    print(res)

def test_getSeasonLength():
    res = api.getSeasonLength()
    print(res)


if __name__ == '__main__':
    test_getRaceResults()