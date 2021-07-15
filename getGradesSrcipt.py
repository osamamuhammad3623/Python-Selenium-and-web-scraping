from selenium import webdriver
import time

########
id = '0000000'
myPassword = 'AAA'
coursesCodes = ['CSE211', 'EPM213', 'ECE252', 'PHM122s', 'ECE212', 'CSE231']
########

driver_path = '/home/osamamuhammad/Documents/chromedriver'
driver = webdriver.Chrome(driver_path)

driver.get("https://eng.asu.edu.eg/login")
driver.maximize_window()

email_field = driver.find_element_by_id("email")

id +='@eng.asu.edu.eg'
email_field.send_keys(id)

pass_field = driver.find_element_by_name("password")
pass_field.send_keys(myPassword)

driver.find_element_by_tag_name("button").click()

time.sleep(2)
driver.get("https://eng.asu.edu.eg/dashboard/my_courses")

for courseCode in coursesCodes:
    course_link = driver.find_element_by_partial_link_text(courseCode)
    screenshot_name = courseCode + '.png'
    try:
        course_link.click()
        time.sleep(1)
        driver.save_screenshot(screenshot_name)
        driver.back()
    except:
        driver.execute_script("window.scrollTo(0, 1000)")
        course_link.click()
        time.sleep(1)
        driver.save_screenshot(screenshot_name)
        driver.back()

driver.close()