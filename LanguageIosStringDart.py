#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, logging, json

logging.basicConfig(level=logging.INFO)

pathTransDir = "/Users/renyushuang/Downloads/PDF_1.0.2"

chinaName = {'波斯语': "fa",
             '罗马尼亚': "ro",
             '罗马尼亚语': "ro",
             '波兰语': "pl",
             '英文': "en",
             '简体中文': "zh",
             '简中': "zh",
             '西班牙语': "es",
             '法语': "fr",
             '马来语': "ms",
             '马来文': "ms",
             '希腊语': "el",
             '韩语': "ko",
             '孟加拉': "bn",
             '俄语': "ru",
             '俄文': "ru",
             '日语': "ja",
             '印地语': "hi",
             '印尼语': "id",
             '印尼文': "id",
             '菲律宾': "tl",
             '意大利语': "it",
             '乌克兰语': "uk",
             '捷克语': "cs",
             '巴西葡语': "pt",
             '越南语': "vi",
             '德语': "de",
             '荷兰语': "nl",
             '泰语': "th",
             '阿拉伯语': "ar",
             '土耳其语': "tr",
             '台湾繁体': "zh_Hant_TW",
             '香港繁体': "zh_Hant_HK", }
targetDict = {}

listdir = os.listdir(pathTransDir)
# print(str(pathTransDir))
list = []
for value in chinaName.values():
    list.append(value)

logging.info(list)
# for i in listdir:
#     if os.path.splitext(i)[1] != ".strings":
#         continue
targetFilePath = os.path.join("./flutter", "intl_" + "zh" + ".arb")
if os.path.exists(targetFilePath):
    with open(targetFilePath, "r") as f:
        targetDict = json.load(f)
else:
    logging.info("没有文件")

resultString = ""
for (key, value) in targetDict.items():

    find1 = str(key).find("@")
    if find1 >= 0:
        continue

    find2 = str(value).find("%@")

    argValue = 0
    while find2 >= 0:
        value = str(value).replace("%@", "$arg" + str(argValue), 1)
        argValue = argValue + 1
        find2 = str(value).find("%@")

    args = ""
    args1 = ""
    if argValue > 0:
        args = "args: ["
        for arg in range(0, argValue):
            args1 = args1 + " String" + " arg" + str(arg) + ","
            args = args + "arg" + str(arg) + ","

    if argValue > 0:
        args = args + "],"



    resultString = "String " + key + "(" + args1 + ") => Intl.message(" \
                   + "\'" + value + "\'," + \
                   "name:" + "\'" + key.strip() + "\'," \
                   + "desc:" + "\'" + "\'," \
                   + "locale:" + "_localeName," + args + ");"

    print(resultString)

