"""
Created by: Dominic Fuentes
Date: 10/14/2022
Purpose:
    Create a model for information spreading through n# of people and m# of new stations
"""
import copy
import json
import random 
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from operators import Operators


if __name__=="__main__":
    """
    This json is good for initial testing but not for scaling
    """
    # path = os.getcwd()
    # path = os.path.join(path,"people_info.json")
    # original_opinions = json.load(open(path, 'r'))
    # new_opinions = json.load(open(path, "r"))


    total_people = 100
    users_list = {}
    connection_list = {}
    number_of_opinions = 4
    for number_of_people in range(1, total_people+1):
        starting_friend = random.randint(1, total_people+1)
        ending_friend = random.randint(1, total_people+1)
        users_list[f"person{number_of_people}"] = {
            "susceptibility":round(random.random()+.01,2),
            "convincing":round(random.random()+.01,2),
            # "friends":[f"person{x}" for x in range(
            #     min(starting_friend, ending_friend), 
            #     max(starting_friend, ending_friend)
            #     )
            # ],
            "opinions":[round(random.random(),2) for x in range(number_of_opinions)]
        }
        connection_list[f"person{number_of_people}"] = [
            [f"person{number_of_people}",f"person{x}"] for x in range(
                min(starting_friend, ending_friend), 
                max(starting_friend, ending_friend)
                )
            ]
    new_users_list = copy.deepcopy(users_list)

    total_news = 5
    for news in range(1, total_news+1):
        starting_friend = random.randint(1, total_people+1)
        ending_friend = random.randint(1, total_people+1)
        users_list[f"news{news}"] = {
            "susceptibility":0,
            "convincing":round(random.random()+0.1, 2),
            "friends":[f"person{x}" for x in range(
                min(starting_friend, ending_friend),
                max(starting_friend, ending_friend)
                )],
            "opinions":[random.randint(1,10) for x in range(number_of_opinions)]
        }

    for person, person_info in new_users_list.items():
        # for friend in person_info["friends"]:
        for connection, connection_info in connection_list.items():
            print(connection_info)
            ops = Operators(person_info, new_users_list[connection_info[1]])
            ops.opinion_interaction()
    
    each_max = []
    for person in new_users_list:
        each_max.append(np.max(new_users_list[person]["opinions"]))
    
    total_max = np.max(each_max)
    for person in new_users_list:
        new_users_list[person]["opinions"] = new_users_list[person]["opinions"] / total_max

    print(new_users_list["person1"], new_users_list["person10"])

    for opinion in range(len(users_list["person1"]["opinions"])):
        for person in new_users_list:
            diff = [round(bi - ai, 2) for ai, bi in zip(
                [users_list[person]["opinions"][opinion]],
                [new_users_list[person]["opinions"][opinion]]
                )
            ]
            # plt.scatter([x for x in range(len(diff))], diff)
            # plt.plot(diff)
            plt.bar(person, diff)
        plt.title(f"Person's Change in Opinion{opinion}")
        plt.xlabel(f"People")
        plt.xticks(rotation=45)
        plt.ylabel("Change in opinion")
        # plt.ylim(0,4)
        plt.legend(new_users_list,bbox_to_anchor=(0, 1), loc='upper left', ncol=int(np.sqrt(number_of_people))-1)
        plt.show()