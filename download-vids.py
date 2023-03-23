from selenium import webdriver
from selenium.webdriver.common.by import By
from pytube import YouTube
import time


lists = [
    ['History' , 'https://www.youtube.com/watch?v=Yocja_N5s1I&list=PLBDA2E52FB1EF80C9'],
    ['Art' , 'https://www.youtube.com/watch?v=mzzvCGfKZR8&list=PLhnHFsOn0cgdjNrlX4qeytqAUIhRqKbAI'],
    ['Physics' , 'https://www.youtube.com/watch?v=ihNZlp7iUHE&list=PLAD5B880806EBE0A4'],
    ['Chemistry','https://www.youtube.com/watch?v=ZuWa827qAao&list=PLybg94GvOJ9EbbO2RXPWTUNIIE0C7hSfm'],
    ['Biology','https://www.youtube.com/watch?v=3w1fY67dnFI&list=PL6gx4Cwl9DGAdmjrf1RaZIJe2_3fGbhbu'],
    ['Astrology','https://www.youtube.com/watch?v=0rHUDWjR5gg&list=PL8dPuuaLjXtPAJr1ysd5yGIyiSFuh0mIL'],
    ['Literature','https://www.youtube.com/watch?v=LAzKGkTIKpg&list=PLwxNMb28Xmpfv2COuuJaKzy6E2n8nSMdi'],
    ['Philosophy','https://www.youtube.com/watch?v=1A_CAkYt3GY&list=PLUHoo4L8qXthO958RfdrAL8XAHvk5xuu9'],
    ['Politics','https://www.youtube.com/watch?v=lrk4oY7UxpQ&list=PL8dPuuaLjXtOfse2ncvffeelTrqvhrz8H'],
    ['Economics','https://www.youtube.com/watch?v=wCHm5SdNO5U&list=PLSQl0a2vh4HDERCw_ddanXbsDpFWcpL-S'],
    ['Psychology','https://www.youtube.com/watch?v=vo4pMVb0R6M&list=PLGMVCsud2sqX1F5BkUp7yiIFcGtFjb1hZ'],
    ['Sociology','https://www.youtube.com/watch?v=ylXVn-wh9eQ&list=PLH2l6uzC4UEX9UzR1bVkK128tLSlzGkt0']
]

driver = webdriver.Edge()
for l in lists:
    driver.get(l[1])
    time.sleep(5)
    vid_links_container = driver.find_element(By.XPATH,'//div[contains(@class,"playlist-items style-scope ytd-playlist-panel-renderer") and contains(@id, "items")]')
    links = vid_links_container.find_elements(By.XPATH,'//a[@id="wc-endpoint"]')
    for link in links:
        print(link.get_attribute('href'))
        yt = link.get_attribute('href')
        vid = YouTube(yt)
        print(vid.streams.filter(only_audio=True).first().download(output_path=f'{l[0]}'))
    
    




    