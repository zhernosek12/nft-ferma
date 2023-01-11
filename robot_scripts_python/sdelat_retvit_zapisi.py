# скрипт запускается с http://ferma.zhernosek.xyz и имеет все встроенные модули
# https://t.me/zhernosek12

driver.get(url)

time.sleep(5)

find_element_by_xpath_v2(driver, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span').click()

time.sleep(3)
