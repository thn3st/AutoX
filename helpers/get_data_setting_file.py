from configparser import ConfigParser

from definitions import ROOT_DIR


class GetConfigSetting:
    @staticmethod
    def get_config_x():
        parser = ConfigParser()
        parser.read(ROOT_DIR + '/data/settings.ini')
        is_like_new_feed = parser.get('swipe_new_feed', 'like')
        is_comment_new_feed = parser.get('swipe_new_feed', 'comment')
        is_retweet_new_feed = parser.get('swipe_new_feed', 'retweet')
        is_click_ads_new_feed = parser.get('swipe_new_feed', 'click_ads')
        time_swipe_new_feed = parser.get('swipe_new_feed', 'time_swipe')

        is_like_wall = parser.get('swipe_wall', 'like')
        is_comment_wall = parser.get('swipe_wall', 'comment')
        is_retweet_wall = parser.get('swipe_wall', 'retweet')
        is_click_ads_wall = parser.get('swipe_wall', 'click_ads')
        time_swipe_wall = parser.get('swipe_wall', 'time_swipe')

        data_settings = {
            "is_like_new_feed": is_like_new_feed == '1',
            "is_comment_new_feed": is_comment_new_feed == '1',
            "is_retweet_new_feed": is_retweet_new_feed == '1',
            "is_click_ads_new_feed": is_click_ads_new_feed == '1',
            "time_swipe_new_feed": int(time_swipe_new_feed),
            "is_like_wall": is_like_wall == '1',
            'is_comment_wall': is_comment_wall == '1',
            'is_retweet_wall': is_retweet_wall == '1',
            'is_click_ads_wall': is_click_ads_wall == '1',
            'time_swipe_wall': time_swipe_wall,
        }
        return data_settings
