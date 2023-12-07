import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Capitalize variable names for consistency
Driver = selenium.webdriver.Chrome
Options = webdriver.ChromeOptions

# Define function to execute single iteration
def single_iteration():

    # Use Service object with path to chromedriver
    driver_path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
    service = Service(driver_path)

    # Create Driver instance with service and options
    driver = Driver(service=service)

    # Open SurveyMonkey URL
    url = "https://pt.surveymonkey.com/r/WXWTMDF"
    driver.get(url)

    # Wait 30 seconds for elements to load
    driver.implicitly_wait(30)

    # Click on the first radio button option
    driver.find_element(By.XPATH, '//*[@id="165536466_1209052673_label"]/span[1]').click()

    # Wait 30 seconds for page to update
    driver.implicitly_wait(30)

    # Click on the submit button
    driver.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()

    # Close the driver after each iteration
    driver.quit()

# Loop 100 times and execute the iteration
for _ in range(50):
    single_iteration()


# Print completion message
print("All 50 iterations completed!")

# Obtenha uma lista de todas as janelas abertas
#window_handles = driver.window_handles

# Especifique que o Selenium não deve fechar nenhuma janela
#driver.set_window_handles_before_close([])