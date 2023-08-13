from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch the browser
def launch_browser():
    driver = webdriver.Chrome()  # You can choose other browsers as well
    return driver

# Navigate to the URL
def navigate_to_url(driver, url):
    driver.get(url)

# Verify home page is visible
def verify_home_page(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise"))
        print("Home page is visible successfully.")
    except:
        print("Home page verification failed.")

# Click 'View Product' link
def click_view_product_link(driver):
    product_link = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[2]/a")
    driver.execute_script("arguments[0].click();", product_link)
    print("Clicked 'View Product' link.")

# Enter product name and click search button
def search_for_product(driver, product_name):
    search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'search_product')))
    search_input.send_keys(product_name)
    search_button = driver.find_element(By.ID, 'submit_search')
    search_button.click()
    print("Entered product name and clicked search button.")

# Verify 'SEARCHED PRODUCTS' is visible
def verify_searched_products(driver):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section[2]/div/div/div[2]/div/h2[contains(text(), 'Searched Products')]")))
        print("'SEARCHED PRODUCTS' is visible.")
    except Exception as e:
        print("'SEARCHED PRODUCTS' is not visible. Error:", e)

# Verify all products related to search are visible
def verify_visible_products(driver, product_names):
    failed_products = []
    
    for product_name in product_names:
        product_selector = f"[title='{product_name}']"
        product_elements = driver.find_elements(By.CSS_SELECTOR, product_selector)
        
        for product_element in product_elements:
            try:
                assert product_element.is_displayed(), f"Product '{product_name}' is not visible."
                print(f"Product '{product_name}' is visible.")
            except AssertionError:
                failed_products.append(product_element)
    
    if not failed_products:
        print("All products related to the search are visible.")
    else:
        print("Some products related to the search are NOT visible.")

# Close the browser
def close_browser(driver):
    driver.quit()

if __name__ == "__main__":
    url = 'http://automationexercise.com'
    product_names = ["Sleeveless Dress", "Stylish Dress", "Sleeves Top and Short - Blue & Pink"]
    
    driver = launch_browser()
    navigate_to_url(driver, url)
    verify_home_page(driver)
    click_view_product_link(driver)
    search_for_product(driver, 'Men Tshirt')
    verify_searched_products(driver)
    verify_visible_products(driver, product_names)
    close_browser(driver)
