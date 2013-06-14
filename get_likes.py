#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
# This file is to fetch likes of the certain file to file
# Putput file: like_dump.json
# Composed by Zakharchenko Taras 

# Desclaimer: You are free to use it as you wish, but do not remove this message
# <3

import vkontakte
import time

def getWallLikes(vk, user):
    pos = 0
    retval = []
    #Get post count
    res = vk.wall.get(owner_id=user, offset=pos, count=1, filter="owner")
    time.sleep(1) #Sleep for a one sec. To protect the application from ban
    left = res[0]
    #Read all posts but mo more then 100 a time
    while left > 0:
        if left >= 100:
            sent = 100
        else:
            sent = left
        #Fetch posts
        res = vk.wall.get(owner_id=user, offset=pos, count=sent, filter="owner")
        left = left - sent
        pos = pos + sent
        #Add new posts to post list
        retval.extend(res[1:])
        time.sleep(1)
    post_list = retval;
    #Fetch likes for every post
    for i in range(0,len(post_list)):
        post_id = post_list[i]["id"]
        res = vk.likes.getList(type="post", owner_id=user, item_id=post_id)
        post_list[i]["like_info"] = res
        print("%d out of %s"%(i, len(post_list)))
        time.sleep(1)
    #Dump the list to file
    f = open('like_dump.json', 'w')  
    f.write(str(retval))
    f.close()  

if __name__ == "__main__":
    #Preobtained access token
    token = "038070621f944cf3454774b52950bbeee5ab7c3df1c5197dc1db95db1d0310342b5b7c5aa391131f82a072b"
    #Person you are interested in
    user_id = "9761294";
    #Your VK application data
    vk = vkontakte.API("3582332403", "AcW90Adkjf87sdfuvts1YJoxF", token)
    getWallLikes(vk, user_id)
