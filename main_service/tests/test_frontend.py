from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_chatbot():
    driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and accessible
    driver.get("http://localhost:5000")  # Adjust URL if necessary

    # Find the input field and type a message
    message_input = driver.find_element(By.ID, "user-message")
    message_input.send_keys("Hi")
    
    # Simulate pressing Enter (Send button press)
    message_input.send_keys(Keys.RETURN)  # This automatically sends the message

    # Wait for the bot response to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bot-message"))
    )

    # Check the response from the chatbot
    bot_response = driver.find_element(By.CLASS_NAME, "bot-message")
    assert bot_response.text in ["Hello!", "Hi there!", "Greetings! How can I assist you today?"]

    driver.quit()
