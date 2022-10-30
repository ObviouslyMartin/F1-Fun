'''
Author: Martin Plut
Date: 10/28/2022
Description: Calculate number of remaining points for the season and the earliest possible race to win driver championship
'''
from shutil import register_archive_format
from ergastWrapper import ergast

f1 = ergast()

def get_num_races(season="current") -> int:
    race_weekends = f1.getSeasonLength()
    sprint_races = find_sprints(race_weekends[1]["MRData"]["RaceTable"]["Races"])
    return int(race_weekends[0]), sprint_races

def find_sprints(race_list):
    sprints = 0
    for item in race_list:
        try:
            item["Sprint"]
            sprints += 1
        except KeyError:
            continue
    return sprints

def get_max_points(season="current"):
    '''
    returns <number of sunday races x26> + <number of saturday sprint races x8>
    '''
    num_races, num_sprints = get_num_races()
    max_points = (num_races * 26) + (num_sprints * 8)
    return max_points

def get_remaining_points(max_points, season="current"):
    '''
    returns the amount of points left to be won during the season.
    requires <remaining races> x <number of points to be won>
    '''
    pass

def get_champ_leader_points(season="current"):
    '''
    return leaders points at the current moment
    '''
    pass

def get_second_place_points(season="current"):
    '''
    return second place's points at the current moment
    '''
    pass

def earliest_win():
    '''
    return the race where second place can no longer win enough points to beat first place (remaining points < delta between 1st and 2nd). 
    '''
    max_points = get_max_points()
    remaining_points= get_remaining_points()
    first_place_points = get_champ_leader_points()
    second_place_points = get_second_place_points()
    points_delta = first_place_points - second_place_points            


def test():
    pass
    
if __name__ == '__main__':
    earliest_win()