from television import Television

tv1 = Television('1')
tv1.setChannel(2)
tv1.turnON()
tv1.setSize(40)

tv2 = Television('2')
tv2.setChannel(1)
tv2.turnON()
tv2.turnON()
tv2.setSize(21)
tv2.turnOFF()

tv3 = Television('3')
tv3.setSize(50)
tv3.turnOFF()

tv4 = Television('4')
tv4.setSize(60)
tv4.setChannel(4)
tv4.turnON()

tv5 = Television('5')
tv5.setSize(24)
tv5.setChannel(6)
tv5.isTVOn()
tv5.turnON()
tv5.turnOFF()
tv5.isTVOn()
