from selenium import webdriver
from selenium.webdriver.common.by import By

#Campos gerais de dados do usuário
def fill_name (browser):
    browser.find_element(By.NAME, "customerName").send_keys("Teste Sicredi")

def fill_lastname (browser):
    browser.find_element(By.NAME, "contactLastName").send_keys("Teste")

def fill_firstname (browser):
    browser.find_element(By.NAME, "contactFirstName").send_keys("Rafaela Cardoso")

def fill_phone (browser):
    browser.find_element(By.NAME, "phone").send_keys("51 9999-9999")

def fill_adress1 (browser):
    browser.find_element(By.NAME, "addressLine1").send_keys("Av Assis Brasil, 3970")

def fill_adress2 (browser):
    browser.find_element(By.NAME, "addressLine2").send_keys("Torre D")

def fill_city (browser):
    browser.find_element(By.NAME, "city").send_keys("Porto Alegre")

def fill_state (browser):
    browser.find_element(By.NAME, "state").send_keys("RS")

def fill_postalcode (browser):
    browser.find_element(By.NAME, "postalCode").send_keys("91000-000")

def fill_country (browser):
    browser.find_element(By.NAME, "country").send_keys("Brasil")

def fill_employeer (browser):
    browser.find_element(By.NAME, "salesRepEmployeeNumber").send_keys("Fixter")

def fill_creditlimit (browser):
    browser.find_element(By.NAME, "creditLimit").send_keys("200")
