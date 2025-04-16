# powcd2d
PythonからWindowsのDirect2D、DirectWrite、DIGI、WICを使いやすくするパッケージです。comtypes、powcに依存します。 

次のようなコードが書けます。

**WICコンポーネントの列挙**

```py
from powcd2d.wic import WICImagingFactory

factory = WICImagingFactory.create()

for info in factory.iter_infos_all():
    print((info.friendlyname, info.friendlyname, info.componenttype))
```
