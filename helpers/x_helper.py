import random

from uiautomator2 import Device

from models.device import DevicePhone
from time import sleep
import time

import openai

COUNT_CHECK_BUTTON_REACTION_POST = 20

openai.api_key = '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'


def generate_reply_chatgpt(question):
    reply = "No comment"
    try:
        messages = [{"role": "system", "content": "You are a intelligent assistant."},
                    {"role": "user", "content": question}]
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, timeout=5
        )

        reply = chat.choices[0].message.content
    except:
        pass
    return reply


class XHelper:
    TIME_OUT_LOGIN = 90

    def __init__(self, d: Device, device: DevicePhone, data, send_last_status_func):
        self.d = d
        self.device = device
        self.data = data
        self.send_last_status_func = send_last_status_func

    def change_proxy(self):
        try:
            self.d.app_stop("com.scheler.superproxy")
            self.d.app_clear("com.scheler.superproxy")
            ip = self.device.proxy.split(":")[0]
            port = self.device.proxy.split(":")[1]
            try:
                user = self.device.proxy.split(":")[2]
                password = self.device.proxy.split(":")[3]
            except:
                user = password = None
            self.d.app_start("com.scheler.superproxy")
            is_fill = False
            for count in range(30):
                if count == 10:
                    print("cant change proxy")
                    return False
                elif self.d(description="Super Proxy").exists():
                    self.d.xpath('//android.widget.Button').click()
                elif self.d(description="Start").exists():
                    self.d(description="Start").click()
                    sleep(2)
                elif (self.d(text="New Profile").exists() or self.d(description="SOCKS5").exists()) and not is_fill:
                    self.d.xpath('//android.widget.EditText[3]').click()
                    self.d.send_keys(ip, clear=True)
                    self.d.xpath('//android.widget.EditText[4]').click()
                    self.d.send_keys(port, clear=True)
                    if user:
                        self.d.xpath('//android.widget.EditText[5]').click()
                        self.d.send_keys(user, clear=True)
                        self.d.xpath('//android.widget.EditText[6]').click()
                        self.d.send_keys(password, clear=True)
                    sleep(1)
                    self.d.xpath("//android.widget.Button[2]").click()
                    is_fill = True
                elif self.d(description="Stop").exists():
                    return True
                elif self.d(text="Connection request").exists():
                    self.d(resourceId="android:id/button1").click()
                sleep(1)
                count += 1
            return False
        except:
            return False

    def login_x(self):
        self.d.app_stop("com.twitter.android")
        self.d.app_start("com.twitter.android")
        count = 0
        while count < self.TIME_OUT_LOGIN:
            if self.d(resourceId="android:id/button2").exists():
                self.d(resourceId="android:id/button2").click()

            if self.d(description="Show navigation drawer").exists():
                self.d(description="Show navigation drawer").click()

            if self.d(text="Log in").exists():
                self.d(text="Log in").click()

            if self.d(text="Log in or sign up").exists():
                self.d(text="Log in or sign up").click()

            if self.d(text="Have an account already? Log in").exists():
                bounds = self.d(text="Have an account already? Log in").info['bounds']
                self.d.click(bounds['right'] - 50, bounds['top'] + 50)

            if self.d(resourceId="com.twitter.android:id/text_field").exists():
                self.d(resourceId="com.twitter.android:id/text_field").click()
                self.d.send_keys(self.device.user_name, clear=True)
                sleep(1.5)
                self.d(text="Next").click()
            if self.d(resourceId="com.twitter.android:id/password_field").exists():
                self.d(resourceId="com.twitter.android:id/password_field").click()
                self.d.send_keys(self.device.password, clear=True)
                sleep(3)
                self.d(text="Log in").click()

            if self.d(text="Profile").exists():
                return True

            if self.d(text="For you").exists():
                return True
            sleep(1)
            count += 1

        return False

    def like_post(self):
        count = 0
        while count < COUNT_CHECK_BUTTON_REACTION_POST:
            if self.d(resourceId="com.twitter.android:id/inline_like").exists():
                self.d(resourceId="com.twitter.android:id/inline_like").click()
                return True
            self.d.swipe(0.524, 0.846, 0.507, 0.519, 0.2)
            sleep(0.5)
            count += 1
        return False

    def comment_post(self, content_post):
        count = 0
        while count < COUNT_CHECK_BUTTON_REACTION_POST:
            if self.d(resourceId="com.twitter.android:id/inline_reply").exists():
                self.d(resourceId="com.twitter.android:id/inline_reply").click()
                self.d(resourceId="com.twitter.android:id/tweet_text").click(timeout=10)
                reply = generate_reply_chatgpt(f'generate comment from this post: "{content_post}" with 150 characters')
                self.d.send_keys(reply, clear=True)
                self.d.xpath(
                    '//*[@resource-id="com.twitter.android:id/composer_toolbar"]/android.widget.LinearLayout[1]').click()
                sleep(3)
                return True
            self.d.swipe(0.524, 0.846, 0.507, 0.519, 0.2)
            sleep(0.5)
            count += 1
        return False

    def retweet_post(self):
        count = 0
        while count < COUNT_CHECK_BUTTON_REACTION_POST:
            if self.d(resourceId="com.twitter.android:id/inline_retweet").exists():
                self.d(resourceId="com.twitter.android:id/inline_retweet").click()
                sleep(1.5)
                self.d.xpath(
                    '//*[@resource-id="com.twitter.android:id/action_sheet_recycler_view"]/android.view.ViewGroup[1]').click()
                sleep(2)
                return True
            self.d.swipe(0.524, 0.846, 0.507, 0.519, 0.2)
            sleep(0.5)
            count += 1
        return False

    def check_specify_ads_post(self):
        is_ads_show = False
        username = ''

        # Kiem tra ads va username chi dinh co tren man hinh khong
        for username_feed in self.data['list_username_new_feed']:
            if self.d.xpath(f"//*[contains(@content-desc, '@{username_feed}')]").exists and self.d(
                    resourceId="com.twitter.android:id/tweet_ad_badge_top_right", text="Ad").exists():
                is_ads_show = True
                username = username_feed
        if not is_ads_show or not username:
            return False

        # Kiem tra ads va username co nam canh nhau khong
        position_top_ads = int(
            self.d(resourceId="com.twitter.android:id/tweet_ad_badge_top_right", text="Ad").info.get("bounds").get(
                "top"))
        position_top_username = int(
            self.d.xpath(f"//*[contains(@content-desc, '@{username}')]").info.get("bounds").get("top"))
        if abs(position_top_username - position_top_ads) > 50:
            return False

        self.send_last_status_func(f"Click bài ads {username}")
        self.d(resourceId="com.twitter.android:id/tweet_ad_badge_top_right", text="Ad").click()
        self.d(text="Post").wait(15)

        content_post = self.d(resourceId="com.twitter.android:id/tweet_content_view_stub").info['text']
        sleep(2)
        if self.d(resourceId="com.twitter.android:id/title").exists():
            self.d(resourceId="com.twitter.android:id/title").click()
            sleep(10)

        if self.d.app_current().get("package") != "com.twitter.android":
            self.d.press("back")

        self.like_post()
        self.comment_post(content_post)
        return True

    def click_post_detail(self):
        count = 0
        while count < 10:
            if self.d.xpath(f"//*[contains(@content-desc, 'repost')]").exists:
                pos = self.d.xpath(f"//*[contains(@content-desc, 'repost')]").info.get('bounds')
                self.d.click(pos.get('left'), pos.get('bottom'))
            if self.d(text="Post").exists():
                return True

            count += 1
            sleep(1)
        return False

    def swipe_new_feed(self, total_runtime=300, is_random_like=True, is_random_comment=True,
                       is_random_retweet=True, is_click_specify_ads=True):

        start_time = time.time()  # Thời điểm bắt đầu chạy
        self.d.shell('am start -a android.intent.action.VIEW -d "https://twitter.com/" com.twitter.android')
        self.d(resourceId="com.twitter.android:id/channels").click(timeout=10)
        time.sleep(5)

        while time.time() - start_time < total_runtime:
            content_post = "Nice day"
            is_click_ads = False
            if is_click_specify_ads:
                is_click_ads = self.check_specify_ads_post()

            if random.randint(0, 30) == 2 and is_random_comment and not is_click_ads:
                if not self.d(text="Post").exists():
                    self.send_last_status_func("Bình luận bài viết")
                    if not self.click_post_detail():
                        continue
                    if not self.d(resourceId="com.twitter.android:id/tweet_content_view_stub").exists():
                        continue
                    content_post = self.d(resourceId="com.twitter.android:id/tweet_content_view_stub").info['text']
                    sleep(random.randint(5, 10))
                self.comment_post(content_post)

            if random.randint(0, 20) == 2 and is_random_like and not is_click_ads:
                if not self.d(text="Post").exists():
                    self.send_last_status_func("Like bài viết")
                    if not self.click_post_detail():
                        continue
                    sleep(random.randint(5, 10))
                self.like_post()

            if random.randint(0, 40) == 2 and is_random_retweet and not is_click_ads:
                if not self.d(text="Post").exists():
                    self.send_last_status_func("Retweet bài viết")
                    if not self.click_post_detail():
                        continue
                    sleep(random.randint(5, 10))
                self.retweet_post()

            if self.d(text="Post").exists():
                self.d.press("back")
                sleep(2)
            if not self.d.xpath(f"//*[contains(@content-desc, 'repost')]").exists:
                self.d.press("back")
                sleep(2)
            self.d.swipe(0.524, 0.846, 0.539, 0.241, random.randint(2, 3) * 0.1)
            sleep(random.randint(1, 4) * 0.5)

    def find_uid(self, uid):
        self.d.app_stop('com.twitter.android')
        link = 'https://twitter.com/'
        self.d.shell('am start -a android.intent.action.VIEW -d "' + link + '" com.twitter.android')
        sleep(2)
        link = 'https://twitter.com/' + uid
        self.d.shell('am start -a android.intent.action.VIEW -d "' + link + '" com.twitter.android')

    def swipe_wall(self, uid, total_runtime=60, view_ads=True):
        self.find_uid(uid)
        count_check = 0
        start_time = time.time()
        while time.time() - start_time < total_runtime:
            try:
                if self.d(text="Follow").exists() or self.d(text="FOLLOW").exists():
                    self.d(text="Follow").click_exists()
                    self.d(text="FOLLOW").click_exists()

                if self.d.info['currentPackageName'] != 'com.twitter.android':
                    self.find_uid(uid)

                if self.d(resourceId="com.twitter.android:id/profile_protected_title").exists():
                    return True

                if not self.d(text="Posts").exists():
                    self.d.press("back")
                    sleep(1)
                    self.d.swipe(0.5, 0.8, 0.5, 0.2, 0.1)
                    continue

                if self.d(resourceId="com.twitter.android:id/tweet_profile_image_container").exists():
                    if self.d(resourceId="com.twitter.android:id/tweet_ad_badge_top_right").exists() and view_ads:
                        # Bắt cáo

                        # d(resourceId="com.twitter.android:id/tweet_ad_badge_top_right").click()
                        self.d(resourceId="com.twitter.android:id/tweet_ad_badge_top_right").wait(10)
                        x, y = self.d(resourceId="com.twitter.android:id/tweet_ad_badge_top_right").center()
                        self.d.click(x - 200, y)
                        for i in range(10):
                            if self.d(resourceId="com.twitter.android:id/inline_like").exists():
                                break
                            self.d.swipe_ext("up", scale=1)
                        self.d(resourceId="com.twitter.android:id/subtitle").click(timeout=10)
                        sleep(20)
                        self.d.press("back")
                        continue

                    # View post
                    x, y = self.d(resourceId="com.twitter.android:id/tweet_profile_image_container").center()
                    self.d.click(x, y + 200)
                    try:
                        content = self.d(resourceId="com.twitter.android:id/tweet_content_view_stub").get_text()
                    except:
                        content = 'Hello!'

                    for i in range(10):
                        if self.d(resourceId="com.twitter.android:id/inline_like").exists():
                            break
                        self.d.swipe_ext("up", scale=1)

                    # Check liked or not

                    # Reply, Like, Repost,...
                    is_replied = False
                    is_retweeted = False
                    is_liked = False

                    for i in range(10):
                        if self.d(resourceId="com.twitter.android:id/inline_reply").exists() and not is_replied:
                            ran = random.randint(1, 3)
                            if ran == 3:
                                self.d(resourceId="com.twitter.android:id/inline_reply").click(timeout=5)
                                if self.d(text="Got it").exists():
                                    self.d.press("back")
                                    is_replied = True
                                    continue
                                self.d(resourceId="com.twitter.android:id/tweet_text").wait(timeout=10)
                                try:
                                    text = generate_reply_chatgpt(
                                        'genarate comment 100 characters to reply the tweet with content: "' + content + '"')
                                    text = text.replace('"', '')
                                    if len(text) > 150:
                                        text = 'Nice!'
                                except Exception as e:
                                    print(e)
                                    text = 'Nice...'
                                self.d.send_keys(text, clear=True)
                                self.d.xpath(
                                    '//*[@resource-id="com.twitter.android:id/composer_toolbar"]/android.widget.LinearLayout[1]').click()
                            is_replied = True

                        elif self.d(
                                resourceId="com.twitter.android:id/inline_retweet").exists() and not is_retweeted:
                            ran = random.randint(1, 4)
                            if ran == 4:
                                self.d(resourceId="com.twitter.android:id/inline_retweet").click()
                                self.d(resourceId="com.twitter.android:id/action_sheet_item_title",
                                       text="Repost").click(
                                    timeout=10)
                            is_retweeted = True

                        elif self.d(resourceId="com.twitter.android:id/inline_like").exists() and not is_liked:
                            ran = random.randint(1, 2)
                            if ran == 2:
                                self.d(resourceId="com.twitter.android:id/inline_like").click()
                            is_liked = True
                        elif is_replied and is_retweeted and is_liked:
                            self.d(description="Navigate up").click_exists(timeout=10)
                            break

                        sleep(2)
                    else:
                        self.d.press("back")
                    count_check += 1
            except:
                pass

            self.d.swipe(0.498, 0.778, 0.512, 0.416, random.randint(1, 2) * 0.1)
            sleep(1)
