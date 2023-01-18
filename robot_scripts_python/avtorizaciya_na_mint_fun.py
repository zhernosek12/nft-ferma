
driver.minimize_window()

driver.set_window_size(1370, 1010)

driver.set_window_position(100, 100, windowHandle='current')

metamaskSelenium = MetamaskSelenium(driver, metamask_password)

driver.get("https://mint.fun/feed/trending")

find_element_by_xpath_v2(driver, "//span[contains(text(),'Connect Wallet')]").click()

time.sleep(2)

find_element_by_xpath_v2(driver, "//span[contains(text(),'MetaMask')]").click()

time.sleep(2)

metamaskSelenium.connect_to_website()

time.sleep(1)

driver.get("https://mint.fun/feed/trending")

find_element_by_xpath_v2(driver, "//span[contains(text(),'Connect Wallet')]").click()

time.sleep(2)

find_element_by_xpath_v2(driver, "//span[contains(text(),'MetaMask')]").click()

time.sleep(2)

metamaskSelenium.connect_to_website()

time.sleep(1)
