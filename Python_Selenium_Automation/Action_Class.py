from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep as wait

# Set up WebDriver for Edge
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# Open the website
url = "https://demoqa.com/"
driver.get(url)
driver.maximize_window()

wait(5)

alert_element = driver.find_element(By.XPATH,"//div[text()='Alerts, Frame & Windows']")

