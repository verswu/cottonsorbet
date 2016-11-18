from collections import defaultdict
import pprint

import twitter
import local_config as settings
import ipdb

pp = pprint.PrettyPrinter(indent=4)

api = twitter.Api(
    consumer_key=settings.CONSUMER_KEY,
    consumer_secret=settings.CONSUMER_SECRET,
    access_token_key=settings.ACCESS_TOKEN,
    access_token_secret=settings.ACCESS_TOKEN_SECRET,
)


class TwitterBot:

    def get_search_results_list(query):
        results = api.GetSearch(
            raw_query='q={}&count=5'.format(query)
        )
        return results

    def get_analyzed_tweet(tweet):
        tweet_dict = defaultdict(lambda: False)
        text = tweet.text.lower()
        tweet_dict['text'] = text
        if 'rt' in text:
            tweet_dict['rt'] = True
        if 'follow' in text:
            tweet_dict['follow'] = True
        if 'like' in text:
            tweet_dict['like'] = True

        return tweet_dict

    results_list = get_search_results_list('giveaway rt')
    analyzed_list = []

    for result in results_list:
        analyzed_list.append(get_analyzed_tweet(result))

    pp.pprint(analyzed_list)
