 

from kivy.metrics import sp
from kivy.logger import Logger , LoggerHistory
import time
 
from kivy.uix.widget import Widget
from config.hippoclasses import Models
from config.hippoclasses import ConfigMyapp
from kivy.clock import mainthread
from kivy.core.clipboard import Clipboard
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.button import  MDFlatButton
from kivymd.uix.dialog import MDDialog
# from kivy.core.audio import SoundLoader
from kivy.core.window import Window
# import asyncio
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import *
from kivymd.toast import toast
from functools import partial
import os
import sys
import traceback

from threading import Thread
from kivy.utils import platform
import json
from kivy.properties import ObjectProperty
## Android settings defaeb 5ed289  58b983
primary_ext_storage = os.path.dirname(os.path.abspath(__file__))
from kivmob import KivMob, TestIds
if platform == 'android':
    import android
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE, Permission.ACCESS_NETWORK_STATE, Permission.INTERNET, Permission.WAKE_LOCK])
    from android.storage import primary_external_storage_path
    primary_ext_storage = primary_external_storage_path()
    from jnius import autoclass
    MediaPlayer = autoclass('android.media.MediaPlayer')


r = '1'
from os import environ
from certifi import where as certifi_where
environ['SSL_CERT_FILE'] = certifi_where()
from ssl import get_default_verify_paths
# import urllib.request as urlrq
# resp = urlrq.urlopen('https://www.tublm.com/', context=ssl.create_default_context(cafile=certifi.where()))
get_default_verify_paths()
 
gcontent=[]
with open('settings.json',  'r') as file:
    gcontent = json.load(file)



Beat_wav=MediaPlayer()
Beat_wav.setDataSource(gcontent["Beat.wav"])
Beat_wav.prepare()
Beat_wav.setLooping(False)

EmotionalDamage_wav=MediaPlayer()
EmotionalDamage_wav.setDataSource(gcontent["EmotionalDamage.wav"])
EmotionalDamage_wav.prepare()
EmotionalDamage_wav.setLooping(False)
follow_wav=MediaPlayer()
follow_wav.setDataSource(gcontent["follow.wav"])
follow_wav.prepare()
follow_wav.setLooping(False)
Gentleman_wav=MediaPlayer()
Gentleman_wav.setDataSource(gcontent["Gentleman.wav"])
Gentleman_wav.prepare()
Gentleman_wav.setLooping(False)
Laugh_wav=MediaPlayer()
Laugh_wav.setDataSource(gcontent["Laugh.wav"])
Laugh_wav.prepare()
Laugh_wav.setLooping(False)
like_wav=MediaPlayer()
like_wav.setDataSource(gcontent["like.wav"])
like_wav.prepare()
like_wav.setLooping(False)
love_wav=MediaPlayer()
love_wav.setDataSource(gcontent["love.wav"])
love_wav.prepare()
love_wav.setLooping(False)
nope_wav=MediaPlayer()
nope_wav.setDataSource(gcontent["nope.wav"])
nope_wav.prepare()
nope_wav.setLooping(False)
Panda_wav=MediaPlayer()
Panda_wav.setDataSource(gcontent["Panda.wav"])
Panda_wav.prepare()
Panda_wav.setLooping(False)
Rose_wav=MediaPlayer()
Rose_wav.setDataSource(gcontent["Rose.wav"])
Rose_wav.prepare()
Rose_wav.setLooping(False)
share_wav=MediaPlayer()
share_wav.setDataSource(gcontent["share.wav"])
share_wav.prepare()
share_wav.setLooping(False)
Welcome_wav=MediaPlayer()
Welcome_wav.setDataSource(gcontent["Welcome.wav"])
Welcome_wav.prepare()
Welcome_wav.setLooping(False)
comment1_wav=MediaPlayer()
comment1_wav.setDataSource(gcontent["comment1.wav"])
comment1_wav.prepare()
comment1_wav.setLooping(False)
comment2_wav=MediaPlayer()
comment2_wav.setDataSource(gcontent["comment2.wav"])
comment2_wav.prepare()
comment2_wav.setLooping(False)
comment3_wav=MediaPlayer()
comment3_wav.setDataSource(gcontent["comment3.wav"])
comment3_wav.prepare()
comment3_wav.setLooping(False)



models = Models()
models.Builder.load_file('echo.kv')
@mainthread
def show_toast( message):
    # show_notification(message)
    toast(message)



gdialog = None
gdialogopen = None
def Sound( sound):
    global Beat_wav    
    global EmotionalDamage_wav 
    global follow_wav  
    global Gentleman_wav   
    global Laugh_wav   
    global like_wav    
    global love_wav    
    global nope_wav    
    global Panda_wav   
    global Rose_wav    
    global share_wav   
    global Welcome_wav 

    global comment1_wav 
    global comment2_wav 
    global comment3_wav 
    if(sound =="Beat.wav"):
        Beat_wav.start()
    if(sound =="EmotionalDamage.wav"):
        EmotionalDamage_wav.start()
    if(sound =="follow.wav"):
        follow_wav.start()
    if(sound =="Gentleman.wav"):
        Gentleman_wav.start()
    if(sound =="Laugh.wav"):
        Laugh_wav.start()
    if(sound =="like.wav"):
        like_wav.start()
    if(sound =="love.wav"):
        love_wav.start()
    if(sound =="nope.wav"):
        nope_wav.start()
    if(sound =="Panda.wav"):
        Panda_wav.start()
    if(sound =="Rose.wav"):
        Rose_wav.start()
    if(sound =="share.wav"):
        share_wav.start()
    if(sound =="Welcome.wav"):
        Welcome_wav.start()
    if(sound =="comment1.wav"):
        comment1_wav.start()
    if(sound =="comment2.wav"):
        comment2_wav.start()
    if(sound =="comment3.wav"):
        comment3_wav.start()
    # show_notification(message)
    # toast(sound)

 
class LivechoP(models.BoxLayout):
    ...


class Livecholikewav(models.BoxLayout):
    text = gcontent["like.wav"].replace(primary_ext_storage, "")
class LivechoBeatwav(models.BoxLayout):
    text = gcontent["Beat.wav"].replace(primary_ext_storage, "")
class LivechoEmotionalDamagewav(models.BoxLayout):
    text = gcontent["EmotionalDamage.wav"].replace(primary_ext_storage, "")
class LivechoGentlemanwav(models.BoxLayout):
    text = gcontent["Gentleman.wav"].replace(primary_ext_storage, "")
class LivechoLaughwav(models.BoxLayout):
    text = gcontent["Laugh.wav"].replace(primary_ext_storage, "")
class LivechoPandawav(models.BoxLayout):
    text = gcontent["Panda.wav"].replace(primary_ext_storage, "")
class LivechoRosewav(models.BoxLayout):
    text = gcontent["Rose.wav"].replace(primary_ext_storage, "")
class LivechoWelcomewav(models.BoxLayout):
    text = gcontent["Welcome.wav"].replace(primary_ext_storage, "")
class Livechofollowwav(models.BoxLayout):
    text = gcontent["follow.wav"].replace(primary_ext_storage, "")
class Livecholovewav(models.BoxLayout):
    text = gcontent["love.wav"].replace(primary_ext_storage, "")
class Livechonopewav(models.BoxLayout):
    text = gcontent["nope.wav"].replace(primary_ext_storage, "")
class Livechosharewav(models.BoxLayout):
    text = gcontent["share.wav"].replace(primary_ext_storage, "")


class Livechocomment1wav(models.BoxLayout):
    text = gcontent["comment1.wav"].replace(primary_ext_storage, "")
    textc = ""
    if os.path.isfile("1.txt"):
        with open("1.txt", "r") as f:
            textc = f.read()

class Livechocomment2wav(models.BoxLayout):
    text = gcontent["comment2.wav"].replace(primary_ext_storage, "")
    textc = ""
    if os.path.isfile("2.txt"):
        with open("2.txt", "r") as f:
            textc = f.read()

class Livechocomment3wav(models.BoxLayout):
    text = gcontent["comment3.wav"].replace(primary_ext_storage, "")
    textc = ""
    if os.path.isfile("3.txt"):
        with open("3.txt", "r") as f:
            textc = f.read()
class LivechoL(models.BoxLayout):
    ...








class LivechoU(models.BoxLayout):
    ...

class LivechoS(models.BoxLayout):
    ...

class LivechoV(models.BoxLayout):
    ...




class Contentopen(models.BoxLayout):
    pass
class Content(models.BoxLayout):
    pass

class PrimaryView(models.BoxLayout):
    # ads = KivMob("")#(TestIds.APP)
    def __init__(
        self, **kw
        ):
        super(PrimaryView, self).__init__(**kw)
        Window.bind(on_keyboard=self.events)
        self.client = None
        # self.echothread = None
        self.manager_open = False
        self.file_manager =  MDFileManager()
        # self.ads.new_banner("" ,top_pos=False) #(TestIds.BANNER ,top_pos=False)
        # self.ads.new_interstitial("")#TestIds.INTERSTITIAL
        # self.ads.request_banner()
        # self.ads.show_banner()


 


    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def popup(self):
        global gdialog
        gdialog = MDDialog(
        size_hint=(0.86, None),
        auto_dismiss=False,
        type="custom",
        pos_hint={'center_x':0.5,'center_y':0.52},
        content_cls=Content(),
        
        )
        gdialog.open() 

    def popupopen(self):
        global gdialogopen
        gdialogopen = MDDialog(
        size_hint=(0.86, None),
        auto_dismiss=False,
        type="custom",
        pos_hint={'center_x':0.5,'center_y':0.52},
        content_cls=Contentopen(),
        
        )
        gdialogopen.open()  


    def paste(
        self, object, *args
    ):
        object.text = Clipboard.paste()

   
    @mainthread
    def show_toast(self, message):
        # show_notification(message)
        toast(message)

 
        

    def CONNECTpaste(
        self, object, *args
    ):

        # 15ad6b#15ad6b
        #14aa69
        # blessedbykidd
        # @Sparklesnmoreco

        # Jay.H:
        # @Luraroshop7
        # @licc180
        # Jay.H:
        # @envybyalisa
        # "@funbill1995"

        if len(object.text.strip())<=1:
            toast('Please enter VALID Room ID!')
            return



        client: TikTokLiveClient = TikTokLiveClient(unique_id=object.text)
        self.popup()




        @client.on("like")
        async def on_like(event: LikeEvent):
            if event.likeCount > 0:
                Sound('like.wav')
                # if sound2:                    sound2.start()



        # Define how you want to handle specific events via decorator
        @client.on("connect")
        async def on_connect(_: ConnectEvent):
            global gdialog
            if gdialog:
                gdialog.dismiss()

            show_toast("connect live room success")
            Sound('Welcome.wav')
            # if sound2:                sound2.start()




        @client.on("live_end")
        async def on_connect(event: LiveEndEvent):
            # print(f"Livestream ended :(")


        @client.on("share")
        async def on_share(event: ShareEvent):
            Sound('share.wav')
            # if sound2:                sound2.start()

        @client.on("join")
        async def on_join(event: JoinEvent):
            # Clock.schedule_once(self.start_test, 0)
            # toast("join"+"-zyl-"+ str(event.user.uniqueId ))    
            # r.publish('bd', "join"+"-zyl-"+ str(event.user.uniqueId ))
            #show_toast("join"+"-zyl-"+ str(event.user.uniqueId ))

            # Thread(
            # target=show_toast,
            # args=(),
            # daemon=True,
            # ).start()

        @client.on("follow")
        async def on_follow(event: FollowEvent):
            Sound("follow.wav")
            # if sound2:                sound2.start()
            # r.publish('bd', "msg"+"-zyl-"+str(event.user.uniqueId)+"-zyl-"+str(event.user.uniqueId)+"-zyl-"+"Thanks for following," +str(event.user.uniqueId)+"!");
         

        # Notice no decorator?
        async def on_comment(event: CommentEvent):
            # global r
            # r.publish('bd', "msg"+"-zyl-"+str(event.user.uniqueId)+"-zyl-"+str(event.user.uniqueId)+"-zyl-"+str(event.comment))
            # if(str(event.comment))

            if os.path.isfile("1.txt"):
                with open("1.txt", "r") as f:
                    textc = f.read()
                    if textc in str(event.comment):
                        Sound('comment1.wav')



            if os.path.isfile("2.txt"):
                with open("2.txt", "r") as f:
                    textc = f.read()
                    if textc in str(event.comment):
                        Sound('comment2.wav')



            if os.path.isfile("3.txt"):
                with open("3.txt", "r") as f:
                    textc = f.read()
                    if textc in str(event.comment):
                        Sound('comment3.wav')





        # Define handling an event via "callback"
        client.add_listener("comment", on_comment)
        @client.on("gift")
        async def on_gift(event: GiftEvent):
            if event.gift.extended_gift.name == "Rose":
                Sound("Rose.wav")
            elif event.gift.extended_gift.name == "Panda":
                Sound("Panda.wav")
            elif event.gift.extended_gift.name == "Finger Heart" or event.gift.extended_gift.name == "Vingerhart":
                Sound("love.wav")
            elif event.gift.extended_gift.name == "Mini Speaker" or  event.gift.extended_gift.name == "Headphones":
                Sound("Beat.wav")
            elif event.gift.extended_gift.name == "TikTok" or event.gift.extended_gift.name == "Choc Chip Cookie":
                Sound("Gentleman.wav")
            elif event.gift.extended_gift.name == "Welcome" or event.gift.extended_gift.name == "Daisies" or  event.gift.extended_gift.name == "Gift Box":
                Sound("Welcome.wav")
            elif event.gift.extended_gift.name == "Wishing Bottle" or  event.gift.extended_gift.name == "May" or   event.gift.extended_gift.name == "Doughnut" or   event.gift.extended_gift.name == "Coffee":
                Sound("Laugh.wav")
            else:
                Sound("EmotionalDamage.wav")




        result1 =''
        def yzinyer(name: str):
            global gdialog
            try:
                client.run()
            except:
                if gdialog:
                    gdialog.dismiss()
                    traceback.print_exc()
                show_toast("connect live room failed")
            
        Thread(
            target=yzinyer,
            args=(result1,),
            daemon=True,
        ).start()
        # if self.echothread and self.echothread.IsAlive():
            # self.echothread._Thread__stop() 


        # if __name__ == '__main__':
        #     # Run the client and block the main thread
        #     # await client.start() to run non-blocking
        #     client.run()


    def file_play(
        self, object, *args
    ):

        global Beat_wav    
        global EmotionalDamage_wav 
        global follow_wav  
        global Gentleman_wav   
        global Laugh_wav   
        global like_wav    
        global love_wav    
        global nope_wav    
        global Panda_wav   
        global Rose_wav    
        global share_wav   
        global Welcome_wav 
        global comment1_wav 
        global comment2_wav 
        global comment3_wav 
            
        sound = object.texto
        if(sound =="Beat.wav"):
            Beat_wav.start()
        if(sound =="EmotionalDamage.wav"):
            EmotionalDamage_wav.start()
        if(sound =="follow.wav"):
            follow_wav.start()
        if(sound =="Gentleman.wav"):
            Gentleman_wav.start()
        if(sound =="Laugh.wav"):
            Laugh_wav.start()
        if(sound =="like.wav"):
            like_wav.start()
        if(sound =="love.wav"):
            love_wav.start()
        if(sound =="nope.wav"):
            nope_wav.start()
        if(sound =="Panda.wav"):
            Panda_wav.start()
        if(sound =="Rose.wav"):
            Rose_wav.start()
        if(sound =="share.wav"):
            share_wav.start()
        if(sound =="Welcome.wav"):
            Welcome_wav.start()
        if(sound =="comment1.wav"):
            comment1_wav.start()
        if(sound =="comment2.wav"):
            comment2_wav.start()
        if(sound =="comment3.wav"):
            comment3_wav.start()

        # self.ads.new_banner("",top_pos=False ) #(TestIds.BANNER ,top_pos=False)
        # self.ads.request_banner()
        # self.ads.show_banner()


    def _validate1(
        self, object, *args
    ):
        with open("1.txt", "w") as f:
            f.write(f"{object.text}")



    def _validate2(
        self, object, *args
    ):
        with open("2.txt", "w") as f:
            f.write(f"{object.text}")



    def _validate3(
        self, object, *args
    ):
        with open("3.txt", "w") as f:
            f.write(f"{object.text}")




    def file_manager_open(
        self, object, *args
    ):

    # def choose_dir(self, *args):
        ''' create filemanager and open in user's home directory
        '''
        # self.file_manager = MDFileManager()
        self.popupopen()
        self.file_manager.exit_manager = partial(self.exit_filemanager, self.file_manager, object)
        self.file_manager.select_path = partial(self.handle_selection, self.file_manager, object)
        self.file_manager.ext=['.wav', '.ogg', '.mp3', '.m4a', '.mp4']
        self.manager_open = True
        # self.ads.new_banner("",top_pos=False ) #(TestIds.BANNER ,top_pos=True)
        # self.ads.request_banner()
        # self.ads.show_banner()
        self.file_manager.show(primary_ext_storage)
        global gdialogopen
        if gdialogopen:
            gdialogopen.dismiss()

    def exit_filemanager(self, fm, ob,*args):
        self.manager_open = False
        fm.close()



    def handle_selection(self, fm, ob, datadir):

        # toast(ob.texto + datadir)
        if os.path.isfile(datadir) is True:
            pass
        else:
            toast('Please select audio file')
            return
        
        global Beat_wav    
        global EmotionalDamage_wav 
        global follow_wav  
        global Gentleman_wav   
        global Laugh_wav   
        global like_wav    
        global love_wav    
        global nope_wav    
        global Panda_wav   
        global Rose_wav    
        global share_wav   
        global Welcome_wav 
        global comment1_wav 
        global comment2_wav 
        global comment3_wav 

        toast(ob.texto)

        content=[]
        with open('settings.json',  'r') as file:
            content = json.load(file)
            


  
        if(ob.texto =="Beat.wav"):
            Beat_wav=MediaPlayer()
            Beat_wav.setDataSource(datadir)
            Beat_wav.prepare()
            Beat_wav.setLooping(False)
        if(ob.texto =="EmotionalDamage.wav"):
            EmotionalDamage_wav=MediaPlayer()
            EmotionalDamage_wav.setDataSource(datadir)
            EmotionalDamage_wav.prepare()
            EmotionalDamage_wav.setLooping(False)
        if(ob.texto =="follow.wav"):
            follow_wav=MediaPlayer()
            follow_wav.setDataSource(datadir)
            follow_wav.prepare()
            follow_wav.setLooping(False)
        if(ob.texto =="Gentleman.wav"):
            Gentleman_wav=MediaPlayer()
            Gentleman_wav.setDataSource(datadir)
            Gentleman_wav.prepare()
            Gentleman_wav.setLooping(False)
        if(ob.texto =="Laugh.wav"):
            Laugh_wav=MediaPlayer()
            Laugh_wav.setDataSource(datadir)
            Laugh_wav.prepare()
            Laugh_wav.setLooping(False)
        if(ob.texto =="like.wav"):
            like_wav=MediaPlayer()
            like_wav.setDataSource(datadir)
            like_wav.prepare()
            like_wav.setLooping(False)
        if(ob.texto =="love.wav"):
            love_wav=MediaPlayer()
            love_wav.setDataSource(datadir)
            love_wav.prepare()
            love_wav.setLooping(False)
        if(ob.texto =="nope.wav"):
            nope_wav=MediaPlayer()
            nope_wav.setDataSource(datadir)
            nope_wav.prepare()
            nope_wav.setLooping(False)
        if(ob.texto =="Panda.wav"):
            Panda_wav=MediaPlayer()
            Panda_wav.setDataSource(datadir)
            Panda_wav.prepare()
            Panda_wav.setLooping(False)
        if(ob.texto =="Rose.wav"):
            Rose_wav=MediaPlayer()
            Rose_wav.setDataSource(datadir)
            Rose_wav.prepare()
            Rose_wav.setLooping(False)
        if(ob.texto =="share.wav"):
            share_wav=MediaPlayer()
            share_wav.setDataSource(datadir)
            share_wav.prepare()
            share_wav.setLooping(False)
        if(ob.texto =="Welcome.wav"):
            Welcome_wav=MediaPlayer()
            Welcome_wav.setDataSource(datadir)
            Welcome_wav.prepare()
            Welcome_wav.setLooping(False)
        if(ob.texto =="comment1.wav"):
            comment1_wav=MediaPlayer()
            comment1_wav.setDataSource(datadir)
            comment1_wav.prepare()
            comment1_wav.setLooping(False)
        if(ob.texto =="comment2.wav"):
            comment2_wav=MediaPlayer()
            comment2_wav.setDataSource(datadir)
            comment2_wav.prepare()
            comment2_wav.setLooping(False)
        if(ob.texto =="comment3.wav"):
            comment3_wav=MediaPlayer()
            comment3_wav.setDataSource(datadir)
            comment3_wav.prepare()
            comment3_wav.setLooping(False)
    

        content[ob.texto]=datadir
        with open('settings.json', 'w') as w_json:
            json.dump(content, w_json, indent=4, sort_keys=True)
        ob.text = datadir.replace(primary_ext_storage, "")
        self.manager_open = False
        fm.close()
 
 





 

 


class Livecho(models.Liveapp):
    dialog_restart = None
    __version__ = "1.01"
    def load_logs(self):
        self.root.ids.logs_content.text = '\n'.join([l.msg for l in LoggerHistory.history])

    def build(
        self
    ):  

        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.accent_palette = 'Yellow'
        return PrimaryView()

    def reset_APP(
        self, object, *args
    ):
        self.root.clear_widgets()
        self.stop()
        # os.execvp(sys.executable, ['python'] + sys.argv)

    def cexit_dialog(self, obj):
        self.dialog_restart.dismiss(force=True)

    def reset_audio(
        self, object, *args
    ):
        with open('settingso.json', 'r') as file:
            existant_data = json.load(file)
        with open('settings.json', 'w') as js_file:
            json.dump(existant_data, js_file, indent=4, sort_keys=True)

        if not self.dialog_restart:
            self.dialog_restart = MDDialog(
                text="reset audio,need restart the app",
                auto_dismiss=False,
                buttons=[
                    MDFlatButton(
                        text="No",
                        on_release=self.cexit_dialog,
                    ),
                    MDFlatButton(
                        text="Yes",
                        on_release=self.reset_APP,
                    ),
                ],
            )

        self.dialog_restart.open()


    def on_resume(self):
        if platform == 'android':
            # self.root.ads.request_interstitial()
            # self.root.ads.show_interstitial()


    def on_pause(self):
        return True
    def about(
        self, object, *args
    ):
        from webbrowser import open as webopen
        webopen("https://www.tublm.com/")


Livecho().run()