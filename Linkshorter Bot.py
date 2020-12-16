#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import telebot
from telebot import types
from telebot import util
import re
import time
import logging
logging.basicConfig(filename='mybot.txt', level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

 
    

TOKEN = 'توکن'
bot = telebot.TeleBot(TOKEN)


def link(url):
   request = requests.get("https://api-ssl.bitly.com/v3/shorten?access_token=f2d0b4eabb524aaaf22fbc51ca620ae0fa16753d&longUrl={}".format(url))
   content = request.content
   pattern = re.compile('"url":"(.*?)"', re.M)
   links = re.findall(pattern, content)
   return links

@bot.message_handler(commands=['start'])
def start(m):
    msg = bot.reply_to(m, "خوش آمديد" + "\n" + "لطفا لينک خود را بفرستيد")

    
@bot.message_handler(content_types=['text'])
def process(m):   
   if m.text.startswith('htt'): 
      bot.send_message(m.chat.id, "لطفا صبر کنيد")
      bot.send_chat_action(m.chat.id, "typing")
      aa = link(m.text)
      bot.send_message(m.chat.id, aa)
   else:
      agi = bot.send_message(m.chat.id, "لينک شما اشتباه است لطفا دوباره بفرستيد" + "\n" + "example: https://google.com or http://google.com")
      bot.register_next_step_handler(agi, process)

 
   
bot.polling(True)


