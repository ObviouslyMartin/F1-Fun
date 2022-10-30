from driverpy import F1Driver


class F1Parser():

    def createDrivers(self, res):
        driver = F1Driver()
        for thing in res:
            for k, v in thing.items():
                print(f"K: {k}, V: {v}")
            return


    def printRawResult(self, resultJSON):
        if(type(resultJSON) == dict):
            for key, value in resultJSON.items():
                try:
                    for k, v in value.items():
                        print(f'{k}: {v}')
                except (ValueError, AttributeError) as e:
                    print(f'{key}: {value}')
                    print(e)
        elif (type(resultJSON) == list):
            for item in resultJSON:
                self.printRawResult(item)


    '''
    TODO: generalize this for all json results from ergast...

    '''
    def getNamesAndPosFromRes(self, res, nandp=[], di={}):
        NamesAndPos = nandp
        driverInfo = di
        for driver in res:
            for key, value in driver.items():
                try:
                    for k, v in value.items():
                        if k == "driverId":
                            driverInfo.update({"driver":v})
                        elif k == "constructorId":
                            driverInfo.update({"constructor" : v})
                        
                except (ValueError, AttributeError) as e:
                    if key == "position":
                        driverInfo.update({"racePos" : value})
                    if key == "grid":
                        driverInfo.update({"qualifyingPos" : value})
                    if key == "status":
                        driverInfo.update({key : value})
                        NamesAndPos.append(driverInfo.copy())
                        driverInfo.clear()
                    
        #self.printresults(NamesAndPos)
        return NamesAndPos
        
