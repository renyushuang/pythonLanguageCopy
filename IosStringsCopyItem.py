import os, logging, json, sys

logging.basicConfig(level=logging.INFO)

pathTargetPath = "/Users/renyushuang/custom/projectDo/FlutterPDF/flutter_pdf/ios/Runner"

pathTransDir = "/Users/renyushuang/Downloads/PDF_v1.0.0_多语文案"

targetFilename = "InfoPlist.strings"

copyList = ["NSPhotoLibraryUsageDescription", "NSCameraUsageDescription"]

chinaName = {'波斯语': "fa",
             '罗马尼亚': "ro",
             '罗马尼亚语': "ro",
             '波兰语': "pl",
             '英文': "en",
             '简体中文': "zh-Hans",
             '简中': "zh-Hans",
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
             '泰语': "th-TH",
             '阿拉伯语': "ar",
             '土耳其语': "tr",
             '台湾繁体': "zh-HK",
             '香港繁体': "zh_Hant_HK", }

listdir = os.listdir(pathTransDir)

for i in listdir:
    if os.path.splitext(i)[1] != ".strings":
        continue

    # 翻译的目录
    sourceFilePath = os.path.join(pathTransDir, i)

    # 获取翻译文件路径
    fileName = os.path.splitext(i)[0]
    fileNameSplit = fileName.split(" ")

    fileNameSplitLen = len(fileNameSplit)
    if fileNameSplitLen < 2:
        print("这个语言的文件命名和其他的不同 = " + str(fileName))
        continue

    split_ = chinaName.get(fileNameSplit[1])
    if split_ == None:
        print("当前这个语言的命名在字典中没有找到 = " + str(fileNameSplit[1]))
        continue

    targetFilePath = os.path.join(pathTargetPath, split_ + ".lproj", targetFilename)

    if os.path.exists(targetFilePath):
        sourceFile = open(sourceFilePath)
        sourceReadlines = sourceFile.readlines()
        for sourceLine in sourceReadlines:

            for copyItem in copyList:
                if sourceLine.find(copyItem) >= 0:
                    targetFile = open(targetFilePath, "a")
                    targetFile.write(sourceLine.replace("「", "\"").replace("」", "\""))
                    targetFile.close()
