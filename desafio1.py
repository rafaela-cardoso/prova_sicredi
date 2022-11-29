from datetime import datetime
import time
import os
import unittest
from fielduteis import *
import xmlrunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


RESULTS_FOLDER = "test-reports/sicredi"
START_DATETIME = datetime.now()


class SicrediTest(unittest.TestCase):
    def setUp(self):

        is_running_in_ci = os.environ.get('CI') == 'true'
        selenium_url = os.environ.get('SELENIUM_URL')
        use_remote_browser = selenium_url != ''

        options = webdriver.ChromeOptions()

        if use_remote_browser or is_running_in_ci:
            options.add_argument("--no-sandbox")
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-dev-shm-usage")

        if is_running_in_ci:
            self.browser = webdriver.Remote(selenium_url, options=options)
        else:
            service = Service(os.environ.get("WEBDRIVE_PATH"))
            self.browser = webdriver.Chrome(service=service)

        payment_url = os.environ.get('FRONT_MICRO')

        print("Browser: ", self.browser.name)
        print("Acessando: ", payment_url)
        self.browser.get(payment_url)
        drop = Select (self.browser.find_element(By.ID,"switch-version-select"))
        drop.select_by_value ("/v1.x/demo/my_boss_is_in_a_hurry/bootstrap-v4")
        self.addCleanup(self.browser.quit)


    def screen_shot(self, step_name):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        print("tirando screenshot: " + step_name)

        self.browser.get_screenshot_as_file(
            os.path.join(RESULTS_FOLDER, "ss_" + START_DATETIME.strftime("%Y-%m-%d__%H-%M-%S") + "_" + step_name + ".png"))


    def testecadastro(self):
    #Etapa 1, preenchendo os campos    
        time.sleep(3)

        self.browser.find_element(By.CSS_SELECTOR, 'a.btn.btn-default.btn-outline-dark').click()
        time.sleep(1)

        self.screen_shot(step_name="test1click_addcustomer")

        time.sleep(1)

        fill_name (self.browser)

        fill_lastname (self.browser)

        fill_firstname (self.browser)

        fill_phone (self.browser)

        fill_adress1 (self.browser)

        fill_adress2 (self.browser)

        fill_city (self.browser)

        fill_state (self.browser)

        fill_postalcode (self.browser)

        fill_country (self.browser)

        fill_employeer (self.browser)

        fill_creditlimit (self.browser)

        self.screen_shot(step_name="test1campos_preenchidos")
        time.sleep(1)

        finalizar = self.browser.find_element(By.ID, "form-button-save")
        finalizar.click()
        time.sleep(3)

        self.screen_shot(step_name="test1cadastro_realizado")
        
    #Etapa 2, validando a mensagem de sucesso
        time.sleep(3)
        self.screen_shot(step_name="salvo")

        textoElement = self.browser.find_element(By.ID, "report-success").text;
        assert textoElement == "Your data has been successfully stored into the database. Edit Record or Go back to list", "A mensagem de cadastro é inválida"

    #Desafio 2
        self.browser.find_element(By.XPATH, "//*[@id='report-success']/p/a[2]").click()
        time.sleep(3)

        self.browser.find_element(By.NAME, "customerName").send_keys("Teste Sicredi")
        time.sleep(5)
        self.browser.find_element(By.CLASS_NAME, "select-all-none").click()
        self.screen_shot(step_name="selecionando")
        self.browser.find_element(By.XPATH, "//*[@id='gcrud-search-form']/div[2]/table/thead/tr[2]/td[2]/div[1]/a").click()
        alert = self.browser.find_element(By.CSS_SELECTOR, 'p.alert-delete-multiple-one').text;
        assert alert == "Are you sure that you want to delete this 1 item?", "A mensagem de alerta é inválida ou existe mais de um item para deletar"
        self.browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(2)
        conf = self.browser.find_element(By.XPATH, "/html/body/div[3]").text;
        #assert conf == "Your data has been successfully deleted from the database.", "Dados não foram deletados"
        time.sleep(5)
        self.screen_shot(step_name="deletado")
        time.sleep(5)

if __name__ == '__main__':
    os.makedirs(RESULTS_FOLDER, exist_ok=True)
    unittest.main(verbosity=2,
                  testRunner=xmlrunner.XMLTestRunner(output=RESULTS_FOLDER),
                  failfast=False, buffer=False, catchbreak=False)
