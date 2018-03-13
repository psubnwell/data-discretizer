import json
from data_discretizer import recognize

def testdrive_recognize_money():
    example = ['盗窃28万元。',  # 第一型数字：阿拉伯数字+中文数量级。
               '盗窃1千元。',
               '盗窃95.8万元。',
               '盗窃2百万元。',
               '盗窃4，200元。',
               '盗窃4，200, 000元。',
               '盗窃十一万元。',  # 第二型数字：纯中文数字。
               '盗窃一千元。',
               '盗窃两千七百块钱。']
    for i in example:
        print(recognize.recognize_money(i))
        print()

def testdrive_recognize_weight():
    example = ['73.3公斤',
               '8千克',
               '8000克',
               '8千千克',
               '8百克',
               '8吨',
               '十余克']
    for i in example:
        print(recognize.recognize_weight(i))
        print()

def testdrive_recognize_BAC():
    example = ['酒精浓度为117.4mg/100ml。',
               '117.4毫克/100毫升。',
               '120毫克/毫升',
               '120mg/ml']
    for i in example:
        print(recognize.recognize_BAC(i))
        print()

if __name__ == '__main__':
    testdrive_recognize_money()
    testdrive_recognize_weight()
    testdrive_recognize_BAC()
