from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tracking


class instagram_bot:

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com/'
        self.driver = webdriver.Chrome('chromedriver.exe')

        self.login()

    def login(self):

        self.driver.get('{}accounts/login/'.format(self.base_url))

        time.sleep(.5)

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)

        time.sleep(.5)

        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()

        time.sleep(3)

        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        except:
            pass

    def nav_user(self, user):

        self.driver.get('{}{}'.format(self.base_url, user))

    def follow_user(self, user):

        self.nav_user(user)

        try:
            follow_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
            follow_button.click()
            tracking.followadd(user)
        except:
            pass

    def unfollow_user(self, user):

        self.nav_user(user)
        time.sleep(.5)

        try:
            unfollow_closed = self.driver.find_element_by_xpath("//button[contains(text(), 'Requested')]")
            unfollow_closed.click()
        except:
            pass

        try:
            unfollow_open = self.driver.find_elements_by_xpath("//button")
            unfollow_open[1].click()
        except:
           pass

        time.sleep(1)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
            tracking.followremove(user)
        except:
            pass

    def hashtag_search(self, hashtag):

        self.driver.get("{}{}{}".format(self.base_url, "explore/tags/", hashtag))

        # Redundant Method Keeping in case of breaks (and because it looks cool)

        # search = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        # search.send_keys(hashtag)
        # time.sleep(1)
        # search.send_keys(Keys.ENTER)
        # time.sleep(1)
        # search.send_keys(Keys.ENTER)
        # time.sleep(2)

    def secondary_find_first_post_from_search(self):

        link_array = self.driver.find_elements_by_xpath("//a")
        first_hashtag_post = link_array[10].find_elements_by_xpath(".//*")
        first_hashtag_post[3].click()
        time.sleep(1.5)

    def hashnav(self):

        self.secondary_find_first_post_from_search()

        self.follow_under_150()
        time.sleep(2)
        next_post_button = self.driver.find_element_by_xpath("//a[contains(text(), 'Next')]")

        next_post_button.click()
        self.follow_under_150()
        time.sleep(2)
        # self.hashnav_follow()

        next_post_button.click()
        self.follow_under_150()
        time.sleep(2)

    def next_post(self):

        next_post_button = self.driver.find_element_by_xpath("//a[contains(text(), 'Next')]")

        next_post_button.click()
        time.sleep(1.5)

    def hashnav_follow(self):

        # finding anchors
        header_elements = self.driver.find_elements_by_xpath("//header")
        all_children_of_header = header_elements[1].find_elements_by_xpath(".//a")
        link_to_username = all_children_of_header[0].get_attribute('href')

        # storing username
        username_link_array = str(link_to_username).split("/")
        username = username_link_array[3]

        # finding follow button and clicking it
        follow_button_anchor = header_elements[1].find_elements_by_xpath(".//button")
        follow_button_anchor[0].click()
        tracking.followadd(username)

        # Unfollow users immediately for testing purposes
        # time.sleep(5)
        # follow_button_anchor[0].click()
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
        # tracking.followremove(username)

    def check_likes(self):

        # loading anchors
        like_amount_finder = self.driver.find_elements_by_xpath("//button")
        likes = ""
        counter1 = 0
        for a in like_amount_finder:

            # prints are for testing purposes to find the correct button anchor containing the like amount for the post
            print(a.text + str(counter1))
            print()
            print("-----")
            counter1 += 1
        counter = 7
        while likes == "":

            like_count = like_amount_finder[counter].text

            for char in like_count:
                if char.isnumeric():
                    likes += char
                    # print is exclusively for debugging to see looping as it happens in console
                    print(likes + " first loop")
                else:
                    pass
            # print also for debugging
            print(likes + " While loop " + str(counter))
            counter += 1
        #if int(likes) < 150:
        #    return True
        #else:
        #    return False

    def follow_under_150(self):
        if self.check_likes():
            self.hashnav_follow()

    def mass_unfollow(self):
        remove_list = tracking.checkAge()
        for user in remove_list:
            self.unfollow_user(user)


if __name__ == "__main__":
    # initialization of bot instance
    ig_bot = instagram_bot("username goes here", "password goes here")

    # individual function testing, flow control yet to be implemented
    ig_bot.hashtag_search("goodeats")
    ig_bot.secondary_find_first_post_from_search()
    ig_bot.check_likes()
    ig_bot.next_post()
    ig_bot.check_likes()
    ig_bot.next_post()
    ig_bot.check_likes()
    ig_bot.next_post()
    ig_bot.check_likes()
    ig_bot.next_post()
    ig_bot.next_post()
    ig_bot.next_post()
    ig_bot.next_post()
    ig_bot.check_likes()

    time.sleep(15)
    ig_bot.driver.quit()







