import random
""" 有3扇关闭的门，一扇门后停着汽车，另外两扇门后是山羊，主持人知道每扇门后是什么。
参赛者首先选择一扇门。在开启它之前，主持人会从另外两扇门中打开一扇门，露出门后的山羊。
此时，允许参赛者更换自己的选择。
请问，参赛者更换选择后，能否增加猜中汽车的机会？
 """
# 按照故事叙述方式模拟
# 合理性：不换是1/3；换的话，因为开门后排除一🐏，只剩一🐏一🚗，所以如果我现在选🐏换后得🚗，现在🚗换后🐏。现在是🐏的概率就是得🚗的概率，即2/3。
total = 100000
unNum, doNum = 0, 0
for i in range(total):  # undo test start
    sheepDoor = random.randint(1, 3)
    chosenDoor = random.randint(1, 3)
    openDoor = random.randint(1, 3)
    while openDoor == sheepDoor:
        openDoor = random.randint(1, 3)  # open isn't needed
    if sheepDoor == chosenDoor:
        unNum += 1
else:
    unPer = unNum / total
for i in range(total):  # do test
    sheepDoor = random.randint(1, 3)
    firstChosenDoor = random.randint(1, 3)
    openDoor = random.randint(1, 3)
    while openDoor == sheepDoor or openDoor == firstChosenDoor:  # for player's change, open another door instead of first choice
        openDoor = random.randint(1, 3)
    chosenDoor = random.randint(1, 3)
    while chosenDoor == openDoor or chosenDoor == firstChosenDoor:
        chosenDoor = random.randint(1, 3)
    if sheepDoor == chosenDoor:
        doNum += 1
else:
    doPer = doNum / total
print('change:{:%}, not change:{:%}.'.format(doPer, unPer))
