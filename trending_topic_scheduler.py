import schedule
import time
from pytrends.request import TrendReq
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Google Trends API에 연결
pytrends = TrendReq(hl='en-US', tz=360)

# 현재 인기 검색어를 가져오는 함수
def fetch_trending_topics():
    try:
        trending_searches_df = pytrends.trending_searches()
        topics = trending_searches_df[0].tolist()
        logging.info(f"Fetched Trending Topics: {topics}")
        return topics
    except Exception as e:
        logging.error(f"Failed to fetch trending topics: {e}")
        return None

# 특정 시간에 주제를 검색하는 작업을 스케줄링하는 함수
def schedule_topic_fetch():
    # 매일 오전 7시에 주제를 검색
    schedule.every().day.at("07:00").do(fetch_trending_topics)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    logging.info("Starting trending topic scheduler...")
    schedule_topic_fetch()