from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


@given(u'Je suis connecté a l\'application avec un compte utilisateur')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.get("http://localhost:8087")
    username = context.driver.find_element(By.XPATH, "//input[@name='username']")
    username.send_keys("admin")
    password = context.driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("12345678")
    login_button = context.driver.find_element(By.XPATH, "//button[@type='button']")
    login_button.click()


@given(u'Je clique sur le lien \'Fichiers partagés\'')
def step_impl(context):
    fichiers_partages = context.driver.find_element(By.XPATH, "//a[@href='/share/page/context/shared/sharedfiles']")
    fichiers_partages.click()


@given(u'Je clique sur le fichier "FichierTest 11.jpg"')
def step_impl(context):
    file_link = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Fichier Test 11']"))
    )
    file_link.click()


@given(u'Je clique sur \'Voir dans le navigateur\'')
def step_impl(context):
    voir_dans_navigateur = context.driver.find_element(By.XPATH, "//a[@title='View In Browser']/span")
    voir_dans_navigateur.click()


@then(u'je vais etre rederige vers une page du navigateur et verifier le contenu')
def step_impl(context):
    original_window = context.driver.current_window_handle
    window_after = context.driver.window_handles[1]
    context.driver.switch_to.window(window_after)
    new_window_text = context.driver.find_element(By.XPATH, '//pre[normalize-space()="test"]').text
    assert new_window_text == 'test'
    context.driver.close()
    context.driver.switch_to.window(original_window)


@then(u'Je dois me deconnecter et fermer tous les navigateurs')
def step_impl(context):
    admin_button = context.driver.find_element(By.ID, "HEADER_USER_MENU_POPUP")
    admin_button.click()
    logout_button = context.driver.find_element(By.ID, "HEADER_USER_MENU_LOGOUT_text")
    logout_button.click()
