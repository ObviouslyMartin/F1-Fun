'''
Author: Martin Plut
Date: 10/28/2022
Description: Calculate number of remaining points for the season and the earliest possible race to win driver championship
'''

'''
TODO:   determine how many sprint races are left (currently assumes all sprint races have been completed

'''

from ergastWrapper import ergast

f1 = ergast()

class Earliest_Win:

    def __init__(self):
        self.num_races, self.num_sprint_races = self.get_num_races()
        self.max_points = (self.num_races * 26) + (self.num_sprint_races * 8)
        self.leader_points = self.get_champ_leader_points()
        self.second_place_points = self.get_second_place_points()
        self.remaining_points = self.get_remaining_points()
        self.print()


    def get_num_races(self, season="current") -> int:
        race_weekends = f1.getSeasonLength()
        sprint_races = self.find_sprints(race_weekends[1]["MRData"]["RaceTable"]["Races"])
        return int(race_weekends[0]), sprint_races

    def find_sprints(self, race_list) -> int:
        sprints = 0
        for item in race_list:
            try:
                item["Sprint"]
                sprints += 1
            except KeyError:
                continue
        return sprints

    def get_remaining_points(self, season="current") -> int:
        '''
        returns the amount of points left to be won during the season.
        requires <remaining races> x <number of points to be won>
        '''
        last_round = int(f1.getRaceResults()["round"])
        remaining_races = self.num_races - last_round
        return remaining_races * 26

    def get_champ_leader_points(self, season="current") -> int:
        '''
        return leaders points at the current moment
        '''
        return f1.getDriverStandings()[0]["points"]

    def get_second_place_points(self, season="current") -> int:
        '''
        return second place's points at the current moment
        '''
        return f1.getDriverStandings()[1]["points"]

    def print(self):
        print(f'number of races in the current season: {self.num_races}')
        print(f'number of sprint races in the current season: {self.num_sprint_races}')
        print(f'maximum number of points in the current season: {self.max_points}')
        print(f'points left in the season: {self.remaining_points}')
        print(f'championship leader current points total: {self.leader_points}')
        print(f'second place current points total: {self.second_place_points}')

    def calculate(self):
        if self.remaining_points < (self.leader_points - self.second_place_points):
            print(f'mathematically won, remaining points < points delta')
            print(f'remaining points: {self.remaining_points}')
            print(f'Champion\'s points: {self.leader_points}')
            print(f'2nd place\'s points: {self.second_place_points}')
        else:
            pass
            '''
            TODO: print finish position 1st and 2nd place need to win/take the championship
            find at what point the amount of points remaining < the points delta
            '''
def earliest_win():
    '''
    return the race where second place can no longer win enough points to beat first place (remaining points < delta between 1st and 2nd). 
    '''
    win = Earliest_Win()

    
if __name__ == '__main__':
    earliest_win()