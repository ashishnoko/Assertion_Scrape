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

    
            
    
                 
                 
    def test_about(self):
      
        try:
           
            about_section = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span/a)[3]'))).click()
          
            
            current_url = self.driver.current_url
            expected_url = "https://quotes.toscrape.com/author/Albert-Einstein/"
            
            self.assertEqual(current_url,expected_url,'URL doesnot match')
            
            
            
            
        except Exception as e :
            print(e)
            
            
    def test_url(self):
      
        try:
           
            about_section = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span/a)[3]'))).click()
          
            
            current_url = self.driver.current_url
            expected_url = "https://quotes.toscrape.com/author/Steve Martin/"
            
            self.assertEqual(current_url,expected_url,'URL doesnot match')
            
            
            
            
        except Exception as e :
            print(e)
            
               
            
    def test_totaltags(self):
      
        try:
           
           
            #tags_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"(//div[@class="tags"]/a[text()='life'])[1]")))
            total_tags = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div/a[@class="tag"]')))
            tags = len(total_tags)
            self.assertGreater(tags,5,"Error not found")
            
            
           
                
        except Exception as e :
            print(e)
            
            
    def test_totaltags(self):
      
        try:
           
           
            #tags_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"(//div[@class="tags"]/a[text()='life'])[1]")))
            total_tags = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div/a[@class="tag"]')))
            tags = len(total_tags)
            self.assertGreater(tags,5,"Error not found")
            
            
           
                
        except Exception as e :
            print(e)
            
            
            
    
            
    
            
            
    
                 
    
if __name__ == "__main__":
    unittest.main()