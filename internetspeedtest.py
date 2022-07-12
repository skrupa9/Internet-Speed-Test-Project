import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import paths


class InternetSpeedTest:

    def __init__(self):
        self.driver = webdriver.Chrome(paths.DRIVER_PATH)
        self.driver.get(paths.SPEED_TEST_URL)
        self.download_speed = "-"
        self.upload_speed = "-"
        self.result_id = "-"

    def get_internet_speed(self):
        privacy_accept_btn = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        privacy_accept_btn.click()
        start_btn = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_btn.click()
        time.sleep(60)
        download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                      'div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                                    'div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

        measure_id = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                        'div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a')
        self.download_speed = download.text
        self.upload_speed = upload.text
        self.result_id = measure_id.text

    def save_results(self):
        pass
