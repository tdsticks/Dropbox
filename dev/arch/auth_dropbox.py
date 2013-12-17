from splinter import *

import Credentials

from dropbox import rest, session
from dropbox import client as dbclient

import time

import os

C                       = Credentials.Credentials()

# Initiate Dropbox API
APP_KEY                 = C.KEY
APP_SECRET              = C.SECRET

ACCESS_TYPE             = 'dropbox'

emailDropbox            = C.usr
passwordDropbox         = C.pwd

sess                    = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
request_token           = sess.obtain_request_token()

urlDropbox              = sess.build_authorize_url(request_token)
#print urlDropbox


def phantomjsOAuth():
    # Target url
    print 'Target url: ', urlDropbox

    browser             = Browser('phantomjs')
    print 'Starting phantomjs browser'
    print 'Visiting url'
    browser.visit(urlDropbox)

    # Email form
    print 'Is the email form present? ', browser.is_element_present_by_id('login_email')
    print 'Filling email form'
    browser.find_by_id('email-field').first.find_by_id('login_email').first.fill(emailDropbox)
    print 'Email form successfully filled'

    # Password form
    print 'Is the password form present? ', browser.is_element_present_by_id('login_password')
    print 'Filling password form'
    browser.find_by_id('login_password').first.fill(passwordDropbox)
    print 'Password form successfully filled'

    # Find login submit button
    print 'Is the "Submit" button present?', browser.is_element_present_by_name('login_submit_dummy')
    submitButton        = browser.is_element_present_by_name('login_submit_dummy')


    if submitButton == True:

        print 'Pausing for 5 seconds to avoid clicking errors'
        
        time.sleep(5)

        print 'Attempting to click the "Submit" button in order to login'
        browser.find_by_name('login_submit_dummy').first.click()
        print '"Submit" button successfully clicked'

        # Allow connection with Dropbox
        print 'Is the "Allow" button present?', browser.is_element_present_by_css('.freshbutton-blue')
        allowButton     = browser.is_element_present_by_css('.freshbutton-blue')


        if allowButton == True:

            print 'The "Allow" button is present, attempting to click..'
            browser.find_by_css('.freshbutton-blue').click()
            
            browser.quit()

            dropboxCode()

        else:
            print 'The "Allow" button is not present, quitting.'
            browser.quit()

    else:
        print 'The "Submit" button was not present, quitting.'
        browser.quit()


def dropboxCode():
    # The rest of the Dropbox code
    # This will fail if 'Allow' wasn't clicked
    access_token        = sess.obtain_access_token(request_token)

    client              = dbclient.DropboxClient(sess)
    print "linked account:", client.account_info()


    #src_path            = "/Users/steves/Dropbox/dev/RaspberryPi/projects/Dropbox/dev/camera"
    src_path            = "/home/pi/camera"

    # List files from path, then loop through them adding to Dropbox
    files               = listfiles(src_path)

    for src_file in files:

        src_fullpath    = src_path + "/" + src_file
        print "src_fullpath:",src_fullpath

        f               = open(src_fullpath)

        dest_file_path  = '/camera/' + src_file
        print "dest_file_path:",dest_file_path

        response        = client.put_file(dest_file_path, f)
        print "uploaded:", response


    # Try keeping this open for multiple files (delayed loop),
    # then fire unlink
    sess.unlink()


def listfiles(src):
    #print "src:",src

    if os.path.isdir(src):
        print src, "is directory"
    else:
        print src, "is NOT directory"

    for root, dirs, files in os.walk(src):

        #print "root:",root
        #print "dirs:",dirs
        print "files:",files

        return files


if __name__ == "__main__":

    phantomjsOAuth()
