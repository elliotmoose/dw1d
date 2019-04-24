# Requires Adafruit_Python_PN532

import binascii
import socket
import time
import signal
import sys
import pyrebase

import PN532

# PN532 configuration for a Raspberry Pi GPIO:

# GPIO 18, pin 12
CS   = 18
# GPIO 23, pin 16
MOSI = 23
# GPIO 24, pin 18
MISO = 24
# GPIO 25, pin 22
SCLK = 25

# Configure the key to use for writing to the MiFare card.  You probably don't
# need to change this from the default below unless you know your card has a
# different key associated with it.
CARD_KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

# Number of seconds to delay after reading data.
DELAY = 0.5

# Prefix, aka header from the card
HEADER = b'BG'

   

def close(signal, frame):
        sys.exit(0)

signal.signal(signal.SIGINT, close)

# Create and initialize an instance of the PN532 class
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()
pn532.SAM_configuration()

print('PN532 NFC RFID 13.56MHz Card Reader')


FIREBASE_ENDPOINT = 'https://basic-dc724.firebaseio.com/'
REFRESH_RATE = 60 #firebase calls are still a bottleneck

config = {
  "apiKey": "AIzaSyByqBZnJMeBo9CjNn111hRYWo34ipRIOwM",
  "authDomain": "basic-dc724.firebaseapp.com",
  "databaseURL": "https://basic-dc724.firebaseio.com/",
  "storageBucket": "basic-dc724.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()  

while True:
    # Wait for a card to be available
    uid = pn532.read_passive_target()
    # Try again if no card found
    if uid is None:
        continue
    
    #uidstr = str(uid)[12:][:-2]
    uidstr = uid.decode('latin-1')
    print('Card ID: {0}'.format(uid))
    print('Card ID: {0}'.format(uidstr))
    #get child
    
    if db.child('current').get().val() != None:
        print('Error: User in session. Please log out first')
        continue
    
    allstudents = db.child('students').get().val()
    
    for student in allstudents.values():
        if student['can_number'] == uidstr:  
            db.child('/').update({'current':student})
            print('Found and logged in student: {0}'.format(student['name']))
            

    # Found a card, now try to read block 4 to detect the block type
    #print('Card UID 0x{0}'.format(binascii.hexlify(uid)))
    # Authenticate and read block 4
    #if not pn532.mifare_classic_authenticate_block(uid, 4, PN532.MIFARE_CMD_AUTH_B,
    #                                              CARD_KEY):
    #    print('Failed to authenticate with card!')
    #    continue
    #data = pn532.mifare_classic_read_block(4)
    #if data is None:
    #    print('Failed to read data from card!')
    #    continue
    # Check the header
    #if data[0:2] !=  HEADER:
    #    print('Card is not written with proper block data!')
    #    continue
    # Parse out the block type and subtype
    #print('User Id: {0}'.format(int(data[2:8].decode("utf-8"), 16)))
    time.sleep(DELAY);
