from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# user prompting
browser = input("Select a browser(firefox, chrome, or edge): ")
engine = input("Select a search engine(google, bing, or duckduckgo): ")

# Set up the web driver for the selected browser
if browser.lower() == 'chrome':
    driver = webdriver.Chrome()
elif browser.lower() == 'firefox':
    driver = webdriver.Firefox()
elif browser.lower() == 'edge':
    driver = webdriver.Edge()
else:
    print(f"{browser} is not a supported browser. Please choose from Chrome, Firefox, or Bing.")
    exit()
theengine = f"http://www.{engine}.com/"

# Navigate to the search page
driver.get(theengine)

# Perform the search and record the time
start_time = time.time()
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("statistics")
search_box.submit()
end_time = time.time()

# Calculate the time it took to load the page
load_time = end_time - start_time
print("Page load time: %.2f seconds" % load_time)

# Write the data to a csv file
with open('search_times.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([browser, engine, load_time])

# Close the web driver
driver.quit()
