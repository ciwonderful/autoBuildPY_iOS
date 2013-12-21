""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                     Rytong.BuildApp               """
"""                                                   """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import os
import codecs
import smtplib

username1 = "xixx"
password1 = "xxx"

os.chdir('/Users/xiepingjia/work/empBao/APP')
#os.chdir('/Users/xiepingjia/private/Animations/')
print(os.getcwd())
#os.chdir('../aa')
#os.chdir('./Config.h')
#print(os.getcwd())
print"build debug start"

def updateFromHG():
    input_usr_pwd(username1,password1)
    os.system('hg revert --all')
    os.system('hg pull -u default')

def input_usr_pwd(username,password):
    os.chdir('/Users/xiepingjia/work/empBao/.hg')
    array = []
    with codecs.open('hgrc', 'r', 'utf-8') as the_file:
        for each_line in the_file:
            if not each_line.find('default') == -1:
                aline = each_line
                if aline.find('@') == -1:
                    (head, tail) = aline.split('//',1);
                    head = "%s//%s:%s@"%(head,username,password)
                    each_line = "%s%s"%(head,tail)
                    #print(each_line)
                    array.append(each_line)
                else:
                    (head, temp) = aline.split('//',1);
                    (temp, tail) = aline.split('@',1);
                    head = "%s//%s:%s@"%(head,username,password)
                    each_line = "%s%s"%(head,tail)
                    array.append(each_line)
            else:
                array.append(each_line)
    print(array)
    codecs.open('hgrc', 'w','utf-8').writelines(array)


def change_info_plist():
    array = []
    isFind = 0
    with codecs.open('APP-Info.plist', 'r', 'utf-8') as the_file:
        for each_line in the_file:
            if each_line.find('CFBundleIdentifier') >= 1:
                isFind = 1
                array.append(each_line)
            else:
                if isFind == 1:
                    temp = "\t<string>emas.dis.231111</string>\n"
                    array.append(temp)
                    isFind = 0
                else:
                    array.append(each_line) 

    codecs.open('APP-Info.plist', 'w','utf-8').writelines(array)

def build_each_project(project):
    for each_project in project:
        print('%s'%each_project)
        os.system('rm -rf /Users/xiepingjia/work/empBao/%s/build'%each_project)
        os.chdir('/Users/xiepingjia/work/empBao/%s'%each_project)
        os.system('xcodebuild -project %s.xcodeproj -sdk iphoneos -target %s -configuration Release clean build'%(each_project,each_project))

    

def appToIpaFile():
    os.chdir('/Users/xiepingjia/work/empBao')
    os.system('rm -rf APP/Payload')
    os.system('mkdir APP/Payload')
    os.system('cp -r APP/build/Release-iphoneos/APP.app APP/Payload/')
    os.system('zip -r /Users/xiepingjia/Desktop/node/APPaa.ipa APP/Payload')
    os.system('open /Users/xiepingjia/Desktop/node/')




change_info_plist()


os.system('rm -rf /Users/xiepingjia/work/empBao/APP/build')
os.chdir('/Users/xiepingjia/work/empBao/APP')
os.system("xcodebuild -project APP.xcodeproj -sdk iphoneos -target APP -configuration Release CODE_SIGN_IDENTITY=\"iPhone Distribution: Beijing RYTong Information Technology Co. Ltd.\" clean build")
os.system('-exportProvisioningProfile')
appToIpaFile()
#os.system('sh build_fake_framework.sh')
#os.system('88632930')
array = []
newArray = []

"""with codecs.open('Config.h', 'r', 'utf-8') as the_file:
    for each_line in the_file:
        if each_line.find('TEMPLATEMODE') >= 1:
            temp = "\t//#define TEMPLATEMODE\n"
            array.append(temp)
        else:
            array.append(each_line) 
    

codecs.open('Config1.h', 'w','utf-8').writelines(array)"""

co
#pVrint(array)


#os.system('cd /Users/xiepingjia/private/Animations/')

#os.system('mkdir /Users/xiepingjia/private/Animations/ds1a')
#os.system('rm -rf /Users/xiepingjia/work/empBao/Control/build')
#os.system('xcodebuild')



