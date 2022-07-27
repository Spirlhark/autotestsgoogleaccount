from pages.BasePage import BasePage
import allure
from selenium.webdriver.common.by import By


class PeopleSharingPage(BasePage):
    locator_dictionary = {
        "tabPeopleSharingPage": (By.CSS_SELECTOR, ".HJOYVi12"),
        "openContactsPage": (By.PARTIAL_LINK_TEXT, 'Начать')
        }

    @allure.step("Tab People Sharing Page")
    def tabPeopleSharing(self):
        self.visit(self.base_url)
        # time.sleep(2)
        self.find_element(*self.locator_dictionary['tabPeopleSharingPage']).click()

    @allure.step("Open Contacts Page")
    def openContacts(self):
        self.find_element(*self.locator_dictionary['openContactsPage']).click()

    @allure.step('Open Family Create Page')
    def examination(self):
        assert self.browser.current_url == 'https://myaccount.google.com/family/create'