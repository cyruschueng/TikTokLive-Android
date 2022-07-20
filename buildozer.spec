[app]

 
title = Tiktok Live Echo
 
# (str) Package name
package.name = Livecho

# (str) Package domain (needed for android/ios packaging)
package.domain =  com.tublm

source.dir = .

source.include_exts = py,png,jpg,kv,atlas,so,pyx,pyi,c,pxi,h,pxd,typed,wav,mp3,json,txt
#source.include_patterns = assets/*,images/*.png

#version = 1.01
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py


source.exclude_dirs = bin, __pycache__, trash, PassLOCK_old, data, screenshots, screenshot_original

android.permissions = INTERNET, ACCESS_NETWORK_STATE, WAKE_LOCK
 
# (str) Supported orientation (one of landscape, portrait or all) before 28
orientation = all
fullscreen = 0


android.api =  30



#before requirements = python3,kivy==2.1.0,pillow,pycryptodome  requirements = python3,kivy==2.0.0,https://github.com/kivymd/KivyMD/archive/master.zip,charset-normalizer,idna,pytube,hurry.filesize, pygments,sdl2_ttf==2.0.15,Pillow, requests,urllib3,jnius,certifi,ffpyplayer,pycryptodome

#requirements = python3,kivy==2.1.0,https://github.com/kivymd/KivyMD/archive/master.zip,charset-normalizer,idna,hurry.filesize, pygments,sdl2_ttf==2.0.15,pillow, requests,urllib3,jnius,certifi,ffpyplayer,plyer,kivmob,aiohttp
#TikTokLive-0.8.9 aiohttp-3.8.1 aiosignal-1.2.0 async-timeout-4.0.2 asynctest-0.13.0 charset-normalizer-2.1.0 dacite-1.6.0 dataclasses-0.8 frozenlist-1.2.0 protobuf-3.19.4 protobuf3-to-dict-0.1.5 pyee-9.0.4


requirements = python3,aiohttp,kivy,kivymd,Pillow,TikTokLive,protobuf3-to-dict ,protobuf ,pyee ,dacite ,asynctest,multidict,attrs,async-timeout,aiosignal,typing-extensions,yarl,frozenlist,charset-normalizer,idna-ssl,six,idna,jnius,certifi,kivmob

#ffpyplayer,plyer,kivmob, requests,urllib3
#,charset-normalizer, idna, six,hurry.filesize, pygments,sdl2_ttf==2.0.15, requests,urllib3,jnius,certifi,ffpyplayer,TikTokLive

#android.arch = armeabi-v7a

 

#requirements = python3,kivy==2.0.0,charset-normalizer,idna,hurry.filesize, pygments,sdl2_ttf==2.0.15,Pillow, requests,urllib3,jnius,certifi,ffpyplayer

 
icon.filename = logo.png
#icon.filename = icon.ico
android.presplash_color = #fecd06
presplash.filename = p.jpg


#android.logcat_filters = *:S python:D
android.accept_sdk_license = True

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = True


android.release_artifact = aab
#p4a.branch = develop

# (list) Gradle dependencies to add (currently works only with sdl2_gradle
# bootstrap)
 
android.gradle_dependencies = 'com.google.firebase:firebase-ads:10.2.0'
#test
android.meta_data = com.google.android.gms.APPLICATION_ID = ca-app-pub-3940256099942544~3347511713

 


[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2


# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0


   
