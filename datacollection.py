from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

def speed_test(browser, engine):
    # Set up the web driver for the selected browser
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser.lower() == 'edge':
        driver = webdriver.Edge()
    else:
        print(f"{browser} is not a supported browser. Please choose from Chrome, Firefox, or Edge.")
        return

    # Construct the search engine URL
    the_engine = f"http://www.{engine}.com/"

    # Navigate to the search page
    driver.get(the_engine)

    # Perform the search and record the time
    start_time = time.time()
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys("statistics")
    search_box.submit()
    end_time = time.time()

    # Calculate the time it took to load the page
    load_time = end_time - start_time
    print(f"Page load time for {browser} and {engine}: {load_time:.2f} seconds")

    # Write the data to a csv file
    with open('search_times.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([browser, engine, load_time])

    # Close the web driver
    driver.quit()

# Read browser and search engine pairs from the CSV file
with open('order.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row if present
    for row in reader:
        browser, engine = row
        speed_test(browser, engine)

