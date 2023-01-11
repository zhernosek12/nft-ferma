# скрипт запускается с http://ferma.zhernosek.xyz и имеет все встроенные модули
# https://t.me/zhernosek12

driver.get("https://toshies.xyz/whitelist")

time.sleep(3)

find_element_by_xpath_v2(driver, '//*[@id="address"]').send_keys(mm_address)

time.sleep(1)

find_element_by_xpath_v2(driver, '//*[@id="email"]').send_keys(email)

time.sleep(1)

find_element_by_xpath_v2(driver, '/html/body/div/main/div[2]/main/div/div/div[2]/div/div/main/div/form/p[4]/select/option[2]').click()

time.sleep(1)

driver.execute_script("window.scrollTo(0,150)")

time.sleep(1)

find_element_by_xpath_v2(driver,"//button[contains(text(),'Register')]").click()

time.sleep(3)
