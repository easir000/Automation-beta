from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def verify_page_title(self, expected_title):
        WebDriverWait(self.driver, 10).until(EC.title_is(expected_title))
        print("Home page is visible successfully.")

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver

    def open_product_detail(self):
        product_link = self.driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/div[1]/div[3]/div/div[2]/ul/li/a")
        self.driver.execute_script("arguments[0].click();", product_link)
        print("Clicked 'View Product' link.")
        
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2")))
        print("Product detail is opened successfully.")

    def increase_quantity(self, quantity):
        quantity_input = self.driver.find_element(By.CSS_SELECTOR, '.product-information span input') 
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))
        print("Increased quantity to", quantity)

    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.XPATH, "/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button")
        add_to_cart_button.click()
        print("Clicked 'Add to cart' button.")

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def view_cart(self):
        view_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/div/div[2]/div[1]/div/div/div[2]/p[2]/a/u")))
        view_cart_button.click()
        print("Clicked 'View Cart' button.")
        time.sleep(5)

    def verify_product_in_cart(self, product_name, expected_quantity):
        product_name_element = self.driver.find_element(By.XPATH, "/html/body/section/div/div[2]/table/tbody/tr/td[2]/h4/a")
        quantity_input_element = self.driver.find_element(By.XPATH, "/html/body/section/div/div[2]/table/tbody/tr/td[4]/button")
        
        actual_quantity = quantity_input_element.get_attribute("data-max")
        print("Actual Quantity in Cart:", actual_quantity)
        
        assert product_name_element.text == product_name, f"Product name mismatch in cart. Actual: {product_name_element.text}, Expected: {product_name}"
        assert actual_quantity == str(expected_quantity), f"Quantity mismatch in cart. Actual: {actual_quantity}, Expected: {expected_quantity}"
        
        print("Product with exact quantity is displayed in cart.")


# ... (other code)

if __name__ == "__main__":
    url = 'http://automationexercise.com'
    expected_product_name = "Men Tshirt"  # Replace with the expected product name
    expected_quantity = 4
    
    driver = webdriver.Chrome()
    home_page = HomePage(driver)
    product_detail_page = ProductDetailPage(driver)
    cart_page = CartPage(driver)
    
    home_page.navigate_to(url)
    home_page.verify_page_title("Automation Exercise")
    
    product_detail_page.open_product_detail()
    product_detail_page.increase_quantity(expected_quantity)
    product_detail_page.add_to_cart()
    
    cart_page.view_cart()
    cart_page.verify_product_in_cart(expected_product_name, expected_quantity)
    
    driver.quit()
