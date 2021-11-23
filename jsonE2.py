
import json

with open(input(), encoding='utf8') as f:
    templates = json.load(f)

value = 0
def examInt(item):
    return isinstance(templates[item], int)

def examStr(item):
    return isinstance(templates[item], str)

def examBool(item):
    return isinstance(templates[item], bool)

def examUrl(item):
    if (templates[item]).startswith('http://') or (templates[item]).startswith('https://'):
        return True 
    else:
        return False

def CheckStrValue(item, val):
    if templates[item] == 'itemBuyEventm' or templates.get(item) == 'itemViewEvent':
        return True
    else:
        return False

def ErrorLog(string):
    Error.append(string)

listOfItems = {
               'timestamp':'int', 'item_price':'int', 'referer':'url','location':'url',
               'item_url':'url', 'remoteHost':'str', 'partyId':'str',
               'sessionId':'str', 'pageViewId':'str', 'item_id':'str',
               'basket_price':'str', 'userAgentName':'str', 'eventType':'val',
               'detectedDuplicate':'bool', 'detectedCorruption':'bool', 'firstInSession':'bool'
               }

Error = []
if len(templates) == len(listOfItems):
    for item in templates:
        if item in listOfItems:
            if listOfItems[item] == 'int':
                if not examInt(item):
                    ErrorLog(f'Error: {item}: {templates[item]}, нужен тип: {listOfItems[item]}')
            elif listOfItems[item] == 'str':
                if not examStr(item):
                    ErrorLog(f'{item}:{templates[item]}, нужен тип: {listOfItems[item]}')
            elif listOfItems[item] == 'bool':
                if not examBool(item):
                    ErrorLog(f'Error: {item}: {templates[item]}, нужен тип: {listOfItems[item]}')
            elif listOfItems[item] == 'url':
                if not examUrl(item):
                    ErrorLog(f'Error: {item}: {templates[item]}, нужен тип: {listOfItems[item]}')
            elif listOfItems[item] == 'val':
                if not CheckStrValue(item,['itemBuyEventm', 'itemViewEvent']):
                    ErrorLog(f'Error: {item}: {templates[item]}, нужен тип itemBuyEventm или itemViewEvent')
        else:
            ErrorLog(f'Error: {item}: неожиданное значение')
else:
    print('неверный формат ввода данных')
       

if Error == []:
    if len(templates) == len(listOfItems):
        print('Pass')
else:
    print('Fail')
    print(*Error, sep='\n')
