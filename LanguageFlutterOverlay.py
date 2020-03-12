# -*- coding: UTF-8 -*-
'''
@Time    : 2020/3/12 11:43
@Author  : 任玉双
@FileName: LanguageFlutterOverlay.py
@Software: PyCharm
 
'''

import os, logging, json, sys
from json import JSONDecodeError

transDir = "./多语文件夹"
file_name = "多语"
flutter_dir = "/Users/renyushuang/custom/projectDo/FlutterPDF/flutter_pdf/lib/res/global/l10n"


def copyDataTiFlutter(jsonData, flutterFilePath):
    flutterFile = open(flutterFilePath,"r")
    try:
        flutterJson = json.loads(flutterFile.read())
        flutterJson.update(jsonData)
        flutterFile.close()
        flutterFileW = open(flutterFilePath, "w")
        flutterFileW.write(json.dumps(flutterJson, indent=4, ensure_ascii=False))
        flutterFileW.close()
    except:
        print("这个flutter文件有问题"+flutterFilePath)

for languageDir in os.listdir(transDir):
    languageCode = languageDir.split("-")[0]
    flutterFile = os.path.join(flutter_dir, "intl_" + languageCode + '.arb')
    if os.path.exists(flutterFile):
        for home, dirs, files in os.walk(os.path.join(transDir, languageDir)):
            for file in files:
                if file.find(file_name) != -1:
                    try:
                        t = open(os.path.join(home, file))
                        jsonData = json.loads(t.read().replace("”", "\""))
                        t.close()
                        copyDataTiFlutter(jsonData, flutterFile)
                    except JSONDecodeError:
                        try:
                            t = open(os.path.join(home, file))
                            jsonData = json.loads("{" + t.read().replace("”", "\"") + "}")
                            t.close()
                            copyDataTiFlutter(jsonData, flutterFile)
                        except JSONDecodeError:
                            print("这个文件下的json有问题" + os.path.join(home, file))
                    except:
                        print("这个文件有问题" + os.path.join(home, file))

            print("------------")
        pass
    else:
        print("不存在该文件路径" + flutterFile)
