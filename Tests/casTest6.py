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

# Partager sur reseaux sociaux
link_share = driver.find_element(By.XPATH, "//a[text()='Shared']")
link_share.click()

# clique sur bouton pour partager sur facebook
link_share_facebook = driver.find_element(By.XPATH, "//div[@class='bd']//a[@title='Share using Facebook']")
link_share_facebook.click()
# driver.back()
# Redirection vers la page facebook
original_window = driver.current_window_handle
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
new_window_text = driver.title
assert new_window_text == 'Facebook'
driver.close()
driver.switch_to.window(original_window)

# Logout and close browser
admin_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "HEADER_USER_MENU_POPUP"))
)
admin_button.click()
logout_button = driver.find_element(By.ID, "HEADER_USER_MENU_LOGOUT_text")
logout_button.click()
driver.quit()
