from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Step Definitions

# Login
driver = webdriver.Chrome()
driver.get("http://localhost:8087")
driver.maximize_window()
username = driver.find_element(By.XPATH, "//input[@name='username']")
username.send_keys("admin")
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("12345678")
login_button = driver.find_element(By.XPATH, "//button[@type='button']")
login_button.click()

# Navigate to shared files
shared_files_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/share/page/context/shared/sharedfiles']"))
)
shared_files_link.click()

# Click on the file
file_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Fichier Test 11']"))
)
file_link.click()

# Ajouter aux favoris
link_favorite = driver.find_element(By.XPATH, "//a[text()='Favorite']")
link_favorite.click()

# clique Back dans le navigateur
driver.back()

# Clique link to my documents

link_my_documents = driver.find_element(By.XPATH, "//a[@class='filter-link filter0'][text()='All Documents']")
link_my_documents.click()

# Clique Link to My favorites
link_favorite = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='filter-link filter0'][text()='My Favorites']"))
)
link_favorite.click()

# Remove file from favorites
link_remove_file = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='item item-social']/a"))
)
link_remove_file.click()

# Logout and close browser
admin_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "HEADER_USER_MENU_POPUP"))
)
admin_button.click()
logout_button = driver.find_element(By.ID, "HEADER_USER_MENU_LOGOUT_text")
logout_button.click()
driver.quit()
