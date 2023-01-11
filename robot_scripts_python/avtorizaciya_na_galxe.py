# скрипт запускается с http://ferma.zhernosek.xyz и имеет все встроенные модули
# https://t.me/zhernosek12

metamaskSelenium = MetamaskSelenium(driver, metamask_password)

driver.get("https://galxe.com/")

driver.minimize_window()

driver.set_window_size(1370, 1010)

try:
    # после авторизации просит авторизоваться
    metamaskSelenium.connect_to_website()
except:
    pass

time.sleep(1)

driver.get("https://galxe.com/")

try:
    # кроме этого просит ещё и подключить потом
    metamaskSelenium.connect_to_website()
except:
    pass

time.sleep(1)
