""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""                     Rytong.BuildApp               """
"""                                                   """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import codecs
"""---------------------------------------------------"""
                   
 
"""HG"""
username1 = "xie.pingjia"
password1 = "xpj123"
""""""
BundleIdentifier1 = "ssdsa"
BundleDisplayName1 = "dsad"
BundleVersion1 = "sdf"
"""---------------------------------------------------"""
os.chdir(os.pardir)
currentPath = os.getcwd()



print currentPath

#print os.getcwd()
print"build release starting..."

def updateFromHG():
    input_usr_pwd(username1,password1)
    os.system('hg revert --all')
    os.system('hg pull -u default')

def input_usr_pwd(username,password):
    #os.chdir('/Users/xiepingjia/work/empBao/.hg')
    array = []
    with codecs.open('%s/.hg/hgrc'%currentPath, 'r', 'utf-8') as the_file:
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
    #print(array)
    codecs.open('%s/.hg/hgrc'%currentPath, 'w','utf-8').writelines(array)

def changeXcodeProjConfigAboutProvisioning():
    array = []
    #os.chdir('/Users/xiepingjia/work/empBao/APP/APP.xcodeproj')
    filePath = '%s/APP/APP.xcodeproj/project.pbxproj'%currentPath
    with codecs.open(filePath,'r','utf-8') as the_file:
        for each_line in the_file:
            if each_line.find('PROVISIONING_PROFILE[sdk=iphoneos*]') >= 1:
                each_line = "				\"PROVISIONING_PROFILE[sdk=iphoneos*]\" = \"\";\n"
                array.append(each_line)
            elif each_line.find('PROVISIONING_PROFILE =') >= 1:
                each_line = "				PROVISIONING_PROFILE = \"\";\n"
                array.append(each_line)
            else:
                array.append(each_line)
    print(array)
    codecs.open(filePath,'w','utf-8').writelines(array)

def change_info_plist(BundleIdentifier,BundleDisplayName,BundleVersion):
    array = []
    isFindID = 0
    isFindName = 0
    isVersion = 0
    #CFBundleDisplayName CFBundleShortVersionString CFBundleVersion
    with codecs.open('%s/APP/APP-Info.plist'%currentPath, 'r', 'utf-8') as the_file:
        for each_line in the_file:
            if each_line.find('CFBundleIdentifier') >= 1:
                isFindID = 1
                array.append(each_line)
            elif each_line.find('CFBundleDisplayName') >= 1:
                isFindName = 1
                array.append(each_line)
            elif each_line.find('CFBundleVersion') >= 1:
                isVersion = 1
                array.append(each_line)
            else:
                if isFindID == 1:
                    temp = "	<string>%s</string>\n"%BundleIdentifier
                    array.append(temp)
                    isFindID = 0
                elif isFindName == 1:
                    temp = "	<string>%s</string>\n"%BundleDisplayName
                    array.append(temp)
                    isFindName = 0
                elif isVersion == 1:
                    temp = "	<string>%s</string>\n"%BundleVersion
                    array.append(temp)
                    isVersion = 0
                else:
                    array.append(each_line) 

    codecs.open('%s/APP/APP-Info.plist'%currentPath, 'w','utf-8').writelines(array)

def build_each_project(project):
    for each_project in project:
        print('%s'%each_project)
        os.system('rm -rf %s/%s/build'%(currentPath,each_project))
        #print '%s/%s'%(currentPath,each_project)
        os.chdir('%s/%s'%(currentPath,each_project))
        #print filePath
        #os.system('cd %s'%filePath)
        os.system('xcodebuild -project %s.xcodeproj -sdk iphoneos -target %s -configuration Release clean build'%(each_project,each_project))

    
def buildApp():
    os.system('rm -rf %s/APP/build'%currentPath)
    os.chdir('%s/APP'%currentPath)
    #os.system("xcodebuild clean");
    os.system("xcodebuild clean -project APP.xcodeproj -sdk iphoneos -target APP -configuration Release build")
    #appToIpaFile()
    os.system("xcrun -sdk iphoneos PackageApplication -v \"/Users/xiepingjia/work/emp5.1std/APP/build/Release-iphoneos/APP.app\" -o \"/Users/xiepingjia/Desktop/node/aaa.ipa\" --sign \"iPhone Distribution: Beijing RYTong Information Technology Co. Ltd.\" --embed \"/Users/xiepingjia/Downloads/emasdis/emasdis.mobileprovision\"")
    
def appToIpaFile():
    os.chdir('/Users/xiepingjia/work/emp5.1std')
    os.system('rm -rf APP/Payload')
    os.system('mkdir APP/Payload')
    os.system('cp -r APP/build/Release-iphoneos/APP.app APP/Payload/')
    os.system('zip -r /Users/xiepingjia/Desktop/node/APPaa.ipa APP/Payload')
    os.system('open /Users/xiepingjia/Desktop/node/')

def prepareSth():
    #input_usr_pwd(username1,password1)
    #updateFromHG()
    project = ("JSONParser","Utility","XMLParser","DataBase","Network","FilesUpdate","Encrypt","UIKitAdditions","LUAScript","ControlAdditions","Control","ClassScriptParser","PreView","UserBehaviourAnalyse","XMPP","TwoDimensionCode")
    build_each_project(project)

#updateFromHG();
#prepareSth()
#changeXcodeProjConfigAboutProvisioning()
#change_info_plist(BundleIdentifier1,BundleDisplayName1,BundleVersion1)
buildApp()
#change_info_plist()


#os.system('rm -rf /Users/xiepingjia/work/empBao/APP/build')
#os.chdir('/Users/xiepingjia/work/empBao/APP')
#os.system('xcodebuild -project APP.xcodeproj -sdk iphoneos -target APP clean build')
#os.system("xcodebuild -project APP.xcodeproj -sdk iphoneos -target APP -configuration Release CODE_SIGN_IDENTITY=\"iPhone Distribution: Beijing RYTong Information Technology Co. Ltd.\" clean build")
#os.system("xcrun -sdk iphoneos PackageApplication -v \"/Users/xiepingjia/work/empBao/APP/build/Release-iphoneos/APP.app\" -o \"/Users/xiepingjia/Desktop/node/aaa.ipa\" --sign \"iPhone Distribution: Beijing RYTong Information Technology Co. Ltd.\" --embed \"/Users/xiepingjia/Downloads/emasdis/emasdis.mobileprovision\"")
#appToIpaFile()
#os.system('sh build_fake_framework.sh')
#os.system('88632930')
isOpenAnalyse = 0
appname = 'ebank'

def changeConfig():
    with codecs.open('Config.h', 'r', 'utf-8') as the_file:
        for each_line in the_file:
            if each_line.find('define NATIVE_DEVELOP') >= 1:
                temp = '//    #define NATIVE_DEVELOP'
                array.append(temp)
            if isOpenAnalyse == 1:
                if each_line.find('define START_USER_BEHAVIOUR_ANALYSE') >= 1:
                    temp = "//    #define START_USER_BEHAVIOUR_ANALYSE"
                    array.append(temp)
            if each_line.find('define APP_NAME') >= 1:
                temp = "    #define APP_NAME @\"%s\""%appname
                array.append(temp)
            if each_line.find('TEMPLATEMODE') >= 1:
                temp = "\t//#define TEMPLATEMODE\n"
                array.append(temp)
            elif each_line.find('define START_USER_BEHAVIOUR_ANALYSE') >= 1:
                temp = "//    #define START_USER_BEHAVIOUR_ANALYSE"
                array.append(temp)
            else:
                array.append(each_line) 

    codecs.open('Config1.h', 'w','utf-8').writelines(array)
#pVrint(array)


#os.system('cd /Users/xiepingjia/private/Animations/')

#os.system('mkdir /Users/xiepingjia/private/Animations/ds1a')
#os.system('rm -rf /Users/xiepingjia/work/empBao/Control/build')
#os.system('xcodebuild')



