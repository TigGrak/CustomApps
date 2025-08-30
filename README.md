# CustomApps
**一些基于CustomApp的[Awtrix](https://awtrix.blueforcer.de/)自定义应用程序**

[![](https://img.shields.io/badge/Author-TigGrak-orange.svg)](https://github.com/TigGrak)
[![GitHub Star]( )](https://github.com/TigGrak/CustomApps)
[![GitHub License](https://img.shields.io/github/license/TigGrak/CustomApps.svg?label=License&color=4285dd&logo=github)](https://github.com/TigGrak/CustomApps/blob/main/LICENSE)

<br />
<br />
<br />


> 注意，这里的所有程序都是基于CustomApp制作的，你需要先在awtrix的操纵面板控制台中的应用商店下载CustomApp并记录好对应的url和id。

<img src="https://awtrix.blueforcer.de/icons/1060" width="20%" height="20%" />

> CustomApp的默认url为 `https://127.0.0.1:7000/api/v3/customapp`


<br />
<br />
<br />


## 已开发应用
> _所有的应用都可以使用[awtrix-push](https://github.com/JunyuMu/awtrix-push/)进行托管和自动推送。_


| 程序名称 | 介绍 | 版本 | 链接 |
| :-----:| :----: | :----: | :----: |
| jiejiari | 通过API获取当日节假日、纪念日、农历并推送 | [![](https://img.shields.io/badge/v1.0-brightgreen.svg)](https://github.com/TigGrak/CustomApps/tree/main/jiejiari) | [链接](https://github.com/TigGrak/CustomApps/tree/main/jiejiari)

<br />
<br />
<br />

## 使用基本教程


> _教程使用[jiejiari](https://github.com/TigGrak/CustomApps/tree/main/jiejiari)为例。_

### 一、使用自己的python程序推送
<br />


1.在jiejiari.py所在文件夹下新建文件 `**.py` 这里**为任意文件名

> 当然可以不在同一个文件夹，只要你能 `import jiejiari` 就行。

<br/>

2.在 `**.py` 写入代码
```python
import jiejiari

# 这里的config为程序的配置文件，每个程序都不一样，具体请看程序连接。
config = {'key':'XXXXXXXXXX','mode':'1','color':'67,142,219','cuscolor':'67,142,219',"push_url":"http://127.0.0.1:7000/api/v3/customapp","id":"2","updata":"3","color_priority":"1","icon_priority":"0"}

jiejiari.jiejiari(config)
```
<br/>

3.运行 `**.py` 

至此，你已经完成了单次推送，你可以选择修改 `**.py` 完成更多操作。

<br />
<br />
<br />

### 二、使用[awtrix-push](https://github.com/JunyuMu/awtrix-push/)进行自动推送。
> 使用本方法，你需要对awtrix-push有熟悉的掌握。

<br />

1.插入代码

awtrix-push默认主要文件树：
```
awtrix-push
│  tasks.py
│  template.cfg
│
└─parse
        custom.py
        default.py
        __init__.py
```

将 `jiejiari.py` 内的所有代码复制进 `\parse\你的任务托管py文件.py`

例如使用 `default.py`
```python
# task 1
def anotherTask(config):
    pass
    # Others...


# 插入的代码
# task 2
def jiejiari(config):
    _version = '1.0.0'
    uptext = ''
    Upath = os.getcwd()
    # Others...
```

<br />

2.配置config文件

在config内插入程序的配置信息
```ini
[DEFAULT]
# Celery Broker
broker_url=redis://127.0.0.1:6379/0
# Your timezone
timezone=Asia/Shanghai

# Your CustomApp Name
[ANOTHERTASK]
# run every seconds
seconds=20
# Custom parameter
push_url=http://127.0.0.1:7000/api/v3/customapp
id=3
icon=1177
# Custom function
custom=True

# 插入的配置信息，每个程序都不一样，具体请看程序连接。
[JIEJIARI]
push_url=http://127.0.0.1:7000/api/v3/customapp
seconds=600
id=2
mode=1
updata=3
key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
color=67,142,219
cuscolor=67,142,219
color_priority=1
icon_priority=0


#[Something]
#...
```
<br />


3.重启awtrix-push服务。

至此，你已经完成了awtrix-push的自定义程序任务配置，awtrix-push将会根据你的配置进行自动推送。

<br />
<br />
<br />

### 三、其他推送方法
当然，你可以修改 `jiejiari.py` 并编译使其被系统托管，例如
```python
import models

def jiejiari(config):
    _version = '1.0.0'
    uptext = ''
    Upath = os.getcwd()
    # Others...

if  __name__ == '__main__':
    config = {'key':'XXXXXXXXXX','mode':'1','color':'67,142,219','cuscolor':'67,142,219',"push_url":"http://127.0.0.1:7000/api/v3/customapp","id":"2","updata":"3","color_priority":"1","icon_priority":"0"}
    
    jiejiari(config)


```

<br />
<br />
<br />

## License
```
MIT License

Copyright (c) 2022 TigGrak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
