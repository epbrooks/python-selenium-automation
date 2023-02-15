#Amazon logo
driver.find_element(By.ID, 'nav-bb-logo')

#Email field
driver.find_element(By.XPATH, "//input[@type='email']")

#Continue button
driver.find_element(By.ID, 'continue')

#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

#Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-sign-issues-link')

#Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

#*Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

#*Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")







