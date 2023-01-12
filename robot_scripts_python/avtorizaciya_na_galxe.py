# скрипт запускается с http://ferma.zhernosek.xyz и имеет все встроенные модули
# https://t.me/zhernosek12

metamaskSelenium = MetamaskSelenium(driver, metamask_password)

driver.get("https://galxe.com/")

driver.minimize_window()

driver.set_window_size(1370, 1010)

metamaskSelenium.connect_to_website()

time.sleep(1)

driver.get("https://galxe.com/")

time.sleep(1)

metamaskSelenium.connect_to_website()

time.sleep(1)
