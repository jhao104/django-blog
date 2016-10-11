# 标题
```
import itertools


def containAny(seq, aset):
    """
    判断seq序列中是否有任意字符存在于aset中
    """
    for item in itertools.ifilter(aset.__contains__, seq):
      # item has in aset
      return True
    return False
```