#DO READ EVERY COMMENT IN THIS PROGRAM TO UNDERSTAND ITS WORKING...
#THIS CODE CANNOT SEND SMS AS I CANNOT SHARE MY TWILIO CREDENTIALS LIKE AUTHORISED TOKEN, SO TO USE THIS CODE JUST REPLACE MY TWILIO CREDENTIALS LIKE  account_sid (in line 75) auth_token(76) twilio number(in line 83)
#YOU WILL GET THE CREDENTIALS AFTER REGISTERING AND VERIFYING YOURSELF AT TWILIO, YOU CAN ONLY SEND SMS TO VERIFIED NUMBERS AT TWILIO, TO SEND SMS TO EVERY NUMBER YOU MUST UPGRADE TO PREMIUM


#importing required libraries 
import sqlite3
import pandas as pd
from twilio.rest import Client



#getting connected to the data base
conn=sqlite3.connect("DHOLAKPUR BANK DATABASE .db")


#creating the table containing account holder,account number,phone number, account balalnce columns
conn.execute('''CREATE TABLE BANK_OF_DHOLAKPUR2
              (ACCOUNT_HOLDER                      TEXT                       NOT NULL,
               ACCOUNT_NUMBER                      VARCHAR                    NOT NULL,
               PHONE _UMBER                        INT                        NOT NULL,
               ACCOUNT_BALANCE                     INT                        NOT NULL
               )''')

#creating a data  with all details like account holder, phone number etc

bank_data={
    "ACCOUNT_HOLDER":["SANJAY JADHAV","USHA JADHAV","KARAN JADHAV","ROHAN JADHAV","DEEKSHA JADHAV","ADWAIT","AMOGH","ANJAN","AYAAN","CHAITANYA","CHIKU","DIKSHANT","MITHIL","GAJALA","HRISHIK","KETHAN","KIREETI","LINGABABU","MAYOOR","NITHIN","PRATHAM","PRATIK","RAMARAJU","RUTVIK","SAI CHARAN","SAI TEJA","SANDESH","SATHVIK","SAURAV PAWAR","SAURABH KINNERA","SHANKAR","THARUN","THOMAS","VIJAY","YASHWANTH SIMHA","LIKITH","SANDEEP","MURALI","ANVESH","CHETAN KUMOR","MANOHAR SAI","SAI CHARAN PATEL","SATISH","SIDDHARTH","SRI RAM","UMESH","VARSHIT REDDY","ANISH","MANISH","ROHAN","MOKSHIT"],
    "ACCOUNT_NUMBER":["AXXXXXX001",   "AXXXXXX002", "AXXXXXX003",  "AXXXXXX004",  "AXXXXXX005",    "AXXXXXX006", "AXXXXXX007","AXXXXXX008","AXXXXXX009","AXXXXXX010","AXXXXXX011","AXXXXXX012","AXXXXX013","AXXXXXX014","AXXXXXX015","AXXXXXX016","AXXXXXX017","AXXXXXX018","AXXXXXX019","AXXXXXX020","GXXXXXX021","GXXXXXX022","GXXXXXX023","GXXXXXX024","GXXXXXX025","GXXXXXX026","GXXXXXX027","GXXXXXX028","GXXXXXX029","GXXXXXX030","GXXXXXX031","GXXXXXX032","GXXXXXX033","GXXXXXX034","GXXXXXX035","GXXXXXX036","GXXXXXX037","GXXXXXX038","GXXXXXX039","GXXXXXX040","GXXXXXX041","GXXXXXX042","GXXXXXX043","GXXXXXX045","GXXXXXX046","GXXXXXX047","GXXXXXX048","GXXXXXX049","GXXXXXX050","GXXXXXX044","GXXXXXX051"],
    "PHONE_UMBER":[9291641692,9398847273,9182208408,7396815192,7893814692,7794870029,6304412202,7036787606,8897848801,7660004748,7620864209,6006537255,9391128584,8790778050,7036805472,9392348141,7337230309,9515819306,9398774076,6304650935,9796419183,9284712550,8179107535,9059224146,7386603298,9553248060,8767120820,7671867176,7020103751,7558779488,9032777103,7386633696,9542758814,9347371439,8639260110,9849002951,8341226539,9908092442,6305851653,8309177158,6305952092,9032901983,8978115997,8074244545,8074561818,9819793025,8978546082,6301823514,9000365585,8919972570,6300283558],
    "ACCOUNT_BALANCE":[10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000]
    
}

#transforming the data to data frame
# to update bank balance you have to enter account holder's name , so print and this data frame and look for correct account holder's name other wise it will lead to error
accounts_df=pd.DataFrame(bank_data,columns=["ACCOUNT_HOLDER","ACCOUNT_NUMBER","PHONE_UMBER","ACCOUNT_BALANCE"],index=range(1,52))


#transforming the data to data frame
# to update bank balance you have to enter account holder's name , so print and this data frame and look for correct account holder's name other wise it will lead to error
accounts_df=pd.DataFrame(bank_data,columns=["ACCOUNT_HOLDER","ACCOUNT_NUMBER","PHONE_UMBER","ACCOUNT_BALANCE"],index=range(1,52))

conn.commit()

c=conn.cursor()

#function to update the account the balance and send SMS to account holder
def update_account_balance():
    account_holder_name=str(input("enter the account holder's name in CAPITALS :"))
    c.execute(f'''SELECT  ACCOUNT_BALANCE,ACCOUNT_NUMBER,PHONE_UMBER FROM BANK_OF_DHOLAKPUR WHERE ACCOUNT_HOLDER="{account_holder_name}" ''')
    x=c.fetchall()
    print(x)
    account_holders_phone_number=x[0][2]
    print(account_holders_phone_number)
    c.execute(f'''SELECT ACCOUNT_NUMBER FROM BANK_OF_DHOLAKPUR WHERE PHONE_UMBER={account_holders_phone_number} ''')
    account_number_for_sms_before_strip=c.fetchall()
    
    account_number_for_sms= account_number_for_sms_before_strip[0][0]
    print(account_number_for_sms)
    
    print(f"THE ACCOUNT NUMBER OF {account_holder_name} is {x[0][1].strip()} AND THE PHONE NUMBER IS {x[0][2]}")
    y=x[0][0]
    
    print("THE ACCOUNT BALANCE OF ",account_holder_name,"is :",y)
    c.execute(f'''UPDATE BANK_OF_DHOLAKPUR SET ACCOUNT_BALANCE={y+(int(input("PLEASE ENTER THE AMOUNT TO BE ADDED OR DEDUCTED(IF DEDUCTED PLEASE INCLUDE - SIGN)")))} WHERE ACCOUNT_HOLDER="{account_holder_name}" ''')
    conn.commit()
    c.execute(f'''SELECT ACCOUNT_BALANCE FROM BANK_OF_DHOLAKPUR WHERE ACCOUNT_HOLDER="{account_holder_name}" ''')
    updated_balance= c.fetchone()
    print(f"THE ACCOUNT BALANCE OF {account_holder_name} is : {updated_balance[0]}")
    
    
    
    
    account_sid="ACa7c39a50618f0cc2fd11d0f785b9c83f"
    auth_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  #THIS IS MY AUTH TOKEN OF TWILIO PLATFORM THROUGH WHICH SMS WOULD BE SENT, IT CANNOT BE SHARED HERE.



    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+91"+f"{str(account_holders_phone_number)}",
        from_='+13197741739',
         body=f'''DEAR {account_holder_name} THIS IS FROM BANK OF DHOLAKPUR YOUR CURRENT ACCOUNT BALANCE(WITH ACCOUNT NUMBER {account_number_for_sms}) AFTER CREDITION OR DEBITION IS {updated_balance[0]}'''
    
    )

    print(message.sid)

print(accounts_df)
    

#before running this run the above and print the accounts_df to know correct names of account holders
#all the account holders are my classmates so do not update account balance of any random account holder
# kindly update either account balance of ROHAN JADHAV  only YOU CANT SEND SMS TO ANY OTHER NUMBER
# getting SM8c2041xxxxxxxx like output after runnig this function means the SMS is sent
#AFTER UPDATING THE ACCOUNT BALANCE IN DATAFRAME WILL NOT UPDATE BUT THE ACCOUNT BALANCE IN THE DATABSE WILL BE UPDATED
update_account_balance()
