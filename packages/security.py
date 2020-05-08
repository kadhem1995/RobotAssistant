from twilio.rest import Client
import smtplib
import os
import codecs,json


class Security :
    def __init__(self, config_path):
        '''
        to do
        '''
        config_file = open(config_path,'r')
        config_contact = json.load(config_file)
        self.email ="kadhemanaibi0@gmail.com"
        self.num_tel ="+21652417178"
        self.account_sid = 'AC11ba230f617be5f89cf842008d12554a'
        self.auth_token = 'c74816f583c085c53daae27bfecf9733'
        self.num='+18452445557'
        slef.msg_sms="helllllo"
        slef.msg_email="helllllo"
        self.path_file=""
        k = open("contact.json",'w')
        json.dump(self.data,k)
        k.close()
    def send_sms(self, msg, destination_num):
        '''
        to do
        '''
        
        
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
            .create(
                 body = self.msg_sms,
                 from_= self.num_tel ,
                 to= self.num
             )

        print(message.sid)
    def send_email(self):
        '''
        to do
        '''
         
        msg = self.meg_email
        destination_email = self.email
        os.system("echo " + msg + " | msmtp " + destination )
    def send_file(self,parametre):
        '''
        to do
        '''
        path = self.path_file
        destination_email = self.email
        os.system(" mpack -s “Attachments with mpack” "+path  + destination )
        
