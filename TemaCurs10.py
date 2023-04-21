"""
1. Faceti o suita care sa contina testele voastre de la tema 9. Generati raportul.
2. Ganditi voi o clasa de test din paginile sugerate in tema 8
- Scrieti cel putin 3 functii de test intr-o clasa (cum am facut la clasa)
Folositi firefox in loc de chrome (ce doriti voi, cate functii de test doriti,
freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test).
Bine de stiut: o functie de test este echivalentul unui test case
Mai multe aici:
https://www.tutorialspoint.com/software_testing_dictionary/test_case.htm

https://www.phptravels.net/
http://automationpractice.com/index.php
https://formy-project.herokuapp.com/
https://the-internet.herokuapp.com/
https://www.techlistic.com/p/selenium-practice-form.html
Sau puteti alege voi ce pagina doriti
"""

# Ex 1

# import unittest
# from time import sleep

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# import unittest

# from TemaCurs9 import Login
# import HtmlTestRunner

# class TestSuite(unittest.TestCase):
# def test_suite(self):
# test_to_run = unittest.TestSuite()
# test_to_run.addTests([

# unittest.defaultTestLoader.loadTestsFromTestCase(Login)
# ])
# runner = HtmlTestRunner.HTMLTestRunner(
# combine_reports = True,
# report_name = "First Report",
# report_title = "First-report"
# )
# runner.run(test_to_run)


# Ex 2
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# firefox = webdriver.Firefox()
# firefox.get("https://phptravels.net/")

import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Hotels(unittest.TestCase):
    CITY_NAME = (By.ID, 'select2-hotels_city-container')
    CHECK_IN = (By.ID, 'checkin')
    CHECK_OUT = (By.ID, 'checkout')
    TRAVELLERS = (By.CLASS_NAME, 'dropdown-toggle dropdown-btn travellers waves-effect')

    def setUp(self):
        self.firefox = webdriver.Firefox()
        self.firefox.maximize_window()
        self.firefox.implicitly_wait(3)
        self.firefox.get("https://phptravels.net/")

    def tearDown(self):
        self.firefox.quit()

    def test_url(self):
        actual_url = self.firefox.current_url
        expected_url = "https://phptravels.net/"
        assert actual_url == expected_url, f"Invalid url: expected:{expected_url}, actual: {actual_url}"

    def test_city_name(self):
        self.firefox.find_element(By.ID, 'checkin').send_keys('Cluj-Napoca')
        self.firefox.find_element(By.XPATH, "//*[@id='checkin']").click()

    def test_titlu(self):
        titlu = self.firefox.title
        expected_titlu = "PHPTRAVELS | Travel Technology Partner - PHPTRAVELS"
        assert titlu == expected_titlu, f"Titlul invalid, expected:{expected_titlu}, actual: {titlu}"
