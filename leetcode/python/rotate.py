def  rotate(x, y):
    dict_x = {}
    dict_y = {}
    for i in range(len(x)):
        rot_x = x[i:] + x[:i]
        rank = 0
        length = len(rot_x)
        for j in range(len(rot_x)):
            rank += (ord(rot_x[j]) - ord('a')) * (length - j)
        dict_x[rank] = rot_x
        
    for i in range(len(y)):
        rot_y = y[i:] + y[:i]
        rank = 0
        length = len(rot_y)
        for j in range(len(rot_y)):
            rank += (ord(rot_y[j]) - ord('a')) * (length - j)
        dict_y[rank] = rot_y
    
    print "dict", dict_x, dict_y
    high_x = max(dict_x.keys())
    high_y = max(dict_y.keys())
    
    return dict_x[high_x] + dict_y[high_y]
