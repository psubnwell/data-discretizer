import re
from .regexkit import RegexKit

def full2half(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        #全角空格直接转换
        if inside_code == 12288:
            inside_code = 32
        #全角字符（除空格）根据关系转化
        elif (inside_code >= 65281 and inside_code <= 65374): 
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring

def half2full(ustring):
    """半角转全角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        #半角空格直接转化
        if inside_code == 32:
            inside_code = 12288
        #半角字符（除空格）根据关系转化
        elif inside_code >= 32 and inside_code <= 126:
            inside_code += 65248

        rstring += chr(inside_code)
    return rstring


def num2int(s):
    """Convert Arabic numbers with comma <str> into integers.
    """
    if type(s) is not str:
        return 0
    return int(re.sub(r'[,，\s]', '', s))

def num2float(s):
    """Convert Arabic numbers with comma <str> into float.
    """
    if type(s) is not str:
        return 0
    return float(re.sub(r'[,，\s]', '', s))

def _testdrive_num2float():
    example = ['123',
               '12.3',
               '1,200.35',
               '1, 323.65']
    for s in example:
        print(num2float(s))

def en_num2int(n):
    pass  # TODO

def zh_num2int(a):
    """Convert numbers in Chinese characters into integers.
    Original author: binux(17175297.hk@gmail.com)
    https://github.com/binux/binux-tools/blob/master/python/chinese_digit.py
    """
    numdict = {'零':0, '一':1, '二':2, '三':3, '四':4, '五':5, '六':6,
               '七':7,'八':8, '九':9, '十':10, '百':100, '千':1000, '万':10000,
               '〇':0, '两':2, '亿':100000000,
               '壹':1, '贰':2, '叁':3, '肆':4, '伍':5, '陆':6, '柒':7,
               '捌':8, '玖':9, '拾':10, '佰':100, '仟':1000, '萬':10000}
    count = 0
    result = 0
    tmp = 0
    Billion = 0
    while count < len(a):
        tmpChr = a[count]
        #print tmpChr
        tmpNum = numdict.get(tmpChr, None)
        #如果等于1亿
        if tmpNum == 100000000:
            result = result + tmp
            result = result * tmpNum
            #获得亿以上的数量，将其保存在中间变量Billion中并清空result
            Billion = Billion * 100000000 + result
            result = 0
            tmp = 0
        #如果等于1万
        elif tmpNum == 10000:
            result = result + tmp
            result = result * tmpNum
            tmp = 0
        #如果等于十或者百，千
        elif tmpNum >= 10:
            if tmp == 0:
                tmp = 1
            result = result + tmpNum * tmp
            tmp = 0
        #如果是个位数
        elif tmpNum is not None:
            tmp = tmp * 10 + tmpNum
        count += 1
    result = result + tmp
    result = result + Billion
    return result

def _testdrive_zhnum2int():
    """纯中文数字转阿拉伯数字的测试用例"""
    test_map = {
        '三千五百二十三': 3523,
        '七十五亿八百零七万九千二百零八': 7508079208,
        '四万三千五百二十一': 43521,
        '三千五百二十一': 3521,
        '三千五百零八': 3508,
        '三五六零': 3560,
        '一万零三十': 10030,
        '': 0,
        #1 digit 个
        '零': 0,
        '一': 1,
        '二': 2,
        '三': 3,
        '四': 4,
        '五': 5,
        '六': 6,
        '七': 7,
        '八': 8,
        '九': 9,
        #2 digits 十
        '十': 10,
        '十一': 11,
        '二十': 20,
        '二十一': 21,
        #3 digits 百
        '一百': 100,
        '一百零一': 101,
        '一百一十': 110,
        '一百二十三': 123,
        #4 digits 千
        '一千': 1000,
        '一千零一': 1001,
        '一千零一十': 1010,
        '一千一百': 1100,
        '一千零二十三': 1023,
        '一千二百零三': 1203,
        '一千二百三十': 1230,
        #5 digits 万
        '一万': 10000,
        '一万零一': 10001,
        '一万零一十': 10010,
        '一万零一百': 10100,
        '一万一千': 11000,
        '一万零一十一': 10011,
        '一万零一百零一': 10101,
        '一万一千零一': 11001,
        '一万零一百一十': 10110,
        '一万一千零一十': 11010,
        '一万一千一百': 11100,
        '一万一千一百一十': 11110,
        '一万一千一百零一': 11101,
        '一万一千零一十一': 11011,
        '一万零一百一十一': 10111,
        '一万一千一百一十一': 11111,
        #6 digits 十万
        '十万零二千三百四十五': 102345,
        '十二万三千四百五十六': 123456,
        '十万零三百五十六': 100356,
        '十万零三千六百零九': 103609,
        #7 digits 百万
        '一百二十三万四千五百六十七': 1234567,
        '一百零一万零一百零一': 1010101,
        '一百万零一': 1000001,
        #8 digits 千万
        '一千一百二十三万四千五百六十七': 11234567,
        '一千零一十一万零一百零一': 10110101,
        '一千万零一': 10000001,
        #9 digits 亿
        '一亿一千一百二十三万四千五百六十七': 111234567,
        '一亿零一百零一万零一百零一': 101010101,
        '一亿零一': 100000001,
        #10 digits 十亿
        '十一亿一千一百二十三万四千五百六十七': 1111234567,
        #11 digits 百亿
        '一百一十一亿一千一百二十三万四千五百六十七': 11111234567,
        #12 digits 千亿
        '一千一百一十一亿一千一百二十三万四千五百六十七': 111111234567,
        #13 digits 万亿
        '一万一千一百一十一亿一千一百二十三万四千五百六十七': 1111111234567,
        #14 digits 十万亿
        '十一万一千一百一十一亿一千一百二十三万四千五百六十七': 11111111234567,
        #17 digits 亿亿
        '一亿一千一百一十一万一千一百一十一亿一千一百二十三万四千五百六十七': 11111111111234567,
    }

    for each in test_map:
        assert(test_map[each] == zhnum2int(each))

def all_zh_num2float(s):
    pattern = r'^{}$'.format(RegexKit.all_zh_num)  # 需要加上开始结束标志。
    res = re.match(pattern, s)
    # print(res.groupdict())
    if res.group('num') != None:
        # 说明是阿拉伯数字和中文数字结合型。
        # 在该型中，中文数字识别为阿拉伯数字的数量级，需相乘。
        base = num2float(res.group('num'))
        mag = zh_mag2float(res.group('zh_mag'))
        value = base * mag
    elif res.group('zh_num') != None:
        # 说明是纯中文数字型。
        # 在该型中，中文数字识别为阿拉伯数字的中文写法，需转化。
        value = float(zh_num2int(res.group('zh_num')))
    return value


def zh_mag2float(s):
    if type(s) is not str:
        return 0
    mag_dict = {'纳':1e-9, '微':1e-6, '毫':1e-3,
                '': 1, '十': 10, '百': 1e2, '千': 1e3, '万': 1e4,
                '十万': 1e5, '百万': 1e6, '千万': 1e7, '亿': 1e8}
    return mag_dict[s]

if __name__ == '__main__':
    _testdrive_num2float()
