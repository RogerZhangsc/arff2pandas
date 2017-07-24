# arff2pandas
A bidirectional converter arff to pandas

## install
```sh
pip install arff2pandas
```

require
- python 3.*
- liac-arff
- pandas


## usage
import
```py
from arff2pandas import a2p
```

load arff from file to pandas.DataFrame
```py
with open('sample.arff') as f:
    df = a2p.load(f)
    print(df)
```

load arff from str to pandas.DataFrame

```py
arff_str = '@RELATION feature\n\n@ATTRIBUTE power NUMERIC\n@ATTRIBUTE label {good,bad}\n\n@DATA\n0.3,good\n0.5,bad'
df = a2p.loads(arff_str)
print(df)
```

dump pandas.DataFrame to file
```py
import pandas as pd
df = pd.DataFrame({
    'power@NUMERIC':[0.5,0.2],
    'label@{good,bad}':['good','bad']
})
with open('sample.arff','w') as f:
    a2p.dump(df,f)
```

dump pandas.DataFrame to str
```py
import pandas as pd
df = pd.DataFrame({
    'power@NUMERIC':[0.5,0.2],
    'label@{good,bad}':['good','bad']
})
print(a2p.dumps(df))
```
