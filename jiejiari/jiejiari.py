#UTF-8
"""
基于Awtrix CustomApp的自动获取农历、节日、纪念日的推送程序。
可以使用awtrix-push进行自动推送。Github:https://github.com/JunyuMu/awtrix-push
节日获取API:https://www.tianapi.com/apiview/139   免费（每天可获取100次）

项目地址、具体使用方法、开源许可：https://github.com/TigGrak/CustomApps
BILIBILI:https://space.bilibili.com/432639062
主页：https://tiggrak.gitee.io



写得比较急，代码凌乱，有时间的话后期优化一下。（或许还会更新:-P)
"""

"""
#ENGLISH
Push program based on awtrix customapp to automatically obtain lunar calendar, festivals and anniversaries.
You can use awtrix push to push automatically. Github: https://github.com/JunyuMu/awtrix-push
Festival get api: https://www.tianapi.com/apiview/139 Free (100 times a day)
Project address, specific use method, open source license: https://github.com/TigGrak/CustomApps
BILIBILI: https://space.bilibili.com/432639062
Home page: https://tiggrak.gitee.io
It's written in a hurry and the code is messy. If you have time, optimize it later. (maybe update: -p)
"""



import requests
import os,json   #额外模块
from dateutil.relativedelta import relativedelta  #额外模块
from datetime import datetime  #额外模块



def jiejiari(config):
    _version = '1.0.0' #版本号
    uptext = '' #更新信息
    Upath = os.getcwd() #运行时的路径


    #要加上，要不获取更新被拒
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }

    #提前存好一个月的节假日，防止访问次数用完。
    thisMonth = datetime.now().strftime("%Y-%m")
    if not(os.path.exists('./jiejiari')):  #初次使用要创建文件夹
        os.makedirs('./jiejiari')
    if not(os.path.exists(f'./jiejiari/{thisMonth}.json')):
        r = requests.get(url=f"https://api.tianapi.com/jiejiari/index?key={config['key']}&date={thisMonth}&type=2&mode={config['mode']}")
        with open(f'./jiejiari/{thisMonth}.json','w',encoding='UTF-8') as f:
            f.write(json.dumps(r.text))

    #更新（程序）
    update_mode = config['updata']
    try:
        uplink = 'https://tiggrak.gitee.io/project/jiejiari/info'
        if update_mode != '0':
            r = requests.get(url=uplink,headers=headers)
            jiejiariInfo = r.json()
            newinfoVersion = jiejiariInfo["jinfoVersion"]
            newpyVersion = jiejiariInfo["pyVersion"]
            jinfoLink = jiejiariInfo["jinfo"]
            pyupdataLink = jiejiariInfo["pyUpdata"]
            pyGithub = jiejiariInfo["github"]
            
        if update_mode in ['1','3']:
            if newpyVersion != _version:
                #uptext = f'找到一个可用的新版本:v{newpyVersion}。已经下载至{Upath}/jiejiari/，github地址：{pyGithub}'
                uptext = f'Found a new version available: v{newpyVersion}. Downloaded to {Upath}/jiejiari/, GitHub: {pyGithub}'
                upicon='506'
                uptextColor = [0,255,0]
                r = requests.get(url=pyupdataLink,headers=headers)
                with open(f'./jiejiari/jiejiari-{newpyVersion}.py','wb') as f:
                    f.write(r.content)
    except Exception as e:
        #错误输出
        update_mode = 0 #关闭更新，设置为离线模式
        #print(e.__class__.__name__)
        uptext = f'An error found while trying to get updates:{str(e.__class__.__name__)}. You can go to GitHub to feed back the error.Detailed errors have been saved in{Upath}/jiejiari/error.txt'
        uptextColor = [255,0,0]
        upicon = "23"
        errorTime = datetime.now().strftime(r"%Y-%m-%d_%H:%M:%S")
        error_text=f'[{errorTime}] {str(e)} \n'
        with open(f'./jiejiari/error.txt','a+',encoding="UTF-8") as f:
            f.write(error_text)

    #删除前一个月的及假日信息
    lastMonth = (datetime.now().date() - relativedelta(months=1)).strftime("%Y-%m")
    if os.path.exists(f'./jiejiari/{lastMonth}.json'):
        os.remove(f'./jiejiari/{lastMonth}.json')
    

    
    #读取今天的节假日信息
    today = datetime.now().strftime("%Y-%m-%d")
    todayNY = datetime.now().strftime("%m-%d")
    #today='2022-07-01'
    with open(f'./jiejiari/{thisMonth}.json','r',encoding='UTF-8') as f:
        thisMonthJJR =  json.loads(json.loads(f.read()))
    for i in thisMonthJJR['newslist']:
        if i['date'] == today:
            todayInfo = i
            break
    

    #将农历月份汉字转换为ax支持的数字
    if todayInfo['lunarmonth'][0]=='正':
        lm1 = '1'
    elif todayInfo['lunarmonth'][0]=='二':
        lm1 = '2'
    elif todayInfo['lunarmonth'][0]=='三':
        lm1 = '3'
    elif todayInfo['lunarmonth'][0]=='四':
        lm1 = '4'
    elif todayInfo['lunarmonth'][0]=='五':
        lm1 = '5'
    elif todayInfo['lunarmonth'][0]=='六':
        lm1 = '6'
    elif todayInfo['lunarmonth'][0]=='七':
        lm1 = '7'
    elif todayInfo['lunarmonth'][0]=='八':
        lm1 = '8'
    elif todayInfo['lunarmonth'][0]=='九':
        lm1 = '9'
    elif todayInfo['lunarmonth'][0]=='十':
        lm1 = '10'
    elif todayInfo['lunarmonth'][0]=='冬':
        lm1 = '11'
    elif todayInfo['lunarmonth'][0]=='腊':
        lm1 = '12'


    #将农历日期汉字转换为ax支持的数字
    #十位数
    if todayInfo['lunarday'][0]=='初':
        ld1 = ''
    elif todayInfo['lunarday'][0]=='十':
        ld1 = '1'
    elif todayInfo['lunarday'][0]=='二':
        ld1 = '1'
    elif todayInfo['lunarday'][0]=='廿':
        ld1 = '2'
    elif todayInfo['lunarday'][0]=='三':
        ld1 = '3'
    #个位数
    if todayInfo['lunarday'][1]=='一':
        ld2 = '1'
    elif todayInfo['lunarday'][1]=='二':
        ld2 = '2'
    elif todayInfo['lunarday'][1]=='三':
        ld2 = '3'
    elif todayInfo['lunarday'][1]=='四':
        ld2 = '4'
    elif todayInfo['lunarday'][1]=='五':
        ld2 = '5'
    elif todayInfo['lunarday'][1]=='六':
        ld2 = '6'
    elif todayInfo['lunarday'][1]=='七':
        ld2 = '7'
    elif todayInfo['lunarday'][1]=='八':
        ld2 = '8'
    elif todayInfo['lunarday'][1]=='九':
        ld2 = '9'
    elif todayInfo['lunarday'][1]=='十':
        ld2 = '0'

    #加载文件
    jinfo = {}
    customdayAll = {}
    if os.path.exists('./jiejiari/jinfo.json'):
        with open('jiejiari/jinfo.json','r',encoding="UTF-8") as f:
            jinfo = json.load(f)

    if os.path.exists('./jiejiari/customday.json'):
        with open('jiejiari/customday.json','r',encoding="UTF-8") as f:
            customdayAll = json.load(f)

    #更新（jinfo）
    if update_mode in ['2','3']:
        if os.path.exists('./jiejiari/jinfo.json'):
            if jinfo['version'] != newinfoVersion:
                r = requests.get(url=jinfoLink,headers=headers)
                with open(f'./jiejiari/jinfo.json','wb') as f:
                    f.write(r.content)
                with open('jiejiari/jinfo.json','r',encoding="UTF-8") as f:
                    jinfo = json.load(f)
        else:
            r = requests.get(url=jinfoLink,headers=headers)
            with open(f'./jiejiari/jinfo.json','wb') as f:
                f.write(r.content)
            with open('jiejiari/jinfo.json','r',encoding="UTF-8") as f:
                jinfo = json.load(f)


            
    #整合农历信息
    lunarday = ld1+ld2
    lunar = lm1+'.'+lunarday

    #初始化节日推送信息
    name = ''
    enname = ''
    rgb = config['color'].split(',')
    color=[int(rgb[0]),int(rgb[1]),int(rgb[2])]
    icon=1972


    #寻找自定义节假日
    cusday = ''
    cusicon = '1972'
    cusrgb = config['cuscolor'].split(',')
    cuscolor = [int(cusrgb[0]),int(cusrgb[1]),int(cusrgb[2])]
    
    if customdayAll:
        if todayNY in customdayAll['jiejiari']:
            cusday = customdayAll['jiejiari'][todayNY][0]
            cusicon = customdayAll['jiejiari'][todayNY][1]
            cuscolor = customdayAll['jiejiari'][todayNY][2]
    

    if todayInfo['name']:
        name = todayInfo['name']
        #寻找英文名    
        if todayInfo['enname']:
            enname = todayInfo['enname']
        else:
            if os.path.exists('./jiejiari/jinfo.json'):
                if todayInfo['name'] in jinfo['jiejiari']:
                    if jinfo['jiejiari'][todayInfo['name']][0]:
                        enname = jinfo['jiejiari'][todayInfo['name']][0]
        #寻找合适的图标、颜色
        if os.path.exists('./jiejiari/jinfo.json'):
            if todayInfo['name'] in jinfo['jiejiari']:
                if jinfo['jiejiari'][todayInfo['name']][1]:
                    icon = jinfo['jiejiari'][todayInfo['name']][1]
                if jinfo['jiejiari'][todayInfo['name']][2]:
                    color = jinfo['jiejiari'][todayInfo['name']][2]

    #愚人节小彩蛋
    if name == '愚人节':
        enname = "yaD s'looF lirpA"


    #整理推送信息
    #两种节日（API、自定义）
    if enname and cusday:
        finallytext = f'{lunar}==={enname}  \  {cusday}==='
        #获取优先级
        if config['color_priority'] == '1':
            finallycolor = color
        else:
            finallycolor = cuscolor
        if config['icon_priority'] == '1':
            finallyicon = int(icon)
        else:
            finallyicon = int(cusicon)

    #只有API节日
    elif enname:
        finallytext = f'{lunar}==={enname}==='
        finallyicon = int(icon)
        finallycolor = color
    #只有自定义节日
    elif cusday:
        finallytext = f'{lunar}==={cusday}==='
        finallyicon = int(cusicon)
        finallycolor = cuscolor
    #都没有，只输出输出农历（如果有更新则一起输出）
    else:
        if uptext:
            finallyicon = int(upicon)
            finallycolor = uptextColor
            finallytext = f'{lunar}     {uptext}'
        else:
            finallyicon = int(icon)
            finallycolor = color
            finallytext = f'{lunar}'

    #推送
    push_data = {
        "ID": config["id"],
        "text": finallytext,
        "icon": finallyicon,
        "repeat":2,
        "color":finallycolor
    }
    awtrix_r = requests.post(config["push_url"], json=push_data)
    if awtrix_r.status_code != requests.codes.ok:
        return "failure"
    return "success"

