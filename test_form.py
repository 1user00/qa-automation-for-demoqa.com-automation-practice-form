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
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(self.driver, 10)
#         self.first_name_input = (By.ID, "firstName")
#         self.last_name_input = (By.ID, "lastName")
#         self.email_input = (By.ID, "userEmail")
#         self.gender_radio = (By.XPATH, "//input[@name='gender']/following-sibling::label[1]")
#         self.mobile_input = (By.ID, "userNumber")
#         self.date_of_birth_input = (By.ID, "dateOfBirthInput")
#         self.subjects_input = (By.ID, "subjectsInput")
#         self.upload_input = (By.ID, "uploadPicture")
#         self.address_input = (By.ID, "currentAddress")
#         self.state_dropdown = (By.ID, "state")
#         self.city_dropdown = (By.ID, "city")
#         self.submit_button = (By.ID, "submit")
#
#     def open_page(self, url):
#         self.driver.get(url)
#
#     def scroll_down(self):
#         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     def fill_first_name(self, first_name):
#         self.wait.until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)
#
#     def fill_last_name(self, last_name):
#         self.wait.until(EC.visibility_of_element_located(self.last_name_input)).send_keys(last_name)
#
#     def fill_email(self, email):
#         self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)
#
#     def select_gender(self):
#         self.wait.until(EC.visibility_of_element_located(self.gender_radio)).click()
#
#     def fill_mobile(self, mobile):
#         self.wait.until(EC.visibility_of_element_located(self.mobile_input)).send_keys(mobile)
#
#     def fill_date_of_birth(self, date):
#         self.wait.until(EC.visibility_of_element_located(self.date_of_birth_input)).send_keys(date)
#
#     def fill_subjects(self, subjects):
#         self.wait.until(EC.visibility_of_element_located(self.subjects_input)).send_keys(subjects)
#
#     def upload_picture(self, file_path):
#         self.wait.until(EC.visibility_of_element_located(self.upload_input)).send_keys(file_path)
#
#     def fill_address(self, address):
#         self.wait.until(EC.visibility_of_element_located(self.address_input)).send_keys(address)
#
#     def select_state(self, state):
#         self.wait.until(EC.visibility_of_element_located(self.state_dropdown)).click()
#         self.driver.find_element(By.XPATH, f"//div[text()='{state}']").click()
#
#     def select_city(self, city):
#         self.wait.until(EC.visibility_of_element_located(self.city_dropdown)).click()
#         self.driver.find_element(By.XPATH, f"//div[text()='{city}']").click()
#
#     def submit_form(self):
#         self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
#
#
# class TestLoginForm:
#     @pytest.fixture(scope="class")
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.login_page = LoginPage(self.driver)
#         self.login_page.open_page("https://demoqa.com/automation-practice-form")
#         yield
#         self.driver.quit()
#
#     def test_fill_form(self, setup):
#         self.login_page.scroll_down()
#         self.login_page.fill_first_name("John")
#         self.login_page.fill_last_name("Doe")
#         self.login_page.fill_email("johndoe@example.com")
#         self.login_page.select_gender()
#         self.login_page.fill_mobile("1234567890")
#         self.login_page.fill_date_of_birth("01/01/2000")
#         self.login_page.fill_subjects("Computer Science")
#         self.login_page.upload_picture(r'C:\Users\vlad_\OneDrive\Изображения\ris2.jpg')
#         self.login_page.fill_address("123 Street")
#         self.login_page.select_state("NCR")
#         self.login_page.select_city("Delhi")
#         self.login_page.submit_form()
#         # Проверка успешного отправки формы
#         assert "Thanks for submitting the form" in self.driver.page_source
    # # Проверка введенных значений в таблице
    # table = self.driver.find_element(By.XPATH, "//div[contains(@class, '

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class DemoQAFormPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def open(self):
#         self.driver.get("https://demoqa.com/automation-practice-form")
#
#     def fill_first_name(self, name):
#         first_name_field = self.driver.find_element(By.ID, "firstName")
#         first_name_field.send_keys(name)
#
#     def fill_last_name(self, name):
#         last_name_field = self.driver.find_element(By.ID, "lastName")
#         last_name_field.send_keys(name)
#
#     def fill_email(self, email):
#         email_field = self.driver.find_element(By.ID, "userEmail")
#         email_field.send_keys(email)
#
#     def select_gender(self, gender):
#         gender_radios = self.driver.find_elements(By.NAME, "gender")
#         for radio in gender_radios:
#             if radio.get_attribute("value") == gender:
#                 radio.click()
#                 break
#
#     def fill_mobile(self, mobile):
#         mobile_field = self.driver.find_element(By.ID, "userNumber")
#         mobile_field.send_keys(mobile)
#
#     def fill_dob(self, dob):
#         dob_field = self.driver.find_element(By.ID, "dateOfBirthInput")
#         dob_field.send_keys(dob)
#
#     def fill_subjects(self, subjects):
#         subjects_field = self.driver.find_element(By.ID, "subjectsInput")
#         subjects_field.send_keys(subjects)
#
#     def upload_picture(self, picture_path):
#         picture_input = self.driver.find_element(By.ID, "uploadPicture")
#         picture_input.send_keys(picture_path)
#
#     def fill_address(self, address):
#         address_field = self.driver.find_element(By.ID, "currentAddress")
#         address_field.send_keys(address)
#
#     def select_state(self, state):
#         state_dropdown = self.driver.find_element(By.ID, "state")
#         state_dropdown.click()
#         state_option = self.driver.find_element(By.XPATH, f"//div[@id='state']//div[contains(text(), '{state}')]")
#         state_option.click()
#
#     def select_city(self, city):
#         city_dropdown = self.driver.find_element(By.ID, "city")
#         city_dropdown.click()
#         city_option = self.driver.find_element(By.XPATH, f"//div[@id='city']//div[contains(text(), '{city}')]")
#         city_option.click()
#
#     def submit_form(self):
#         submit_button = self.driver.find_element(By.ID, "submit")
#         submit_button.click()
#
#     def get_success_message(self):
#         success_message = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,
#                                                                                                 "//div[@class='modal-header']//h5[@id='example-modal-sizes-title-lg'][contains(text(), 'Thanks for submitting the form')]")))
#         return success_message
#
#     def get_table_values(self):
#         table_values = []
#         table_rows = self.driver.find_elements(By.XPATH, "//div[@class='table-responsive']//tr")
#         for row in table_rows:
#             columns = row.find_elements(By.TAG_NAME, "td")
#             for column in columns:
#                 table_values.append(column.text)
#         return table_values
#
#
# @pytest.fixture(scope="module")
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
#
# def test_fill_form(driver):
#     form_page = DemoQAFormPage(driver)
#     form_page.open()
#
#     form_page.fill_first_name("John")
#     form_page.fill_last_name("Doe")
#     form_page.fill_email("john.doe@example.com")
#     form_page.select_gender("Male")
#     form_page.fill_mobile("1234567890")
#     form_page.fill_dob("01-01-1990")
#     form_page.fill_subjects("Maths")
#     form_page.upload_picture("/path/to/picture")
#     form_page.fill_address("123 Main St")
#     form_page.select_state("NCR")
#     form_page.select_city("Delhi")
#     form_page.submit_form()
#
#     success_message = form_page.get_success_message()
#     assert success_message.is_displayed()
#
#     table_values = form_page.get_table_values()
#     assert "John" in table_values
#     assert "Doe" in table_values
#     assert "john.doe@example.com" in table_values
#     assert "Male" in table_values
#     assert "1234567890" in table_values
#     assert "01/01/1990" in table_values
#     assert "Maths" in table_values
#     assert "123 Main St" in table_values
#     assert "NCR" in table_values
#     assert "Delhi" in table_values
