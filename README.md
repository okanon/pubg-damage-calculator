<h1 align="center">
	<img width="330" height="200" src="https://www.pngarts.com/files/4/PlayerUnknowns-Battlegrounds-PUBG-PNG-Free-Download.png" alt="Awesome">
</h1>

# pubg-damage-calculator
## What is this??
This is to calculate the weapon damage of PUBG using python. 
Currently it is only python, but in the future we plan to distribute it in binary format that can be used with each distribution such as Windows and OS X.

## Damage Calculation
<h1 align="center">
	<img src="https://i.imgur.com/wMxJl1S_d.jpg?maxwidth=640&shape=thumb&fidelity=medium" alt="Awesome">
</h1>

## Requirements
__python >= 3.4__

## How to Use
```
python3 main.py
```
or
```python
from hook.pubg import PUBG

cc = PUBG("Kar98K", 3, 3) # PUBG(Weapon, Helmet Level, Vest Level)
cc.calc() # calc(Range) default=1
```
