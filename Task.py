from socket import timeout
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from xml.dom.minidom import Element
import time
import math
import logging
import unittest
# 3. Click “See All Teams”, select Quality Assurance, click “See all QA jobs”,
# filter jobs by Location - Istanbul, Turkey and department - Quality Assurance, check presence of jobs list

# 4. Check that all jobs’ Position contains “Quality Assurance”, Department contains “Quality Assurance”, Location contains  “Istanbul, Turkey” and “Apply Now” button

# 5. Click “Apply Now” button and check that this action redirects us to Lever Application form page

# - Test case should be written using any programming language and framework (Python or Java + Selenium would be preferable)
# - Test case should fully meet POM requirements
# - Buttons, dropdowns and other elements should have optimized Xpath and CSS selectors
# - Assertions should be used in test case


logging.basicConfig(  # Set up logging
    filename="Task.log",
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(message)s",
    datefmt="%m/%d %H:%M:%S",
)


class Task(unittest.TestCase):

    def setUp(self):
        service = FirefoxService(
            executable_path=GeckoDriverManager().install())

        ffOptions = Options()
        ffOptions.add_argument("-profile")
        ffOptions.add_argument(
            r"C:\Users\Zeus\AppData\Roaming\Mozilla\Firefox\Profiles\6qpmkdav.ZeusNew")
        self.driver = Firefox(service=service, options=ffOptions)
        # self.driver.maximize_window()  # For maximizing window

    # 1. Visit https://useinsider.com/ and check Insider home page is opened or not
    def test_home_page(self):
        self.driver.get(
            "https://useinsider.com/"
        )
        self.assertTrue(self.driver.current_url == "https://useinsider.com/",
                        "Insider home page is not opened")
        logging.info("Insider home page is opened")

    # 2. Select “More” menu in navigation bar, select “Careers” and check Career page,
    # its Locations, Teams and Life at Insider blocks are opened or not
    def test_careers_page(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "x").click()

    # def tearDown(self):
    #         self.driver.close()


if __name__ == '__main__':
    unittest.main()
