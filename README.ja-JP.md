<h1 align="center">
	<img width="330" height="200" src="https://www.pngarts.com/files/4/PlayerUnknowns-Battlegrounds-PUBG-PNG-Free-Download.png" alt="Awesome">
</h1>

# ぴーゆーびーじーだめーじけいさんき〜
## 何やねんこれは
PUBGの武器ダメージ計算をpythonで行う便利なスクリプト。将来的にはWindowsやOS Xなどの各ディストリビューションでも動作するバイナリ(例えばexeファイル)形式で公開する予定。

## ダメージ計算
<h1 align="center">
	<img src="https://i.imgur.com/wMxJl1S_d.jpg?maxwidth=640&shape=thumb&fidelity=medium" alt="Awesome">
</h1>

## 依存
__python >= 3.4__

## つかいかた
```
python3 main.py
```
もしくは
```python
from hook.pubg import PUBG

cc = PUBG("Kar98K", 3, 3) # PUBG(Weapon, Helmet Level, Vest Level)
cc.calc() # calc(Range) default=1
```

