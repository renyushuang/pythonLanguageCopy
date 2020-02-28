# 文案转换

## 目录

- IOS文案转换成Flutter文案（ .arb文件)
- Flutter文案（ .arb文件)转换成Flutter多语言文案代码



## 一、IOS文案转换成Flutter文案（ .arb文件)

### 1.python文件

LanguageIosStringCopyToFlutter.py

### 2.使用

python3 LanguageIosStringCopyToFlutter.py IOS返回文案的文件夹全路径

#### 示例

python3 LanguageIosStringCopyToFlutter.py /Users/renyushuang/Downloads/PDF_v1.0.0_多语文案

```
注意：
全路径不能有空格
```

### 3.部分疑问

- 生成目录 **LanguageIosStringCopyToFlutter.py**文件下的**flutter文件夹**
- 如果已有部分文案想要进行新文案的添加，
  - 1.将已有文件拷贝到flutter文件夹下
  - 2.执行使用步骤便可进行**叠加**或**覆盖**



## 二、Flutter文案（ .arb文件)转换成Flutter多语言文案代码

### 1.Python文件

LanguageIosStringDart.py

### 2.使用

python3 LanguageIosStringDart.py 需要转换成dart的.arb文件

#### 示例

```
python3 LanguageIosStringDart.py ./flutter/intl_zh.arb
```

#### 结果示例

```
String setting_head_product_title( String arg0,) => Intl.message('{arg0}高级版',name:'setting_head_product_title',desc:'',locale:_localeName,args: [arg0,],);
String vertify_failed( String arg0,) => Intl.message('校验失败（{arg0}），稍后重试',name:'vertify_failed',desc:'',locale:_localeName,args: [arg0,],);

```

沾入代码就可以了









