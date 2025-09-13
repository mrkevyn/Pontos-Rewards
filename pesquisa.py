from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import time

# Caminho para o WebDriver
EDGE_DRIVER_PATH = r"C:\Users\Kevyn\Documents\msedgedriver.exe"

# Lista de termos de pesquisa
search_terms = [
    "History of ancient civilizations",
    "How to bake sourdough bread",
    "Most effective workout routines",
    "Basics of astrophotography",
    "How to learn a new language fast",
    "Famous philosophers and their ideas",
    "Introduction to birdwatching",
    "Interior design tips for small spaces",
    "How to play the ukulele",
    "Deep sea creatures documentary",
    "Tips for successful public speaking",
    "How to build a treehouse",
    "Understanding wine tasting",
    "Popular hiking trails in South America",
    "Basics of stock market trading",
    "DIY home automation projects",
    "Introduction to digital painting",
    "How to train your dog at home",
    "Famous historical battles explained",
    "Mindful parenting techniques",
    "What is minimalism lifestyle",
    "Best board games for families",
    "How to plan a road trip",
    "Difference between teas and herbal infusions",
    "Photography lighting setups for beginners",
    "How to compost at home",
    "Beginner’s guide to pottery",
    "Street food cultures around the world",
    "How to build a personal brand",
    "Hidden gems in European travel",
]

def search_bing_with_edge(search_terms):
    """Realiza pesquisas no Bing usando o navegador Microsoft Edge."""
    service = Service(EDGE_DRIVER_PATH)
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Edge(service=service, options=options)
    
    try:
        driver.get("https://www.bing.com")
        
        for term in search_terms:
            search_box = driver.find_element(By.NAME, "q")
            search_box.clear()
            search_box.send_keys(term)
            search_box.send_keys(Keys.RETURN)
            
            print(f"Realizada a pesquisa: {term}")
            time.sleep(60)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    search_bing_with_edge(search_terms)
