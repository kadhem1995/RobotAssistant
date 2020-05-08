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
        self.config = json.load(config_file)
        config_file.close()
        self.security_email = self.config["security_email"]
        self.security_num =self.config["security_num"]
        self.account_sid = self.config["twilio_sid"]
        self.auth_token = self.config["twilio_token"]
        self.twilio_num = self.config["twilio_num"]
        try :
            self.client = Client(self.account_sid, self.auth_token)
        except :
            print("failed to connect to twilio account please check your connection or your configuration")
    def send_sms(self, msg, destination_num = None):
        '''
        to do
        ''' 
        if destination_num is None :
            destination_num = self.security_num
        message = self.client.messages \
            .create(
                 body = msg,
                 from_= self.twilio_num ,
                 to= destination_num
             )
        print(message.sid)
    def send_email(self, body, destination_email = None):
        '''
        to do
        '''
        if destination_email is None :
            destination_email = self.security_email
        os.system("echo " + body + " | msmtp " + destination_email )
    def send_file(self, msg, file_path, destination_email = None):
        '''
        to do
        '''
        if destination_email is None :
            destination_email = self.security_email
        os.system(" mpack -s " + msg + ' '  + file_path + ' ' + destination_email )
        
