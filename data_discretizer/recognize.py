import re
import json
from .regexkit import RegexKit
from . import convert
from . import standardize
from . import discretize

def recognize_date(text):
    num = r'[\d零〇一二三四五六七八九十同]'
    regex_pattern = r'(({0}+年)?{0}+月[份]?({0}+日)?({0}+时)?({0}+分)?许?)'.format(num)
    res_iter = re.finditer(regex_pattern, text)
    res = []
    for r in res_iter:
        res.append({'match':r.group(0),
                    'start':r.start(),
                    'end':r.end(),
                    'category':'[date]'})
    return res

def recognize_money(text, category_money_dict='default'):
    regex_pattern = r'({}{})'.format(RegexKit.all_zh_num, RegexKit.currency_unit)
    res_iter = re.finditer(regex_pattern, text)
    res = []
    for r in res_iter:
        # print(r.groupdict())
        value = convert.all_zh_num2float(r.group('all_zh_num'))
        unit = r.group('currency_unit')
        std_value = standardize.standardize_money(value, unit)['std_value']
        std_unit = '元'
        category = discretize.discretize_money(std_value, category_money_dict)
        res.append({'match':r.group(0),
                    'start':r.start(),
                    'end':r.end(),
                    'value':value,
                    'unit':unit,
                    'std_value':std_value,
                    'std_unit':std_unit,
                    'category':category})
    return res

def recognize_weight(text, category_weight_dict='default'):
    regex_pattern = r'({}{})'.format(RegexKit.all_zh_num, RegexKit.weight_unit)
    res_iter = re.finditer(regex_pattern, text)
    res = []
    for r in res_iter:
        value = convert.all_zh_num2float(r.group('all_zh_num'))
        unit = r.group('weight_unit')
        std_value = standardize.standardize_weight(value, unit)['std_value']
        std_unit = '克'
        category = discretize.discretize_weight(std_value, category_weight_dict)
        res.append({'match':r.group(0),
                    'start':r.start(),
                    'end':r.end(),
                    'value':value,
                    'unit':unit,
                    'std_value':std_value,
                    'std_unit':std_unit,
                    'category':category})
    return res

def recognize_BAC(text, category_BAC_dict='default'):
    regex_pattern = r'({}{})'.format(RegexKit.num, RegexKit.BAC_unit)
    res_iter = re.finditer(regex_pattern, text)
    res = []
    for r in res_iter:
        value = convert.num2float(r.group('num'))
        unit = r.group('BAC_unit')
        std_value = standardize.standardize_BAC(value, unit)['std_value']
        std_unit = 'mg/100ml'
        category = discretize.discretize_BAC(std_value, category_BAC_dict)
        res.append({'match':r.group(0),
                    'start':r.start(),
                    'end':r.end(),
                    'value':value,
                    'unit':unit,
                    'std_value':std_value,
                    'std_unit':std_unit,
                    'category':category})
    return res
