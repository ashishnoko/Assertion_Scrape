from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest
import time

class Test(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://quotes.toscrape.com/')

    def tearDown(self):
        self.driver.quit()

    def test_thirdboard(self):
      
        try:
           
            third_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span[@class="text"])[3]')))

            actual_text = third_element.text
           
            expected_text = ("There are only  to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle")

            
            self.assertEqual(actual_text, expected_text, "Third quote text does not match.")

        except Exception as e :
            print(e)
            
            
    def test_authorname(self):
      
            try:
           
                author_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//small[@class="author"])[3]')))

                name = author_name.text
                print(name)
           
                #expected_text = ("There are only  to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle")

            
                self.assertTrue(name.is_Displayed(), "Name not Found")

            except Exception as e :
                 print(e)
                 
                 
    def test_about_section(self):
      
            try:
           
                author_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span/a)[3]'))).click()

                

            except Exception as e :
                 print(e)
                 
    
                 
    
            
            
    
            
   
    


if __name__ == "__main__":
    unittest.main()