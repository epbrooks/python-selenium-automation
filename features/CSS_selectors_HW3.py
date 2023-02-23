#Amazon Header
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

#Create Account Header
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')


#Your name text field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')


#Email text field
driver.find_element(By.CSS_SELECTOR, '#ap_email')


#Password text field
driver.find_element(By.CSS_SELECTOR, "input[name='password']")


#Passwords must be at least 6 chatacters.
driver.find_element(By.CSS_SELECTOR, 'div.a-alert-content')


#Re-enter password
driver.find_element(By.CSS_SELECTOR, "input[name='passwordCheck']")


#Create your Amazon account(Continue)
driver.find_element(By.CSS_SELECTOR, '#input#continue')


#Conditions of Use
driver.find_element(By.CSS_SELECTOR, "a[#legalTextRow href*='condition_of_use']"


#Privacy Notice
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='privacy_notice']")


#Sign In
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='/ap/signin?']")