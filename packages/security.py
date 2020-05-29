"""
description package
This class performs three tasks, each task in the form of a method
The first way is to send a text message to the phone
The second method sends a text message to the e-mail
The third way is to send a file to an email. This file can contain a picture, an audio message, or something else
__version__ : 0.0.1
__autor__ : written by anaibia kadhem and mlawh imed
__teammates__ : no team
__date__ : 16/05/2020
"""
from twilio.rest import Client
import os
import json


class Security :
    '''
    
    '''
    def __init__(self, config_path):
        """
        this is the class constractor
        @param1 : self
        @type : 
        @param 2 : confing_path
        @type : json file
        @return : null
        description : It stores all the necessary information it needs
        in every way in the json file
        """
        config_file = open(config_path,'r')
        self.config = json.load(config_file)
        config_file.close()
        self.security_email = self.config["security_mail"]
        self.security_num =self.config["security_num"]
        self.account_sid = self.config["twilio_sid"]
        self.auth_token = self.config["twilio_token"]
        self.twilio_num = self.config["twilio_num"]
        try :
            self.client = Client(self.account_sid, self.auth_token)
        except :
            print("failed to connect to twilio account please check your connection or your configuration")
    def send_sms(self, msg, destination_num = None):
       
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
        
        if destination_email is None :
            destination_email = self.security_email
        os.system("echo " + body + " | msmtp " + destination_email )
    def send_file(self, msg, file_path, destination_email = None):
        
        if destination_email is None :
            destination_email = self.security_email
        os.system(" mpack -s " + msg + ' '  + file_path + ' ' + destination_email )
        
