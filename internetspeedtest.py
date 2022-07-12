import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
import paths


class InternetSpeedTest:

    def __init__(self):
        self.driver = webdriver.Chrome(paths.DRIVER_PATH)
        self.driver.get(paths.SPEED_TEST_URL)
        self.download_speed = "-"
        self.upload_speed = "-"
        self.result_id = "-"
        self.today = str(date.today())

    def get_internet_speed(self):
        time.sleep(3)
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
        self.download_speed = str(download.text)
        self.upload_speed = str(upload.text)
        self.result_id = str(measure_id.text)

    def save_results(self):
        self.driver.get(paths.FORM_LINK)
        date_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/'
                                                        'div[1]/div/div[1]/input')
        download_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/'
                                                            'div/div[1]/div/div[1]/input')
        upload_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/'
                                                          'div/div[1]/div/div[1]/input')
        id_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/'
                                                        'div[1]/div/div[1]/input')
        submit_btn = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/'
                                                        'span/span')
        date_field.send_keys(self.today)
        download_field.send_keys(self.download_speed)
        upload_field.send_keys(self.upload_speed)
        id_field.send_keys(self.result_id)
        submit_btn.click()
        self.driver.quit()


