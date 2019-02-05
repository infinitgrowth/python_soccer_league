#=========================================

import csv
# league builder main function
def league_builder():
    # Original test for main
    # print('hello')

    # Open csv and read it into an Ordered Dict soccer_reader
    with open('soccerplayers.csv', newline='') as csvfile:
        soccer_reader = csv.DictReader(csvfile)
        
        # Make array of experience, no experience players and full list for extra cred
        pl_list_pop = []
        pl_list_nexp = []
        pl_list = []
        
        # Extract keys and values from the ordered dict based on exp and no  exp
        for pl in soccer_reader:
            a = dict(pl.items())
            #dictpl = 
            #print(a)
            # i += 1 
            # print(a[0][1])
            # str_a = a[0][1].replace(" ","_")+".txt"
            # print(str_a)
            # a[1]
            pl_list.append(a)
            pl_list_pop.append(pl_list.pop(0))
        print(pl_list)

            
            # pl_list.append(list(pl))
            # if pl["Soccer Experience"] == 'YES':
            #     pl_list_exp.append(pl["Name"]+", "+pl["Soccer Experience"]+", "+pl["Guardian Name(s)"])
            # if pl["Soccer Experience"] == 'NO':
            #     pl_list_nexp.append(pl["Name"]+", "+pl["Soccer Experience"]+", "+pl["Guardian Name(s)"])
            
        # get lengths for experience and total players
        # pl_count = len([row for row in rows])
        # exp_pl_count = len([row for row in soccer_reader if row['Soccer Experience'].upper() == 'YES']) 
        # print(pl_count)
        # print(exp_pl_count)

        


if __name__ == "__main__":
    # call league builder
    league_builder()
    