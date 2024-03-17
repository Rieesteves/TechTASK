from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome()  # Or specify the path to your WebDriver executable
driver.get("https://www.flipkart.com")

try:
    # Search for the product
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Samsung Galaxy S10")
    search_box.send_keys(Keys.RETURN)

    # Click on "Mobiles" in categories
    mobiles_category = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Mobiles")))
    mobiles_category.click()

    # Apply filters
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Brand']/following-sibling::div//div[text()='Samsung']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Assured']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Price -- High to Low']"))).click()

    # Read the set of results
    product_names = driver.find_elements(By.XPATH, "//div[@class='_4rR01T']")
    display_prices = driver.find_elements(By.XPATH, "//div[@class='_30jeq3 _1_WHN1']")
    product_links = driver.find_elements(By.XPATH, "//a[@class='IRpwTa' and @target='_blank']")

    # Create and print the list of products
    for name, price, link in zip(product_names, display_prices, product_links):
        print("Product Name:", name.text)
        print("Display Price:", price.text)
        print("Link to Product Details Page:", link.get_attribute('href'))

finally:
    # Close the browser
    driver.quit()
