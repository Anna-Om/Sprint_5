import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from locators import MainPageLocators
from locators import AuthPageLocators
from locators import AdPageLocators
from locators import UserPageLocators

class TestCreatePost:
    def test_create_post_unauthorized_user(self, open_main_page):
        driver = open_main_page

        create_post_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.NEW_AD_BUTTON)
        )
        create_post_button.click()


        modal_window = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AuthPageLocators.WINDOW_AUTH)  
        )
        assert modal_window.is_displayed(), "Ошибка отображения окна"


        modal_title = driver.find_element(*AuthPageLocators.TOP_TEXT)
        assert modal_title.is_displayed(), "Ошибка отображения заголовка"

    def test_create_post_authorized_user(self, login):
        driver = login 


        create_ad_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.NEW_AD_BUTTON)
            )
        create_ad_button.click()
        System.out.println("Ошибка нажатия кнопки")


        title_field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AdPageLocators.NAME_AD)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", title_field)
        title_field.send_keys("Текст объявления")


        description_field = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(AdPageLocators.DISC_AD)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", description_field)
        description_field.send_keys("Текст с подробным описанием")

        price_field = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(AdPageLocators.PRICE_AD)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", price_field)
        price_field.send_keys("100")


        category_dropdown = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(AdPageLocators.DROPDOWN_CATEGORY)
        )
        category_dropdown.click()

        category_option = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(AdPageLocators.DROPDOWN_CATEGORY_BOOK)
        )
        category_option.click()


        city_dropdown = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(AdPageLocators.DROPDOWN_CITY)
        )
        city_dropdown.click()

        city_option = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(AdPageLocators.DROPDOWN_CITY_MOSCOW)
        )
        city_option.click()

        condition_label = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(AdPageLocators.RADIOBUTTON_NEW)
        )
        condition_label.click()


        publish_button = driver.find_element(*AdPageLocators.SUBMIT_AD_BUTTON)
        publish_button.click()

        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.LOGO_BUTTON)
            )
        element.click() 
        System.out.println("Ошибка нажатия кнопки")
        
        first_card = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(UserPageLocators.USER_FIRST_AD)
        )

        title_element = WebDriverWait(first_card, 10).until(
            EC.visibility_of_element_located(UserPageLocators.TOP_TEXT_ON_AD)
        )
        assert title_element.text == "Текст объявления", f"Ожидалось 'Текст объявления', получено '{title_element.text}'"


        city = first_card.find_element(*UserPageLocators.CITY_ON_AD).text
        assert city == "Москва", f"Ожидалось 'Москва', получено '{city}'"


        price = first_card.find_element(*UserPageLocators.PRICE_ON_AD).text
        assert price == "100", f"Ожидалось '100', получено '{price}'"