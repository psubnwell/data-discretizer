class RegexKit():
    # 这里括号内开头加注?P<xxx>的形式作用是
    # 1）将本表达式形成一个分组
    # 2）为该分组分配一个名字方便抽取
    # 后来想了想这件事或许应该由用户自己来分配名字比较好，伺后续改进

    # Basic regex.
    num = r'(?P<num>\d+[\d,，\s]*\.?\d*)'
    zh_num = r'(?P<zh_num>[零一二两三四五六七八九十百千万亿]+)'
    zh_mag = r'(?P<zh_mag>纳|微|毫||十|百|千|万|十万|百万|千万|亿)'
    currency_unit = r'(?P<currency_unit>元|块钱)'
    weight_unit = r'(?P<weight_unit>毫克|克|千克|kg|吨|斤|公斤)'
    BAC_unit = r'(?P<BAC_unit>mg/100ml|mg/ml|毫克/100毫升|毫克/毫升)'
    # Mixed regex.
    mixed_zh_num = r'(?P<mixed_zh_num>{}[余多]?{})'.format(num, zh_mag)
    all_zh_num = r'(?P<all_zh_num>{}|{})[余多]?'.format(mixed_zh_num, zh_num)

