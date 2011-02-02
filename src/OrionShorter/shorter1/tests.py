# -*- coding: UTF-8 -*-

'''
Created on 29/01/2011

@author: ThiagoP
'''
#python imports
import unittest, urllib2


class Test(unittest.TestCase):

    def testURL1(self):
        url  = "http://google.com/"
        response = urllib2.urlopen("http://localhost:8080/oshtr/short?target=" + url)      

        print "URL: " + url
        print "SHORTED_URL: " + response.read()
        
    def testSameURL1(self):
        url  = "http://google.com/"
        response = urllib2.urlopen("http://localhost:8080/oshtr/short?target=" + url)

        print "URL: " + url
        print "SHORTED_URL: " + response.read()
    
    def testURL2(self):
        url  = "http://google.com/mail"
        response = urllib2.urlopen("http://localhost:8080/oshtr/short?target=" + url)
       
        print "URL: " + url
        print "SHORTED_URL: " + response.read()
    
    def testURLAlreadyShorted(self):
        url  = "http://localhost:8080/oshtr/"
        response = urllib2.urlopen("http://localhost:8080/oshtr/short", url)
        
        print "URL: " + url
        print "SHORTED_URL: " + response.read()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()