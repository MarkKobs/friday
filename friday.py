import itchat, time
from itchat.content import *
import re
import os
from NetEaseMusicApi import interact_select_song #网易云音乐
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    #分析是谁发送过来的 who .要转发给friday
    who=itchat.search_friends(userName=msg.FromUserName)
    friday=itchat.search_friends(nickName='friday')[0]
    toUserName=friday.UserName
    print(who)
    if who.NickName!='friday':#假如不是friday发来的
        if who.RemarkName!='':
            itchat.send(msg='receive one message from '+who.RemarkName+":"+msg.text,toUserName=toUserName)
        else:
            itchat.send(msg='receive one message from '+who.NickName+":"+msg.text,toUserName=toUserName)
    #转发至friday，格式：
    #receive one message from（）：（）
    #from : @90525690fce670f4b4595353f00bcb061cce8e6f8d5cd7d314e07695c50b8f5e
    #what : msg.text
    elif 'wiki' in msg.text:#1.wiki
        url='https://en.m.wikipedia.org/wiki/'
        receive=re.sub("wiki ","",msg.text)
        list=receive.split(" ")
        content='%20'.join(list)
        msg.user.send(url+content)
    elif 'pic' in msg.text:#2.picture
        msg.user.send("later,i will sent you a picture")
        pass
    elif 'music' in msg.text:#3.music
        msg.user.send('http://music.163.com/song/media/outer/url?id=22452987.mp3')
        pass
    elif msg.text.startswith('hello') or msg.text.startswith('hi') or msg.text.startswith('friday'):
        itchat.send('hello,boss!',toUserName=toUserName)
        pass
    else:
        itchat.send('boss, you have not set the program on me to solve it.',toUserName=toUserName)

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))
if __name__=="__main__":
    itchat.auto_login(hotReload=True,enableCmdQR=2)
    itchat.run(True)

