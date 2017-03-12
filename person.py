#coding:UTF-8
import os,sys
import datetime,time

class person(object):
  def __init__(self,name,age,sex,major):
    self.name=name
    self.age=age
    self.sex=sex
    self.major=major

  def __del__(self):
    print "ByeBye"
  
  def show_one_birthday(name):
    #function to show one's birthday and when it's is birthday today, system will send him an e-mail to bless him
    
