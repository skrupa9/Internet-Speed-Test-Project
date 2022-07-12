from internetspeedtest import InternetSpeedTest

speed_test = InternetSpeedTest()
print(speed_test.today)
speed_test.get_internet_speed()
speed_test.save_results()
