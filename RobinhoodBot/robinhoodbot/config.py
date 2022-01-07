

#Enter your robinhood username and password here, then save this file in the same directory as a regular python file
rh_password=""
rh_username=""


# change to false to run withough debugs
debug=False

#Twitter Stuff
import praw 

reddit = praw.Reddit(client_id='zPDx63pzvGPMukObD5_9nQ', \
                     client_secret='a2yT0UPudj9GhbLaTMNCQA9WwNALVg', \
                     user_agent='Test Script', \
                     username='simotsu', \
                     password='pin576nine242')

#Below will designate if you actually start trading.
rh_tradeamount=1200
startbuying=False
startselling=False
volFinder=10000000

