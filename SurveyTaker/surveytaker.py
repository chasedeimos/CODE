from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException as EniError
from selenium.common.exceptions import ElementClickInterceptedException as EciError
from time import sleep

link = 'https://www.wenjuan.com/s/UZBZJvQVAG/?sr=wenjuan_mini_app&sy=1'
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 15)
driver.get(link)

positive = [
                'option_602662933631f25418ec958e',
                'option_602662a23631f2596dfa5164',
                'option_602665463631f25369c32287',
                'option_602664d292beb56d634d94d7',
                'option_6026647d3631f255231db4dd',
                'option_602665c892beb56d9918bf65',
                'option_602666c492beb56dca39cb28',
                'option_602666fd92beb56dca39cb2b',
                'option_602667863631f25336cc509a',
                'option_6026684c92beb56bbb224ad7',
                'option_6026689a92beb56e69ab89cf',
                'option_602668d83631f252fde2bcd0',
                'option_6026690e92beb56ca9e3ad7b',
                'option_6026694e3631f258e4c682b4'
        ]

neutral = [
                'option_602662933631f25418ec958d',
                'option_602662a23631f2596dfa5165',
                'option_602665463631f25369c32286',
                'option_602664d292beb56d634d94d7',
                'option_6026647d3631f255231db4dd',
                'option_602665c892beb56d9918bf66',
                'option_602666c492beb56dca39cb29',
                'option_602666fd92beb56dca39cb2c',
                'option_602667863631f25336cc509b',
                'option_6026684c92beb56bbb224ad8',
                'option_6026689a92beb56e69ab89d0',
                'option_602668d83631f252fde2bcd1',
                'option_6026690e92beb56ca9e3ad7c',
                'option_6026694e3631f258e4c682b5'
    ]

negative = [
                'option_602662933631f25418ec958e',
                'option_602662a23631f2596dfa5166',
                'option_602665463631f25369c32285',
                'option_602664d292beb56d634d94d7',
                'option_6026647d3631f255231db4dc',
                'option_602665c892beb56d9918bf67',
                'option_602666c492beb56dca39cb28',
                'option_602666fd92beb56dca39cb2b',
                'option_602667863631f25336cc509c',
                'option_6026684c92beb56bbb224ad9',
                'option_6026689a92beb56e69ab89d1',
                'option_602668d83631f252fde2bcd2',
                'option_6026690e92beb56ca9e3ad7d',
                'option_6026694e3631f258e4c682b6'
    ]

def takeSurvey(answers, times_left):
    for answer in answers:
        # Locate the option's label element
        option = wait.until(EC.presence_of_element_located((By.XPATH, '//label[@for="{}"]'.format(answer))))
        # Find and click its child checkbox
        checkbox = option.find_element_by_xpath('.//span')
        try:
            checkbox.click()
        except EniError:
            # Scroll down 100px to always reach the next question
            driver.execute_script('window.scrollTo(0, 100)')
            checkbox.click()
        except EciError:
            resume = driver.find_element_by_xpath('//div[class="btn-default continue-answer"]')
            resume.click()
            sleep(10)
            checkbox.click()
            
    # Locate and click the submit button
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    submit = wait.until(EC.element_to_be_clickable((By.ID, 'next_button')))
    submit.click()
    sleep(5) # wait for the answers to be submitted
    times_left -= 1
    
    # Print the result of the cycle
    global times
    print('{0}/{1} Survey(s) Submitted.'.format(times - times_left, times))

        
    # Take the questionnaire again if needed
    if times_left >= 1:
        # Refresh the page and restart the survey
        for attempt in range(0,3):
            try:
                driver.refresh()
                break
            except TimeoutError:
                continue  
        restart = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'restart-survey'))) # load the restart button
        restart.click()
        takeSurvey(answers, times_left)
    else:
        print('SurveyTaker\'s program complete.')
        driver.quit()
        return

if __name__ == '__main__':
    answers = input('What answers to use in the survey (positive/neutral/negative): ')
    exec('answers = {}'.format(answers))
    times = int(input('How many times to take the survey: '))
    takeSurvey(answers, times)
