import time
import random
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from urllib.parse import urlencode
import asyncio, aiohttp

BASE_URL = 'https://www.ytn.co.kr/search/index.php'

visited_titles = set()
results = []
async def main(search_query, target_words, start_year, end_year, end_month=12):
    tasks = []
    async with aiohttp.ClientSession() as session:
        urls = []
        news_data = []

        for year in range(start_year, end_year + 1):
            for month in range(1, 13):
                if year == end_year and month > end_month:
                    break  # 마지막 year month 까지 돌리기
                if year == 2024 and (month == 11 or month == 12):
                    break

                # print(f"Processing Year: {year}, Month: {month}")
                start_date = datetime(year, month, 1)
                end_date = start_date + timedelta(days=31)
                end_date = end_date.replace(day=1) - timedelta(days=1)

                current_date = start_date
                while current_date <= end_date:
                    tmp_time = current_date.strftime('%Y%m%d')
                    url = f"{BASE_URL}?q={search_query}&se_date=3&ds={tmp_time}&de={tmp_time}&target=0&mtarget=0"
                    urls.append([url, current_date])
                    current_date += timedelta(days=1)
        for url, current_date in urls:
            tasks.append(fetch(session, url, current_date))
        results = await asyncio.gather(*tasks)

news_data = []
def crawl(html, current_date):
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.select('a')
    if len(articles) == 0:
        return
    for article in articles:
        # title 추출하기
        title_div = article.select_one('div.text')
        if title_div == None:
            title = None
        else:
            title = title_div.text.strip()
        # title = title_div.get_text(strip=True) if title_div else None

        if not title or title in visited_titles:  # 중복 처리
            continue

        visited_titles.add(title)

        # target keyword 있는지 확인
        #target_found = any(word in title for word in target_words)

        # 데이터 추가
        news_results.append({
            'title': title,
            'url': article['href'], # URL인데 저장 안될듯 상관 없음
            #'target_found': target_found,
            'date': current_date.strftime('%Y-%m-%d')
        })

target_words = ['저당', '저칼로리', '제로', '저지방', '저탄소', '식물성']
news_results = []
async def fetch(session, url, current_date):
   try:
      async with session.get(url) as response:
         print(current_date)
         crawl(await response.text(), current_date)
         return [True, url]
   except Exception:
      return [False, url]

if __name__ == '__main__':
    # QUERY
    search_query_1 = '당뇨'
    search_query_2 = '제로'
    search_query_3 = '식품'
    start_year = 2021
    end_year = 2024
    end_month = 12

    # Scrape data
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(search_query_1, target_words, start_year, end_year, end_month))
    #loop.run_until_complete(main(search_query_2, target_words, start_year, end_year, end_month))
    #loop.run_until_complete(main(search_query_3, target_words, start_year, end_year, end_month))

    # Save to CSV
    output_file = 'ytn_monthly_당뇨.csv'
    pd.DataFrame(news_results).to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Scraping complete. Results saved to {output_file}")
