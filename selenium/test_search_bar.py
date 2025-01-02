import time
from contextlib import contextmanager
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

search_bar_xpath = "/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/span/span/span[1]/input"
search_text = "ThinkingFlow"

@contextmanager
def create_chrome_driver() -> Chrome:
    driver = Chrome()
    yield driver
    driver.quit()

def get_xyz_home_by_css(driver: Chrome):
    css_string = "div.p-20"

    board_element_list = driver.find_elements(
        By.CSS_SELECTOR, css_string
    )

    #print([tmp.text for tmp in board_element_list])

    for tmp in board_element_list:
        print(tmp.text)
        assert(search_text in tmp.text)

def search_agent(driver: Chrome):
    url = "https://xyz-beta.protago-dev.com/"
    driver.get(url)

    search_bar = driver.find_element(
        By.XPATH, search_bar_xpath
    )

    for i in search_text:
        search_bar.send_keys(i)
        time.sleep(0.5)

    search_bar.send_keys(Keys.ENTER)
    time.sleep(2)

if __name__ == '__main__':
    with create_chrome_driver() as chrome_driver:
        search_agent(driver=chrome_driver)
        get_xyz_home_by_css(driver=chrome_driver)
