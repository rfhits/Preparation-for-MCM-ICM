# 转载自
# https://blog.csdn.net/weixin_39594447/article/details/88145028

import pandas as pd
data = [
    [102.4, 102.8, 103.1, 102.9, 103.3, 103.5, 103.6,
        104.4, 105.1, 104.6, 104.9, 104.9, 105.4],
    [105.2, 105.9, 106.1, 105.7, 106.8, 107.5, 108.0,
        110.1, 117.1, 109.6, 110.3, 111.0, 111.7],
    [101.7, 101.7, 101.7, 101.7, 101.6, 101.5,
     101.4, 101.5, 101.6, 101.8, 101.8, 101.9, 102.1],
    [98.9, 98.7, 98.8, 99.0, 99.2, 98.8, 98.5,
     98.7, 99.3, 100.1, 99.8, 100.4, 100.8],
    [99.3, 99.5, 99.7, 100.0, 100.2, 100.4, 100.4,
     100.5, 100.7, 101.2, 101.4, 101.4, 101.9],
    [102.5, 102.8, 103.2, 103.2, 103.3, 103.3, 103.4,
     103.7, 104.0, 104.0, 103.2, 103.0, 103.2],
    [100.0, 100.0, 100.1, 99.7, 99.3, 99.4, 99.3,
     99.5, 99.3, 99.3, 99.9, 99.7, 100.1],
    [100.3, 100.4, 100.6, 100.9, 101.1, 101.2, 101.2,
     100.9, 100.6, 100.7, 101.0, 100.3, 100.5],
    [100.3, 104.5, 105.0, 105.0, 104.8, 104.4, 104.3,
     104.9, 105.8, 106.0, 106.8, 106.1, 106.6]
]

def getGM(data):
    ndata = pd.DataFrame(data)
    meandata = ndata.mean(axis=1)   # 要探究第一列和其他列的相关性
    r,c = ndata.shape
    for item in range(r):
        ndata.iloc[item] = ndata.iloc[item]/meandata[item]
    diffdata = ndata.diff().iloc[1:].abs()
    a = diffdata.min().min()
    b = diffdata.max().max()
    res = (a + 0.5*b)/(diffdata +0.5*b)
    ret = res.sum(axis=1)/(c-1)
    return ret

print(getGM(data))