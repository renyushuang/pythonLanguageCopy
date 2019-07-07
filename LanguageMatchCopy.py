#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re

pathTransDir = '/Users/renyushuang/custom/projectDo/DuScreenRecorder/RecordMaster/src/main/res'
pathTransFile = 'strings.xml'

pathAndroidDir = '/Users/renyushuang/custom/projectDo/VideoDownloader/app/src/main/res'
pathAndroidFile = 'strings.xml'

targetList = ['durec_recorder_noti_start','durec_setting_show_touches']

transDirList = os.listdir(pathTransDir)


def getPathAndroidResDir():
    realPath = []
    for dir in transDirList:
        transFilePath = os.path.join(pathTransDir, dir, pathTransFile)
        if os.path.exists(transFilePath):
            join = os.path.join(pathAndroidDir, dir)
            realPath.append(join)
    return realPath


for dir in transDirList:
    transFilePath = os.path.join(pathTransDir, dir, pathTransFile)
    if not os.path.exists(transFilePath):
        continue

    print(dir)

    transFile = open(transFilePath)

    targetFilePath = os.path.join(pathAndroidDir, dir, pathTransFile)

    dirNotExit = not os.path.exists(os.path.join(pathAndroidDir, dir))
    if dirNotExit:
        os.mkdir(os.path.join(pathAndroidDir, dir))

    targetFileRad = open(targetFilePath, 'r+')
    lines = None
    if dirNotExit:
        targetFileRad.writelines(
            '''<?xml version="1.0" encoding="utf-8"?>\n<resources xmlns:tools="http://schemas.android.com/tools" xmlns:xliff="urn:oasis:names:tc:xliff:document:1.2">\n''')
    else:
        lines = targetFileRad.readlines()

    for line in transFile:

        for needCopyStr in targetList:
            if '\"' + needCopyStr + '\"' in line:
                print(line)
                if dirNotExit:
                    targetFileRad.writelines(line)
                else:

                    lines = list(lines)
                    if len(lines) > 0:
                        if not lines[0].strip().startswith('<?xml'):
                            continue
                        lines[len(lines) - 1] = ''
                    else:
                        continue

                    lines.append(line+'\n')

                    lines.append('</resources>')

                    targetFile_add = open(targetFilePath, 'w+')
                    targetFile_add.writelines(lines)

    if dirNotExit:
        targetFileRad.writelines('''</resources>''')

# print('存在的翻译路径-->' + str(realPath))
#
