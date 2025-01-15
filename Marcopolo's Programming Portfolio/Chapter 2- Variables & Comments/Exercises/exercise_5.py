usbPrice = 6
money = 50
totalUSB = int(money/usbPrice)
change = money%usbPrice
print("The girl has £" + str(money) + ". Each USB stick costs £" + str(usbPrice) + ". If she spends as much money as she can on the USB sticks, she will have bought " + str(totalUSB) + " USB sticks and have £" + str(change) + " in change.")