from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class Test(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://quotes.toscrape.com/')

    def tearDown(self):
        self.driver.quit()
        
        
        
    def test_title(self):
        
        try:
           
            title_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1/a')))
            actual_name = title_name.text
            expected_name = "Quotes to Scrape"
            
            self.assertEqual(actual_name,expected_name,'Title Not Equal')
            
            
        except Exception as e :
            print(e)
        
        
    def test_top10tags(self):
      
        try:
           
            tags_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span/a[@class="tag"])[1]'))).click()

            author_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//small[@class="author"])[1]')))
            print(author_name.text)
            
            actual_name = author_name.text
            expected_name = "André Gide"
            
            self.assertEqual(actual_name,expected_name,'Name Not Equal')
            
            
            
          
                
        except Exception as e :
            print(e)
            
            
    def test_totalauthor(self):
      
        try:
           
            get_all_author = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '(//small[@class="author"])')))
            count_author = len(get_all_author)
            print(f'Total number of author : {count_author}')
            
            self.assertGreaterEqual(count_author,10,'There are less author')
            
        except Exception as e :
            print(e)
            
            
    def test_aboutsection(self):
      
        try:
           
            about_section = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//span/a)[1]'))).click()
            title_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h3')))
            actual_title = title_name.text
            expected_title = "André Gide"
            
            self.assertNotEqual(actual_title,expected_title,'Name Not Equal')
            
        except Exception as e :
            print(e)
            
            
            
    def test_display_authorname(self):
        
        
        try:
            while True:
          
                authors = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//small[@class]')))

                for author in authors:
                     self.assertTrue(author.is_displayed(), f"Author {author.text} is not visible")
                     print(f'Author: {author.text} is visible')


            
                try:
                    next_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Next")]')))
                    next_btn.click()
                
                except Exception as e:
                    print("No more pages")
                    break

        except Exception as e:
            print(f"Error: {e}")
            
    
    def test_count_authorname(self):
        
        
        total_sum = 0
        try:
            while True:
          
                authors = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//small[@class]')))
                
                
                total = len(authors)
                total_sum =total_sum + total 
              
                
                
                
                #for author in authors:
                     #self.assertTrue(author.is_displayed(), f"Author {author.text} is not visible")
                     #print(f'Author: {author.text} is visible')
                     
                     


            
                try:
                    next_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Next")]')))
                    next_btn.click()
                
                except Exception as e:
                    print("No more pages")
                    break
                
            print(f'The sum of all author: {total_sum}')
            actual_author = total_sum
         
             
            
            self.assertGreater(actual_author,14,'Error')
            

        except Exception as e:
            print(f"Error: {e}")
            
        
    def test_count_quotes(self):
        
        
        total_sum = 0
        try:
            while True:
          
                get_allquotes = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="text"]')))
                
                
                total = len(get_allquotes)
                total_sum =total_sum + total 
                
                try:
                    next_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Next")]')))
                    next_btn.click()
                
                except Exception as e:
                    print("No more pages")
                    break
                
            print(f'The sum of all total quotes: {total_sum}')
            actual_quotes = total_sum
            self.assertGreater(actual_quotes,14,'Error')
            

        except Exception as e:
            print(f"Error: {e}")
            
            
    def test_count_tags(self):
        
        
        total_sum = 0
        try:
            while True:
          
                get_alltags = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="tag"]')))
                
                
                total = len(get_alltags)
                total_sum =total_sum + total 
                
                try:
                    next_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Next")]')))
                    next_btn.click()
                
                except Exception as e:
                    print("No more pages")
                    break
                
            print(f'The sum of all total tags: {total_sum}')
            
            actual_tags = total_sum
            excepected_tags = 140
            self.assertNotEqual(actual_tags,excepected_tags,'{actual_tags} is not equal to the {excepected_tags} ')        

        except Exception as e:
            print(f"Error: {e}")
            

            

if __name__ == "__main__":
  
    unittest.main(defaultTest="Test.test_count_tags")
    
    
