import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_form(self, first_name, last_name, email, mobile, dob, subjects, picture_path, address, state, city):
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)
        self.driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()
        self.driver.find_element(By.ID, "userNumber").send_keys(mobile)
        self.driver.find_element(By.ID, "dateOfBirthInput").send_keys(dob)
        self.driver.find_element(By.ID, "subjectsInput").send_keys(subjects)
        self.driver.find_element(By.ID, "uploadPicture").send_keys(picture_path)
        self.driver.find_element(By.ID, "currentAddress").send_keys(address)
        self.driver.find_element(By.ID, "state").click()
        self.driver.find_element(By.XPATH, f"//div[contains(text(),'{state}')]").click()
        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.XPATH, f"//div[contains(text(),'{city}')]").click()
        # self.driver.find_element(By.ID, "submit").click()
        element = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(5)

    def is_popup_visible(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))

    def get_popup_title(self):
        return self.driver.find_element(By.ID, "example-modal-sizes-title-lg").text

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    yield driver
    driver.quit()

def test_fill_form(driver):
    form_page = PracticeFormPage(driver)
    form_page.fill_form("John", "Travolta", "name@example.com", "1234567890", "01/01/2000", "Computer Science", r'C:\Users\vlad_\OneDrive\Изображения\ris2.jpg', "123 Street", "NCR", "Delhi")
    assert form_page.is_popup_visible()
    assert form_page.get_popup_title() == "Thanks for submitting the form"

