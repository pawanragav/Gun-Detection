# -*- coding: utf-8 -*-

def msg():
    from pytz import timezone 
    from datetime import datetime

    ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')

    from twilio.rest import Client
    client = Client(account_sid, auth_token)


    message = client.messages .create(
                 body=  f'Weapons detected!! at {ind_time}',   
                 from_ =  +12059418686,
                 to = +918610107552
             )

    return message.sid
