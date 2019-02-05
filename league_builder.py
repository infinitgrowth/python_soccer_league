# ========================================
# Purpose: 
# Program that builds a soccer league by spliting 
# 18 players into 3 balanced teams of experience and 
# non-experienced players. Generates a teams.txt file
# that details the teams and players information
# In addition the program generates welcome letters
# for the guardians of each player with post 
# registration instructions 
# ========================================

# Import libraries to handle csvs and dates
import csv
import datetime


# Player assigner function
# Purpose: Split team's evenly into 3 groups
def pl_assigner(file, team, pl_list):
    pl_list_pop=[]
    pl_list_npop=[]
    pl_list_not_assigned=[]
    # This list is a temp list
    pl_list_temp = pl_list.copy()
    count_exp = 0
    count_non_exp = 0
    file.write(team + '\n')
    for pl in pl_list:
        # Array counter
        if pl["Soccer Experience"] == "YES":
            if count_exp <= 2:
                # Call the player document function to create doc and get count
                count_exp = pl_doc(pl, team, count_exp, file, pl_list_pop, pl_list_temp)                
            else:
                pl_list_not_assigned.append(pl_list_temp.pop(0))
        elif pl["Soccer Experience"] == "NO":
            if count_non_exp <= 2:                
                # Call the player document function to create doc and get count
                count_non_exp = pl_doc(pl, team, count_non_exp, file, pl_list_npop, pl_list_temp)
            else:
                # Remove player from temp list to unassigned list
                pl_list_not_assigned.append(pl_list_temp.pop(0))
    file.write('\n')   
    return pl_list_not_assigned.copy()


# Player documents function
# Purpose: Creates the team and player welcome documents
def pl_doc(pl, team, count,tfile,pop_list,temp_list):
    # Writes player to the teams.txt file
    tfile.write(pl["Name"] + ", " + pl["Soccer Experience"] + ", " + pl["Guardian Name(s)"] + '\n')
    
    # Remove assigned player from copied player list
    pop_list.append(temp_list.pop(0))
    
    # Prepare file name string for each players welcome letter
    pl_file_name = pl["Name"].replace(" ","_")+".txt"

    # Get current year for the document
    cur_year = datetime.datetime.now()
    cur_year = cur_year.year
    
    # Create customized letter for each player
    with open(pl_file_name, 'w') as plfile:
        plfile.write("""
Dear {},

We are pleased to inform you that {} has made the {} team.
The first practice will be on Sunday March 1st, {} at 10am
on the Python field.

Thank you for registering and I look forward to a great
fun filled soccer season!!
                    """.format(
                        pl["Guardian Name(s)"],
                        pl["Name"].split(" ")[0],
                        team,
                        cur_year
                        ))
    # Count that keeps track of the number of players assigned to a team
    # and returned from the function
    count += 1
    return count


# Main function that runs the code to build the soccer league
def league_builder():
    # Open csv and read it into an Ordered Dict soccer_reader
    with open('soccerplayers.csv', newline='') as csvfile:
        soccer_reader = csv.DictReader(csvfile)
        
        # initialize player list as list
        pl_list = []
        
        # Extract keys and values from the ordered dict 
        # and create a list of dictionaries
        for pl in soccer_reader:
            a = dict(pl.items())
            pl_list.append(a)

    # Create team of arrays
    teams = ['Sharks','Dragons', 'Raptors']

    # Create file named team.txt
    with open('teams.txt', 'w') as file:
        
        # loop through teams and call the player assigner function 
        for team in teams:
            pl_list = pl_assigner(file, team, pl_list)


# Ensure program isn't run on import
if __name__ == "__main__":
    # call league builder
    league_builder()
    