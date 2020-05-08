import os 
msg = input('donner un msg : \n')
destination = input('donner l"adress : \n')
os.system("echo " + msg + " | msmtp " + destination )
