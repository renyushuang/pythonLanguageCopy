#!/usr/bin/python
# -*- coding: UTF-8 -*-


from xml.dom import minidom
import os

pathTransDir = '/Users/renyushuang/custom/projectDo/DuScreenRecorder/RecordMaster/src/main/res'
pathTransFile = 'strings.xml'

pathAndroidDir = '/Users/renyushuang/custom/projectDo/VideoDownloader/app/src/main/res'
pathAndroidFile = 'strings.xml'

targetList = ['durec_recorder_noti_start',
              'durec_setting_show_touches']


def writeXmlNewString(pathAndroiid, list):
    doc = minidom.Document()

    root = minidom.parse(pathAndroiid)

    docRoot = doc.createElement('resources')
    docRoot.setAttribute('xmlns:tools', 'http://schemas.android.com/tools')
    docRoot.setAttribute('xmlns:xliff', 'urn:oasis:names:tc:xliff:document:1.2')
    doc.appendChild(docRoot)
    # 将原有的内容copy一遍
    elements = root.getElementsByTagName('string')
    for ele in elements:
        element = doc.createElement('string')
        element.setAttribute("name", ele.attributes['name'].value)
        element.appendChild(doc.createTextNode(ele.firstChild.data))
        doc.documentElement.appendChild(element)
    # 将新增加的内容copy进来
    for k, v in list.items():
        element = doc.createElement('string')
        element.setAttribute("name", k)
        element.appendChild(doc.createTextNode(v))
        doc.documentElement.appendChild(element)
    # 新建的xml进行copy
    fp = open(pathAndroiid, 'w')
    doc.writexml(fp, indent='', addindent='\t', newl='\n')


def getTransMap(path):
    map = {}
    root = minidom.parse(path)
    elements = root.getElementsByTagName('string')
    for ele in elements:
        for target in targetList:
            if ele.attributes['name'].value == target:
                map[ele.attributes['name'].value] = ele.firstChild.data
    return map

def main():
    transDirList = os.listdir(pathTransDir)

    for dir in transDirList:
        # 如果不存在的路径那么就跳过
        transFilePath = os.path.join(pathTransDir, dir, pathTransFile)
        if not os.path.exists(transFilePath):
            continue
        transMap = getTransMap(transFilePath)
        androidResDir = os.path.exists(os.path.join(pathAndroidDir, dir))

        if not androidResDir:
            continue
            # os.mkdir(os.path.join(pathAndroidDir, dir))

        if len(transMap) != 0:
            androiidResFile = os.path.join(pathAndroidDir, dir, pathAndroidFile)
            print(androiidResFile)
            if not os.path.exists(androiidResFile):
                continue
            writeXmlNewString(androiidResFile, transMap)
        else:
            print('没有匹配的字段')


main()
