

def mc_weeklydiscussion(date):
    message=f'''
Subject: [KanchiLUG] Weekly discussion - {date}

Hi everyone,
This week in KanchiLUG we have scheduled an weekly discussion as online meeting on Sunday, {date} 16:00 - 17:00 IST

Meeting link : https://meet.jit.si/KanchiLugWeeklyDiscussion

Weekly discussion is an open and friendly discussion where topics related to Linux/FOSS technologies will be discussed. We will meet in the online jitsi meeting and discuss new linux things everyone explored this week and we chat about linux news and topics. If you are facing any issues with linux or any FOSS applications, you can also share your issues during the discussion. Our KanchiLUG community will help to debug or suggest some good alternatives.

Can join with any browser or JitSi android app.
All the Discussions are in Tamil.

About KanchiLUG : Kanchi Linux Users Group [ KanchiLUG ] has been spreading awareness on Free/Open Source Software (F/OSS) in Kanchipuram since November 2006.

Anyone can join! (Entry is free)
Everyone is welcome
Feel free to share this to your friends

--
Thanks and Regards,
Parameshwar Arunachalam
KanchiLUG Co-ordinator
Personal Email: stark20236@gmail.com
Mailing list: kanchilug@freelists.org
Repository : https://gitlab.com/kanchilug
Twitter handle: @kanchilug
'''
    return message


def bc_weeklydiscussion(date):
    message=f'''
Subject: Weekly discussion - {date}

Hi everyone,
This week in KanchiLUG we have scheduled an weekly discussion as online meeting on Sunday, {date} 16:00  -  17:00 IST

Meeting link : https://meet.jit.si/KanchiLugWeeklyDiscussion

Weekly discussion is an open and friendly discussion where topics related to Linux/FOSS technologies will be discussed. We will meet in the online jitsi meeting and discuss new linux things everyone explored this week and we chat about linux news and topics. If you are facing any issues with linux or any FOSS applications, you can also share your issues during the discussion. Our KanchiLUG community will help to debug or suggest some good alternatives.

Can join with any browser or JitSi android app.
All the Discussions are in Tamil.
'''
    return message

def talks_msg_generator(talk_list):
    talks_msg='''
    '''
    counter=0
    for item in talk_list:
        msg=f'''
Talk {counter}:
Topic : {item.topic}
Description : {item.description} 
Duration : {item.estduration}
Name : {item.name}
About : {item.about}
'''
        talks_msg+=msg 
        counter+=1
    return talks_msg

def mc_monthlymeeting(date, talks_msg):
    top_content=f'''
Subject: [KanchiLUG] Monthly Meeting - {date}

Hi everyone,
KanchiLUG's Monthly meet is scheduled as online meeting this week on Sunday, {date} 16:00 - 17:00 IST

Meeting link : https://meet.jit.si/KanchiLugMonthlyMeet

Can join with any browser or JitSi android app.
All the Discussions are in Tamil.

Talk Details'''
    footer=f'''
After Talks : Q&A, General discussion

About KanchiLUG : Kanchi Linux Users Group [ KanchiLUG ] has been spreading awareness on Free/Open Source Software (F/OSS) in Kanchipuram since November 2006.

Anyone can join! (Entry is free)
Everyone is welcome
Feel free to share this to your friends
--
Thanks and Regards,
Parameshwar Arunachalam
KanchiLUG Co-ordinator
Personal Email: stark20236@gmail.com
Mailing list: kanchilug@freelists.org
Repository : https://gitlab.com/kanchilug
Twitter handle: @kanchilug
    '''
    message=top_content + talks_msg + footer
    return message

def bc_monthlymeeting(date,talks_msg):
    top_content=f'''
Subject: Monthly Meeting - {date}

Hi everyone,
KanchiLUG's Monthly meet is scheduled as online meeting this week on Sunday, {date} 16:00 - 17:00 IST

Meeting link : https://meet.jit.si/KanchiLugMonthlyMeet

Can join with any browser or JitSi android app.
All the Discussions are in Tamil.

Talk Details'''
    message=top_content + talks_msg 
    return message

def fc_monthlymeeting(date,talks_msg):
    top_content=f'''
Hi everyone,
KanchiLUG's Monthly meet is scheduled as online meeting this week on Sunday, {date} 16:00 - 17:00 IST

Meeting link : https://meet.jit.si/KanchiLugMonthlyMeet

Can join with any browser or JitSi android app.
All the Discussions are in Tamil.

Talk Details'''
    message=top_content + talks_msg 
    title=f"KanchiLUG's Monthly meeting - {date}"
    return (message,title)

def mc_callforspeakers(date):
    message=f'''
Subject: [KanchiLUG] Call For Speakers- {date}

Hi All,
Kanchi Linux Users Group, Kanchipuram [ KanchiLUG ] has been spreading awareness on Free/Open Source Software (F/OSS) in Kanchipuram since November 2006

KanchiLUG Monthly meet is going to be held on upcoming {date} through an online meeting platform called Jitsi meet at 16:00 IST.

We are inviting speakers to give a talk on things they have been working on FOSS Technologies like Linux, Free/Libre/Open Source Softwares/Technologies, Open Source Programming Languages/Frameworks etc.

This is an open stage for talking about open source. You can be at any experience level (from beginners to advanced) . We are very happy to schedule your session and listen to your open source experience.

Follow the below steps to give a talk in this week's meeting:
Step 1: If you are already a member of KanchiLUG mailing list you can skip this step1
If you are not a member of KanchiLUG mailing list then,
Go to this link : https://kanchilug.wordpress.com/join-mailing-list/
Follow the procedure mentioned in that link to join the mailing list.
(Note: You must be a member of the mailing list to send a mail to the mailing list)

Step 2: send a mail to kanchilug@freelists.org with below mentioned details
Topic:
Description:
Duration:
Your Name:
About Yourself:

You will get a confirmation mail within 24 hrs.
Note: If you haven't received any reply mail within 24 hrs, you can remind me in my personal mail id : stark20236@gmail.com.

Entry is free!
Feel free to share this to your friends

--
Thanks and Regards,
Parameshwar Arunachalam
KanchiLUG Co-ordinator
Personal Email: stark20236@gmail.com
Mailing list: kanchilug@freelists.org
Repository : https://gitlab.com/kanchilug
Twitter handle: @kanchilug
    '''
    return message

def bc_callforspeakers(date):
    message=f'''
Subject: Call For Speakers - {date}

Hi All,
Kanchi Linux Users Group, Kanchipuram [ KanchiLUG ] has been spreading awareness on Free/Open Source Software (F/OSS) in Kanchipuram since November 2006

KanchiLUG Monthly meet is going to be held on upcoming {date} through an online meeting platform called Jitsi meet at 16:00 IST.

We are inviting speakers to give a talk on things they have been working on FOSS Technologies like Linux, Free/Libre/Open Source Softwares/Technologies, Open Source Programming Languages/Frameworks etc.

This is an open stage for talking about open source. You can be at any experience level (from beginners to advanced) . We are very happy to schedule your session and listen to your open source experience.

Follow the below steps to give a talk in this week's meeting:
Step 1: If you are already a member of KanchiLUG mailing list you can skip this step1
If you are not a member of KanchiLUG mailing list then,
Go to this link : https://kanchilug.wordpress.com/join-mailing-list/
Follow the procedure mentioned in that link to join the mailing list.
(Note: You must be a member of the mailing list to send a mail to the mailing list)

**Step 2:** send a mail to kanchilug@freelists.org with below mentioned details
Topic:
Description:
Duration:
Your Name:
About Yourself:

You will get a confirmation mail within 24 hrs.
Note: If you haven't received any reply mail within 24 hrs, you can remind me in my personal mail id : stark20236@gmail.com.

Entry is free!
Feel free to share this to your friends
'''
    return message
