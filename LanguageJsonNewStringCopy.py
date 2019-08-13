#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json, pprint, os, bs4

pathFlutterDir = '/Users/renyushuang/custom/PythonProject/LanguageMatchCopy/jsonWork/res/global/l10n'
flutterFileName = 'intl_messages.arb'

pathTransDir = '/Users/renyushuang/custom/PythonProject/LanguageMatchCopy/jsonWork/res/trans'
flutterTransName = '补充文案0614.arb'

flutterFileCompareTransDir = {
    'vi-vn': 'vi',
    '繁中': 'zh_Hant_HK|zh_HK|zh_TW|zh_Hant_TW',
    '简中': 'zh|zh_CN',
    '英文': 'messages',
    'ar-eg': 'ar',
    'cs-cz': 'cs',
    'de-de': 'de',
    'es-es': 'es',
    'fr-fr': 'fr',
    'id-id': 'id',
    'it-it': 'it',
    'ja-jp': 'ja',
    'ko-kr': 'ko',
    'nl-nl': 'nl',
    'pl-pl': 'pl',
    'pt-br': 'pt',
    'ro-ro': 'ro',
    'ru-ru': 'ru',
    'th-th': 'th',
    'tr-tr': 'tr',
    'uk-ua': 'uk',
}


def copyTansToRes(pathResFile, pathTransFile):
    # 翻译文档
    transFileData = open(pathTransFile, 'r')

    try:
        transFileJsonData = json.loads(transFileData.read())
        transFileData.close()
    except:
        print('不正确的 json格式 --> ' + pathTransFile)
        return

    # 这个是原始的资源文档
    flutterFileData = open(pathResFile, 'r')
    flutterFileJsonData = json.loads(flutterFileData.read())
    flutterFileData.close()

    items = transFileJsonData.items()

    for key, value in items:
        flutterFileJsonData[key] = value

    result = json.dumps(flutterFileJsonData, indent=4, ensure_ascii=False)

    flutterFileJsonData = open(pathResFile, 'w')
    print(pathResFile)
    flutterFileJsonData.write(result)


# 遍历一下翻译了的所有文件
listdir = os.listdir(pathTransDir)
for transDir in listdir:
    # 检查一下是否存在翻译的文件
    transRealFile = os.path.join(pathTransDir, transDir, flutterTransName)
    if not os.path.exists(transRealFile):
        print('这个翻译文件不存在 --> ' + transRealFile)
        continue
    # 根据翻译的目录名称翻译
    resName = flutterFileCompareTransDir[str(transDir)]
    if resName is None:
        print('匹配不到翻译目录 --> ' + transDir)

    split = resName.split('|')

    for real in split:
        # 获取需要copy的资源文件
        pathResFile = os.path.join(pathFlutterDir, 'intl_' + real + '.arb')
        if not os.path.exists(pathResFile):
            print('这个项目资源不存在 --> ' + pathResFile)
            continue

        copyTansToRes(pathResFile, transRealFile)
