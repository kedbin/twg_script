from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
url = 'https://www.thewrestlinggame.com/wg/frame.asp'
d = {}
for i in range(0, 16):
    key = i
    value = f'Current energy: {i}<'
    d[key] = value


def update_time(time=''):
    sleep(3)
    time = driver.find_element_by_xpath('.//*[@id="timer_stat"]').text
    return time


def battle_timer(btime=''):
    btime = str(driver.find_element_by_xpath(
        '//*[@id="topenergy"]').get_attribute('title'))
    print('Counting energy...')
    return btime


def event_clicker(time, btime, name):
    print(f'Your stat timer is at {time}')
    energy = 0
    if time == 'Train':
        try:
            sleep(3)
            driver.find_element_by_xpath('//*[@id="timer_stat"]/a').click()
            sleep(5)
            driver.find_element_by_xpath('//*[@id="pro4"]/a').click()
            print("You have trained a stat !")
        except:
            print('something went wrong, hold on a moment')
            sleep(3)
    else:
        e =[i for i, timer in d.items() if timer in btime]
        energy = e[0]
        print(energy)
        if energy >= 3 :
            try:
                driver.find_element_by_xpath('/html/body/div[2]/section[2]/nav/ul/li[1]/a').click()
                sleep(5)
                driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[1]').click()
                sleep(7)
                listings = driver.find_elements_by_xpath('//*[@class="listing"]')
                for listing in listings:
                    if name.upper() in listing.text:
                        x = listing
                        print('FOUND YOU!!!!')
                    else:
                        print('NOT THIS ONE')
                x.find_element_by_tag_name('a').click()
                print(f'You are fighting {name} for event points')
                sleep(2)
            except:
                print('this was an error on fighting')
                driver.refresh()
                sleep(10)
        else:
            try:
                print('You have not enough Energy... resting for 15 mins')
                sleep(9)
                print('alright 15 mins done. returning.')
            except:
                print('yatta')


'''
# removing this function as it is uneeded rn
def check_training(time,name,btime):
    print(f'Your timer is at {time}')
    if time == 'Train':
        try:
            sleep(3)
            driver.find_element_by_xpath('//*[@id="timer_stat"]/a').click()
            sleep(3)
            driver.find_element_by_xpath('//*[@id="pro4"]/a').click()
            print("You have trained a stat !")
        except:
            print('something went wrong, hold on a moment')
            sleep(3)
    else:
        if 'Current energy: 0' not in btime:
            try:
                print(f'Finding {name} and starting a fight \n')
                driver.find_element_by_xpath('//*[@id="arena"]/a').click()
                sleep(4)
                driver.find_element_by_xpath('//*[@id="matchsearch"]/div/p[2]/label').click()
                sleep(2)
                driver.find_element_by_xpath('//*[@id="wre_output"]/div/ul/li[5]').click()
                print('Fight initiated, now waiting for a minute... will check if training is available')
                sleep(60)
            except:
                sleep(2)
                print('Error occured, retrying')
                driver.refresh()
                sleep(60)
        else:
            try:
                print('You have no more Energy... resting for 15 mins')
                sleep(900)
                print('alright 15 mins done. returning.')
            except:
                print('yatta')
'''


def launch():
    username = "twgbot123@gmail.com"
    password = "twgbot123!!!"

    driver.get(url)
    driver.find_element_by_xpath('//*[@id="td_login"]').click()
    driver.find_element_by_xpath('//*[@id="login_mail"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="login_pass"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="login_button"]').click()
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="contentcnt"]/section[2]/div[4]/ul/li[2]/a').click()
    driver.switch_to.window(driver.window_handles[-1])


def close_window():
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])


iteration = 0
launch()
name = input('Input the wrestler name you want to fight for the event : \t ')
while 1:
    print(f'\t This is loop number {iteration}')
    iteration += 1
    timez = update_time()
    battle = battle_timer()
    event_clicker(timez, battle, name)
    if iteration == 100:
        print('reached max amount of loops, restarting browser...')
        close_window()
        iteration = 0
        launch()
'''
/html/body/div[2]/div/div/div[2]/div/div/div[6]/div[3]

/html/body/div[2]/div/div/div[2]/div/div[1]
//*[@class="listing"]
/html/body/div[2]/div/div/div[2]/div/div/div[6]/div[5]/div[2]/h4

# Get the common element, in this case div class = listing
# filter through the divs with the same stuff, then /html/body/div[2]/div/div/div[2]/div/div/div[6]/div[3]
'''
