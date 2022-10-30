'''
Author: Martin Plut
Date: 10/28/2022
Description: Calculate number of remaining points for the season and the earliest possible race to win driver championship
'''
from ergastWrapper import ergast

f1 = ergast()

class Earliest_Win:

    def get_num_races(self, season="current") -> int:
        race_weekends = f1.getSeasonLength()
        sprint_races = self.find_sprints(race_weekends[1]["MRData"]["RaceTable"]["Races"])
        return int(race_weekends[0]), sprint_races

    def find_sprints(self, race_list):
        sprints = 0
        for item in race_list:
            try:
                item["Sprint"]
                sprints += 1
            except KeyError:
                continue
        return sprints


    def get_max_points(self, season="current"):
        '''
        returns <number of sunday races x26> + <number of saturday sprint races x8>
        '''
        max_points = (self.num_races * 26) + (self.num_sprints * 8)
        return max_points
    def get_remaining_points(self, season="current"):
        '''
        returns the amount of points left to be won during the season.
        requires <remaining races> x <number of points to be won>
        '''
        pass
    def init(self):
        self.num_races, self.num_sprint_races = self.get_num_races()
        self.max_points = self.get_max_points()





def get_champ_leader_points(season="current"):
    '''
    return leaders points at the current moment
    '''
    return f1.getDriverStandings()[0]["points"]

def get_second_place_points(season="current"):
    '''
    return second place's points at the current moment
    '''
    return f1.getDriverStandings()[1]["points"]

def earliest_win():
    '''
    return the race where second place can no longer win enough points to beat first place (remaining points < delta between 1st and 2nd). 
    '''
    win = Earliest_Win()
    # max_points = win.get_max_points()
    # remaining_points= get_remaining_points(max_points)
    # first_place_points = get_champ_leader_points()
    # second_place_points = get_second_place_points()
    # points_delta = first_place_points - second_place_points            


def test():
    print(get_champ_leader_points())
    print(get_second_place_points())
    
if __name__ == '__main__':
    test()