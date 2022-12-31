from datetime import date as dt
from datetime import timedelta as td
from content import * 
from talks import Talk
from mailer import to_blog,to_mailinglist
from discourser import to_tlc


def date_fetcher():
    correction = 6 - dt.today().weekday()
    return (dt.today()+td(days=correction)).strftime("%b %d, %Y")

def get_talk_details():
    talk_list=[]
    num_talks=int(input("Enter the number of talks: "))
    for i in range(0,num_talks):
        item=Talk()
        talk_list.append(item)
    return talk_list

def printer(content, design, num):
    print(design*num)
    print(content.center(num, design))
    print(design*num)


def previewer(message):
    printer("Preview", "#", 25)
    print(message_en)
    print("#"*25)
#print(mc_weeklydiscussion(date_fetcher()))
#print(mc_monthlymeeting(date_fetcher(), talks_msg_generator(get_talk_details())))

print("Welcome to agent0!")
date=date_fetcher()
print("Date: ",date)
date_choice=input("Is this date correct for the message(y/n): ")
if date_choice.lower()=="n":
    indate,month,year = map(int, input("Enter the date details space seperated in the order (date, month, year): ").split())
    date=dt(year, month, indate).strftime("%b %d, %Y")
print("Date is set now!")
print("Now select the event type: ")
event_menu={
        1:"MM",
        2:"WD",
        3:"CS"
        }
printer("Event Menu", "#", 25)
event_msg='''
1 : MM (Monthly Meeting)
2 : WD (Weekly Discussion)
3 : CS (Call for Speakers)
'''
print(event_msg)
print("#"*25)
event=event_menu[int(input("Enter the menu number(1-3): "))]

print("The choosen event is: ", event)
place_menu={
        1:"111",
        2:"110",
        3:"100",
        4:"010",
        5:"001"
        }

printer("Place Menu", "#", 25)
place_msg='''
1 : All places (Mailing list, blog, TLC)
2 : Combo1 (Mailing list and blog)
3 : Only Mailing list 
4 : Only blog
5 : Only TLC

Note: TLC option is only available for monthly meeting schedule
'''
print(place_msg)
print("#"*25)
place=place_menu[int(input("Enter the place number(1-5): "))]

print("The choosen place code is: ", place)

if event=="MM":
    talkmsg=talks_msg_generator(get_talk_details())
    if place[0]=="1":
        message_en=mc_monthlymeeting(date, talkmsg)
        previewer(message_en)
        if input("Is the content okay(y/n): ").lower()=="y":
            to_mailinglist(message_en)
    if place[1]=="1":
        message_en=bc_monthlymeeting(date, talkmsg)
        previewer(message_en)
        if input("Is the content okay(y/n): ").lower()=="y":
            to_blog(message_en)
    if place[2]=="1":
        message_en,title_en=fc_monthlymeeting(date, talkmsg)
        previewer(message_en)
        if input("Is the content okay(y/n): ").lower()=="y":
            to_tlc(message_en,title_en)
elif event=="WD":
    if place[0]=="1":
        message_en=mc_weeklydiscussion(date) 
        previewer(message_en) 
        if input("Is the content okay(y/n): ").lower()=="y":
            to_mailinglist(message_en)
    if place[1]=="1":
        message_en=bc_weeklydiscussion(date)
        previewer(message_en)
        if input("Is the content okay(y/n): ").lower()=="y":
            to_blog(message_en)
elif event=="CS":
    if place[0]=="1":
        message_en=mc_callforspeakers(date) 
        previewer(message_en)
        if input("Is the content okay(y/n): ").lower()=="y":
            to_mailinglist(message_en)
    if place[1]=="1":
        message_en=bc_callforspeakers(date)
        previewer(message_en)
        if input("Is the content okay(y/n): ").lower()=="y":
            to_blog(message_en)




        



