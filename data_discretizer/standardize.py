def standardize_money(value, unit):
    std_unit = '元'
    lookup_table = {'元':1, '块钱':1, '角':1e-1, '分':1e-2}
    std_value = value * lookup_table[unit]
    return {'std_value':std_value, 'std_unit':std_unit}

def standardize_weight(value, unit):
    std_unit = '克'
    lookup_table = {'毫克':1e-3, '克':1, '千克':1e3, 'kg':1e3, '吨':1e6, '斤':5e2, '公斤':1e3}
    std_value = value * lookup_table[unit]
    return {'std_value':std_value, 'std_unit':std_unit}

def standardize_BAC(value, unit):
    std_unit = 'mg/100ml'
    lookup_table = {'mg/100ml':1, 'mg/ml':1e2, '毫克/100毫升':1, '毫克/毫升':1e2}
    std_value = value * lookup_table[unit]
    return {'std_value':std_value, 'std_unit':std_unit}
