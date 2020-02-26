#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, logging, json

logging.basicConfig(level=logging.INFO)

pathTransDir = "/Users/renyushuang/Downloads/PDF_1.0.2_多语"

chinaName = {'波斯语': "fa",
             '罗马尼亚': "ro",
             '波兰语': "pl",
             '英文': "en",
             '简体中文': "zh",
             '西班牙语': "es",
             '法语': "fr",
             '马来语': "ms",
             '希腊语': "el",
             '韩语': "ko",
             '孟加拉': "bn",
             '俄语': "ru",
             '日语': "ja",
             '印地语': "hi",
             '印尼语': "id",
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
for i in listdir:
    if os.path.splitext(i)[1] != ".strings":
        continue

    # 源文件的目录
    sourceFilePath = os.path.join(pathTransDir, i)

    # 获取目标文件路径
    fileName = os.path.splitext(i)[0]
    fileNameSplit = fileName.split(" ")
    targetFilePath = os.path.join("./flutter", "intl_" + chinaName[fileNameSplit[1]] + ".arb")

    targetDict = {}

    if os.path.exists(targetFilePath):
        with open(targetFilePath, "r") as f:
            targetDict = json.load(f)
    # else:

    # 进行读取源文件
    sourceFile = open(sourceFilePath)
    sourceReadlines = sourceFile.readlines()
    for sourceLine in sourceReadlines:
        # 对源文件进行解析
        sourceSplit = sourceLine.split("=")
        if len(sourceSplit) < 2:
            continue
        split_0 = sourceSplit[0].replace('\"', "")
        split_1 = sourceSplit[1].split(";")[0].replace('\"', "")

        find2 = str(split_1).find("%@")

        argValue = 0
        while find2 >= 0:
            split_1 = str(split_1).replace("%@", "{arg" + str(argValue)+"}", 1)
            argValue = argValue + 1
            find2 = str(split_1).find("%@")

        # 将解析的数据转换为目标文件格式
        targetDict[split_0] = split_1
        content = {}
        targetDict["@" + split_0] = content
        content["description"] = ""
        content["type"] = "text"
        content["placeholders"] = {}

        if argValue > 0:
            args = "args: ["
            for arg in range(0, argValue):
                content["placeholders"]["arg" + str(arg)] = {}

    # 将文件写入到目标文件
    jsonResult = json.dumps(targetDict, indent=4, ensure_ascii=False)
    targetFile = open(targetFilePath, "w")
    targetFile.write(jsonResult)
    targetFile.close()
