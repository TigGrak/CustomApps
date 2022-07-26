# CustomApps-jiejiari
**通过API获取当日节假日、纪念日、农历并用CustomApps推送至[Awtrix](https://awtrix.blueforcer.de/)**

[![](https://img.shields.io/badge/Author-TigGrak-orange.svg)](https://github.com/TigGrak)
[![](https://img.shields.io/badge/version-v1.0-brightgreen.svg)](https://github.com/TigGrak/CustomApps/tree/main/jiejiari)

![](https://awtrix.blueforcer.de/icons/1972)

<br />
<br />

### [返回](https://github.com/TigGrak/CustomApps/) | CustomApps


<br />

## 配置
程序主要配置如下
| 字段 | 类型 | 选项 | 说明 |
| :----| :---- | :---- | :---- |
| push_url | str | url | 推送的url，例如 http://127.0.0.1:7000/api/v3/customapp |
| id | int | \ | CustomAppAPI的ID |
| mode | int | 0,1 | 查询模式，为1返回国际各类特殊纪念日信息 |
| updata | int | 0,1,2,3 | 更新类型，0为不更新，1为只更新程序，2为只更新jinfo，3为都更新 |
| key | str | \ | [天行数据节假日API](https://www.tianapi.com/apiview/139)的API Key |
| color | str(rgb) | rgb颜色值 | 默认推送文字的颜色，rgb形式，用英文逗号分隔，例如 67,142,219 |
| cuscolor | str(rgb) | rgb颜色值 | 默认自定义应用推送文字的颜色，rgb形式，用英文逗号分隔，例如 67,142,219 |
| color_priority | int | 0,1 | API的节假日与自定义节假日重叠时的颜色优先级，1为取API节假日的颜色，0为取自定义节假日的颜色 |
| icon_priority | int | 0,1 | API的节假日与自定义节假日重叠时的图标优先级，1为取API节假日的图标，0为取自定义节假日的图标 |

<br />

使用awtrix-push进行托管时的必要配置
> [JIEJIARI]下

| 字段 | 类型 | 选项 | 说明 |
| :----| :---- | :---- | :---- |
| crontab | bool | True,False | Crontab时间表，True 为启用，使用此项需设置好时间，与 seconds 冲突 |
| seconds | int | 秒速 | 每次执行此任务的间隔，秒为单位，与 crontab 冲突|

<br />

因此，在python中，你可以这么写：
```python
config = {'key':'XXXXXXXXXX','mode':'1','color':'67,142,219','cuscolor':'67,142,219',"push_url":"http://127.0.0.1:7000/api/v3/customapp","id":"2","updata":"3","color_priority":"1","icon_priority":"0"}
```

<br />

在awtrix-push的配置文件中，你可以这么写：

```ini
[JIEJIARI]
push_url=http://127.0.0.1:7000/api/v3/customapp
# 10min执行一次   或者crontab=True
seconds=600
id=2
mode=1
updata=3
key=XXXXXXXXXXXXXXXXXX
color=67,142,219
cuscolor=67,142,219
color_priority=1
icon_priority=0
```


<br />
<br />
<br />

## 文件
> 在初次执行jiejiari任务时，程序会自动在托管程序的目录下创建一个名为 `jiejiari` 的文件夹，里面存储着程序的运行所需的文件，可能有以下文件



| 文件名 | 说明 | 必要性 |
| :----| :---- |  :---- |
| YYYY-mm.json | 从API读取的节假日信息文件,由程序更新 | 必须 |
| jinfo.json | 自定义从 YYYY-mm.json 获取的节日的英文名、文字颜色和图标，可由程序创建或更新，或自己更改 | 可选 |
| customday.json | 自定义节假日的配置文件，由自己创建，更改。 | 可选 |
| error.txt | 错误日志。程序在获取、下载更新时遇到错误时创建或修改 | 可选 |
| jiejiari-version.py | 最新的程序，当程序的检查更新开启时且获取到新版本时自动下载 | 可选 |

<br />
<br />
<br />

## 自定义API节日、纪念日图标



你可以通过修改 `jinfo.json` 来自定义API节日的英文名图标和文字颜色

><font color=#00FFFF>⚠️作者衷心希望你能够将自己设计的节日图标、文字颜色或是修改过后的 `jinfo.json` 发送到 `tiggrak@163.com` 作者会将部分自定义API节日的图标和文字颜色上传至云端供大家使用。同时，你将会进入本markdown的感谢名单内。感谢你为此项目的付出！</font>

文件结构：




```json
{
	"version":"1.0.0", //版本号，必填，自动更新时需要（如开启jinfo的自动更新）
	"jiejiari": {
		"节日、纪念日中文名": ["English name", "图标ID", "rgb颜色（列表形式）"], //用逗号分隔
        "示范": ["example","1",[255,255,255]]
        }
}
```



> <font color=#FF0000>**_⚠️如直接复制请删除注释！！!_<br />_⚠️如直接复制请删除注释！！!_<br />_⚠️如直接复制请删除注释！！!_**</font>

<br />

><font color=#FFFF00>**_⚠️文件格式、语法错误可能会导致程序崩溃（请删除注释），请注意！！!_**</font>

> 程序会自动识别该节日对应的英文名，图标，颜色，不需要重新启动程序（热修改）。

> 如果没有 `jinfo.json` 或程序找不到对应的颜色和图标ID，程序将会推送默认图标（不可修改）和默认颜色（可修改）。

默认图标：

<img src="https://awtrix.blueforcer.de/icons/1972" width="10%" height="10%" />

<br />

> 天行数据API会提供部分节假日、纪念日的英文名，如果某节假日、纪念日没有英文名，程序将在 `jinfo.json` 中寻找，如没有 `jinfo.json` 文件或寻找不到，程序将不予推送。


<br />
<br />
<br />

## 自定义节日、纪念日

你可以通过创建修改 `jinfo.json` 来自定义节日和节日的英文名图标和文字颜色

> **_⚠️程序不会自动创建 `customday.json` ，你需要手动创建。_**

> **_⚠️遇到个位数日期一定要补0，例如:<br />6.7   (×)<br />06.07   (√)_**

> **_⚠️日期不要加年份，加公历的月-日（mm-dd）_**

> **_⚠️一个日期只能设置一个节日、纪念日，如果要设置多个，可以在节日、纪念日的名字用 `/` 号隔开。_**

文件结构：
```json
{
    "info":"BY TigGrak", //文件信息，可随意填写（不要破坏json语法）
    "jiejiari":{
        "mm-dd":["jieri english name","图标ID","rgb颜色（列表形式）"],
        //示范
        "06-10": ["example","1",[255,255,255]],
        "06-11": ["day1 / day2","212",[255,255,0]]

        }
}
```
> <font color=#FF0000>**_⚠️如直接复制请删除注释！！!_<br />_⚠️如直接复制请删除注释！！!_<br />_⚠️如直接复制请删除注释！！!_**</font>

<br />

><font color=#FFFF00>**_⚠️文件格式、语法错误可能会导致程序崩溃（请删除注释），请注意！！!_**</font>

> 程序会自动识别自定义节日，图标，颜色，不需要重新启动程序（热修改）。

<br />
<br />
<br />

## 事件

> **以下的节日、纪念日等统称为“特殊日”**

### 一、无API特殊日、自定义特殊日事件
Awtrix将会显示默认图标和默认颜色和当天的农历日期（ `color` 字段的默认颜色）。

<br />


### 二、有API特殊日、自定义特殊日事件其中之一
Awtrix将会显示API当天农历、API特殊日或自定义特殊日和对应的图标和颜色（如果能找到或有修改、自定义颜色图标的话）。

格式： `{农历}==={特殊日}===`

> 如果找不到对应的图标和颜色，将会显示默认图标和颜色。（`color` 字段为API特殊日默认颜色， `cuscolor` 字段为自定义特殊日默认颜色）

<br />

### 三、API特殊日、自定义特殊日事件重复

Awtrix将会显示API当天农历、API特殊日、自定义特殊日和对应的图标和颜色（如果能找到或有修改、自定义颜色图标的话）。

格式： `{农历}======{API特殊日}  \  {自定义特殊日}======`

> 当天显示的图标、颜色根据优先级判断，但是，当程序找不到优先图标，则会使用次要图标，如还是找不到次要图标，则会显示默认图标。

<br />

### 三、发现并下载更新事件
> 本事件只有在无特殊日事件且发现更新时才会发生。

Awtrix将会显示更新图标、当天农历、新程序的版本、已下载新程序的路径和github链接。

更新图标：

<img src="https://awtrix.blueforcer.de/icons/506" width="10%" height="10%" />

格式： `Found a new version available: {新程序的版本}. Downloaded to {已下载新程序的路径}, GitHub: {github链接}`

> 程序会自动下载新版本，但不会安装和迁移代码，需要你手动操作 ，新程序代码的路径一般为 `托管程序的目录\jiejiari\`

<br />

### 三、错误事件

> 本事件只有在无特殊日事件且获取更新时遇到错误才会发生。

Awtrix将会显示错误图标、错误类型和错误日志的路径。

错误图标:

<img src="https://awtrix.blueforcer.de/icons/23" width="10%" height="10%" />

格式： `An error found while trying to get updates:{错误类型}. You can go to GitHub to feed back the error. Detailed errors have been saved in {错误日志的路径}`

> 你可以根据错误类型和错误日志到[这里](https://github.com/TigGrak/CustomApps/issues)进行反馈

> 错误日志只有在发现错误时才会创建或追加，文件名一般为 `error.txt` ，路径一般为 `托管程序的目录\jiejiari\`


错误日志的格式一般为：
```
[1999-09-09_09:09:09] 错误内容1 
[2000-02-20_20:20:20] 错误内容2 
```

<br />
<br />
<br />

## 其他

[天行数据](https://www.tianapi.com/)

[天行数据节假日API](https://www.tianapi.com/apiview/139)
