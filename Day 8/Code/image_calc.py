from subprocess import run
from opencvloc import locateCenterImage
import pyautogui as py  # 라이브러리 대체

run(['calc'])

for i in range(1, 10):
    x, y = locateCenterImage("../Image/{}.PNG".format(i))
    py.click(x, y)

    if i < 9:
        x, y = locateCenterImage("../Image/+.PNG")
    else:
        x, y = locateCenterImage("../Image/=.PNG")


# time.sleep(1)

# x, y = locateCenterImage('../Image/5.PNG')
# py.click(x,y)

# x, y = locateCenterImage('../Image/5.PNG')
# py.click(x,y)

# x, y = locateCenterImage('../Image/5.PNG')
# py.click(x,y)

# x, y = locateCenterImage('../Image/5.PNG')
# py.click(x,y)
