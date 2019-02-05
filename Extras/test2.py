# # Outline MVP
# output a text file named teams.txt
# Create 3 teams: Sharks, Dragons and Raptors
# split the teams by experience
#   count the number of experienced with yes
#   assign them to teams first evenly
#   then assign the rest to the teams
# Extra credit
# Create 18 files
#   name files by player with underscore btw first and last name using replace
#     
#
#=========================================

import csv
import datetime

def pl_letter(pl, team, count,pop_list,temp_list):
                b = (pl["Name"] + ", " + pl["Soccer Experience"] + ", " + pl["Guardian Name(s)"] + '\n')
                pop_list.append(temp_list.pop(0))
                # Prepare file name string for each player
                pl_file_name = "Letters\\"+pl["Name"].replace(" ","_")+".txt"
                #print(pl_file_name)
                cur_year = datetime.datetime.now()
                cur_year = cur_year.year
                print(pl_file_name)
                a = ("""
Dear {},

We are pleased to inform you that {} has made the {} team.
The first practice will be on Sunday March 1st, {} at 10am
on the Python field.

Thank you for registering and I look forward to a great
fun filled soccer season!!
                    """.format(
                        pl["Guardian Name(s)"],
                        pl["Name"],
                        team,
                        cur_year
                        ))
                count += 1
                return count

# Player assigner function
# Purpose: Split team's evenly into 3 groups
# Code Learnings:
# - looping with for loop:
# .copy() is necessary for loops in order to ensure the 
# loop doesn't behave weirdly and skip indexes when 
# values are removed.
# .pop() the iterated array's COPY
def pl_assigner(team, pl_list):
    pl_list_pop=[]
    pl_list_npop=[]
    pl_list_safe=[]
    # This list is a temp list
    pl_list_temp = pl_list.copy()
    count_exp = 0
    count_non_exp = 0
    print(team + '\n')
    for pl in pl_list:
        # Array counter
        if pl["Soccer Experience"] == "YES":
            if count_exp <= 2:
                count_exp = pl_letter(pl, team, count_exp, pl_list_pop, pl_list_temp)                
            else:
                pl_list_safe.append(pl_list_temp.pop(0))
        elif pl["Soccer Experience"] == "NO":
            if count_non_exp <= 2:                
                count_non_exp =pl_letter(pl, team, count_non_exp, pl_list_npop, pl_list_temp)
            else:
                # List of players that are not yet assigned
                pl_list_safe.append(pl_list_temp.pop(0))
    print('\n')   
    return pl_list_safe.copy()


def league_builder():
    # Original test for main
    # print('hello')

    pl_list = [{'Name': 'Joe Smith', 'Height (inches)': '42', 'Soccer Experience': 'YES', 'Guardian Name(s)': 'Jim and Jan Smith'}, {'Name': 'Jill Tanner', 'Height (inches)': '36', 'Soccer Experience': 'YES', 'Guardian Name(s)': 'Clara Tanner'}, {'Name': 'Bill Bon', 'Height (inches)': '43', 'Soccer Experience': 'YES', 'Guardian Name(s)': 'Sara and Jenny Bon'}, {'Name': 'Eva Gordon', 'Height (inches)': '45', 'Soccer Experience': 'NO', 'Guardian Name(s)': 'Wendy and Mike Gordon'}, {'Name': 'Matt Gill', 'Height (inches)': '40', 'Soccer Experience': 'NO', 'Guardian Name(s)': 'Charles and Sylvia Gill'}, {'Name': 'Kimmy Stein', 'Height (inches)': '41', 'Soccer Experience': 'NO', 'Guardian Name(s)': 'Bill and Hillary Stein'}, {'Name': 'Sammy Adams', 'Height (inches)': '45', 'Soccer Experience': 'NO', 'Guardian Name(s)': 'Jeff Adams'}, {'Name': 'Karl Saygan', 'Height (inches)': '42', 'Soccer Experience': 'YES', 'Guardian Name(s)': 'Heather Bledsoe'}, {'Name': 'Suzane Greenberg', 'Height (inches)': '44', 'Soccer Experience': 'YES', 'Guardian Name(s)': 'Henrietta Dumas'}, {'Name': 'Sal Dali', 'Height (inches)': '41', 'Soccer Experience': 'NO', 'Guardian Name(s)': 'Gala Dali'}, {'Name': 'Joe Kavalier', 'Height (inches)': '39', 'Soccer Experience': 'NO', 'Guardian Name(s)': 'Sam and Elaine Kavalier'}, {'Name': 'Ben Finkelstein', 'Height (inches)': '44', 'Soccer Experience': 'NO', 'Guardian Name(s)': 'Aaron and Jill Finkelstein'}, {'Name': 'Diego Soto', 'Height (inches)': '41', 'Soccer Experience': 'YES', 'Guardian Name(s)': 'Robin and Sarika Soto'}, {'Name': 'Chloe Alaska', 'Height (inches)': '47', 'Soccer Experience': 'NO', 'Guardian Name(s)': 'David and Jamie Alaska'}, {'Name':'Arnold Willis', 'Height (inches)': '43', 'Soccer Experience': 'NO', 'Guardian Name(s)': 'Claire Willis'}, {'Name': 'Phillip Helm', 'Height (inches)': '44', 'Soccer Experience': 'YES', 'Guardian Name(s)': 'Thomas Helm and Eva Jones'}, {'Name': 'Les Clay', 'Height (inches)': '42', 'Soccer Experience': 'YES', 'Guardian Name(s)': 'Wynonna Brown'}, {'Name': 'Herschel Krustofski', 'Height (inches)': '45', 'Soccer Experience': 'YES', 'Guardian Name(s)': 'Hyman and Rachel Krustofski'}]


    # Create team of arrays
    teams = ['Sharks','Dragons', 'Raptors']

    # Create file named team.txt
    #with open('teams.txt', 'w') as file:
        
    # loop through arrays 
    for team in teams:
        pl_list = pl_assigner(team, pl_list)


if __name__ == "__main__":
    # call league builder
    league_builder()
    