#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, logging, json, sys

logging.basicConfig(level=logging.INFO)

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
             '菲律宾': "fil",
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


def main(pathTransDir):
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

        if not os.path.exists("./flutter"):
            os.makedirs("./flutter")

        fileNameSplitLen = len(fileNameSplit)
        if fileNameSplitLen < 2:
            print("这个语言的文件命名和其他的不同 = " + str(fileName))
            continue

        split_ = chinaName.get(fileNameSplit[1])
        if split_ == None:
            print("当前这个语言的命名在字典中没有找到 = " + str(fileNameSplit[1]))
            continue

        targetFilePath = os.path.join("./flutter", "intl_" + split_ + ".arb")

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
            split_0 = sourceSplit[0].replace('\"', "").replace("「", "").replace("」", "")
            split_1 = sourceSplit[1].split(";")[0].replace('\"', "").replace("「", "").replace("」", "")

            find2 = str(split_1).find("%@")

            argValue = 0
            while find2 >= 0:
                split_1 = str(split_1).replace("%@", "{arg" + str(argValue) + "}", 1)
                argValue = argValue + 1
                find2 = str(split_1).find("%@")

            # 将解析的数据转换为目标文件格式
            targetDict[split_0.strip()] = split_1.strip()
            content = {}
            targetDict.get("@" + split_0.strip())

            targetDict["@" + split_0.strip()] = content
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


if __name__ == '__main__':
    pathTransDir = "/Users/renyushuang/Downloads/PDF_1.0.2"

    argLen = len(sys.argv)
    if argLen < 2:
        print("请输入文件参数")
    else:
        excelPath = sys.argv[1]
        if not os.path.exists(excelPath):
            logging.error("需要解析的Excel文件 不存在")
            exit()

        main(excelPath)
