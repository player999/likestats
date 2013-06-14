#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
# This script is to interpret post info from get_likes.py

# Output files:
# fans.txt-- The most of likes
# stats_by_person.txt -- stats by certain person by month
# stats_overall.txt -- stats by all users by month

# Composed by Zakharchenko Taras 
# Desclaimer: You are free to use it as you wish, but do not remove this message
# <3

import operator
import datetime

#Function switcher
def analyze(fname, options):
    data = open(fname, 'r').read()
    data = eval(data)
    for opt in options:
        if opt["name"] == "most_of_likes":
            most_of_likes(data)
        if opt["name"] == "stats_overall":
            stats_overall(data)
        if opt["name"] == "stats_by_person":
            stats_by_person(data, opt["user_id"])

#Collect rating of persons who liked the page
#Sort by like count descending
def most_of_likes(data):
    users = []
    like_count = []
    for post in data:
        users.extend(post["like_info"]["users"])
    uusers =  set(users)
    for user in uusers:
        like_count.extend([(users.count(user), user)])
    like_count.sort(key=operator.itemgetter(0))
    like_count.reverse()
    f = open("fans.txt", "w")
    for entry in like_count:
        f.write("%s\t%s\n"%(entry[1], entry[0]))
    f.close()

#Show stats by months by certain person who liked the page
#Output table format: Month-Like_count
def stats_by_person(data, user_id):
    liked_posts = []
    for entry in data:
        if user_id in entry["like_info"]["users"]:
            liked_posts.extend([entry])
    data = liked_posts
    like_dates = []
    dates = []
    for entry in data:
        date_string = datetime.datetime.fromtimestamp(int(entry["date"])).strftime('%m.%Y')
        like_dates.extend([{"date":date_string, "likes":entry["likes"]["count"]}])
        dates.extend([date_string])
    dates = set(dates)
    dates = list(dates)
    dates.sort(key=compare_dates)
    like_by_month = []
    for date in dates:
        likec = 0
        for entry in like_dates:
            if entry["date"] == date:
                likec = likec + 1
        like_by_month.extend([{"date":date, "likes":likec}])
    f = open("stats_by_person.txt", "w")
    for entry in like_by_month:
        f.write("%s\t%s\n"%(entry["date"], entry["likes"]))
    f.close()

#Show stats by months by all persons who liked the page
#Output table format: Month-Like_count
def stats_overall(data):
    like_dates = []
    dates = []
    for entry in data:
        date_string = datetime.datetime.fromtimestamp(int(entry["date"])).strftime('%m.%Y')
        like_dates.extend([{"date":date_string, "likes":entry["likes"]["count"]}])
        dates.extend([date_string])
    dates = set(dates)
    dates = list(dates)
    dates.sort(key=compare_dates)
    like_by_month = []
    for date in dates:
        likec = 0
        for entry in like_dates:
            if entry["date"] == date:
                likec = likec + int(entry["likes"])
        like_by_month.extend([{"date":date, "likes":likec}])
    f = open("stats_overall.txt", "w")
    for entry in like_by_month:
        f.write("%s\t%s\n"%(entry["date"], entry["likes"]))
    f.close()


#Comparison function for date strings
#Date format MM.YYYY
def compare_dates(entry):
    parts = entry.split('.')
    return int(parts[0]) + int(parts[1]) * 12
        
if __name__ == "__main__":
    user_id = 111111
    #define options of analyze call
    #Options are the list of dictionaries
    #Dictionary has one mandatory field: "name"
    #I hope you will understand how to use it
    options = [{"name":"most_of_likes"},{"name":"stats_overall"},{"name":"stats_by_person", "user_id":user_id}]
    #Replace the file name
    analyze("like_dump.json", options)
    
