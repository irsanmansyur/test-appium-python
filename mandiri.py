import time
from appium import webdriver
import sys
appium_address = "http://192.168.111.14:4723/wd/hub"
# appium_address = "http://localhost:4723/wd/hub"


def run(device_id):
    desired_caps = dict(
        platformName='Android',
        platformVersion='10',
        appPackage='id.bmri.livin',
        appActivity="com.bankmandiri.md.presentation.ui.MainActivity",
        noReset=True,
        udid=device_id,
        uiautomator2ServerInstallTimeout=50000,
    )

    driver = webdriver.Remote(appium_address, desired_caps)
    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    ip = sys.argv[-1]
    run(ip)
