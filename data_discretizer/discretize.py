def discretize_money(std_value, category_dict='default'):
    if category_dict == 'default':
        category_dict = {"[0-500元]": [0, 500],
                         "[500-4000元]": [500, 4000],
                         "[4000-1万元]": [4000, 10000],
                         "[1万-5万元]": [10000, 50000],
                         "[5万-10万元]": [50000, 100000],
                         "[10万-20万元]": [100000, 200000],
                         "[20万-50万元]": [200000, 500000],
                         "[50万-100万元]": [500000, 1000000],
                         "[100万-500万元]": [1000000, 5000000],
                         "[500万元以上]": [5000000, 1e10]}
    for category in category_dict:
        interval = category_dict[category]
        if std_value >= interval[0] and std_value < interval[1]:
            return category
    print('Cannot discretize money value:', std_value)
    return ''

def discretize_weight(std_value, category_dict='default'):
    if category_dict == 'default':
        category_dict = {"[0-10克]": [0, 10],
                         "[10-50克]": [10, 50],
                         "[50-200克]": [50, 200],
                         "[200-1千克]": [200, 1000],
                         "[1-10千克]": [1000, 10000],
                         "[10-50千克]": [10000, 50000],
                         "[50-100千克]": [50000, 100000],
                         "[100-200千克]": [100000, 200000],
                         "[200-500千克]": [200000, 500000],
                         "[500-1吨]": [500000, 1000000],
                         "[1吨以上]": [1000000, 1e10]}
    for category in category_dict:
        interval = category_dict[category]
        if std_value >= interval[0] and std_value < interval[1]:
            return category
    print('Cannot discretize weight value:', std_value)
    return ''

def discretize_BAC(std_value, category_dict='default'):
    if category_dict == 'default':
        category_dict = {"[0-20mg/100ml]": [0, 20],
                         "[20-80mg/100ml]": [20, 80],
                         "[80-200mg/100ml]": [80, 200],
                         "[200以上mg/100ml]": [200, 10000000000.0]}
    for category in category_dict:
        interval = category_dict[category]
        if std_value >= interval[0] and std_value < interval[1]:
            return category
    print('Cannot discretize BAC value:', std_value)
    return ''
