# Python BOT for Google's T-Rex Game
This is the T-Rex game im using for this example:
http://www.trex-game.skipser.com/
### Libraries needed
```
pip install pillow
pip install pyautogui
pip install numpy
```
---
### Setup
#### Step 1
```
git clone https://github.com/0x414b/trex-bot.git
cd trex-bot

python -m venv trex_env
source trex_env/bin/activate

pip install pillow
pip install pyautogui
pip install numpy
```
#### Step 2
First you'll need to place your browser with the game at the left side of the screen,
and your IDE in the right.
![Browser position](https://raw.githubusercontent.com/0x414b/trex-bot/master/browser_position.png)

#### Step 3
Once you've done this, you have to specify the width of your screen resolution.
```
screen_width = 1920   # In my case it's 1920  // 2560 would be for MacBook Pro for example.
```
#### Step 4
Run the code!
```
python trex.py
```
![JUMP](https://raw.githubusercontent.com/0x414b/trex-bot/master/trex.gif)
---
### Optional Instructions
In case you want to tweak the bot, here's a simple graph of the coordinates.
![Graph](https://raw.githubusercontent.com/0x414b/trex-bot/master/trex.PNG)
The origin point will be the T-Rex top-right corner.
```
dinosaur = [x, y]   # For example [221, 374]
```
From here the hitbox distance will be measured in pixels as n.
```
hitbox_distance = n  # Specifying the distance is optional. Default is 0.
```
The hitbox area is defined in n pixels - origin point coordinates.
```
hitbox_area = [x1, y1, x2, y2]    # For example, if area is [60, 0, 100, 30], it would equal [281, 374, 321, 404]
```
---
### 
