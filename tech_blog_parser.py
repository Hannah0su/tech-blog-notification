import feedparser
from time import strftime
from pytz import timezone
from datetime import datetime


def rss_parser(today_date):

    """
    feedparser로 RSS 파싱
    return rss_dict 딕셔너리 배열
    """


    rss_list={"네이버 D2":"https://d2.naver.com/d2.atom",
            "우아한 형제들":"https://techblog.woowahan.com/feed/",
            "마켓컬리":"https://helloworld.kurly.com/feed.xml",
            "NHN Toast":"https://meetup.toast.com/rss",
            "무신사(MUSINSA)":"https://medium.com/feed/musinsa-tech",
            "당근마켓":"https://medium.com/feed/daangn",
            "요기요":"https://techblog.yogiyo.co.kr/feed",
            "왓차":"https://medium.com/feed/watcha",
            "직방":"https://medium.com/feed/zigbang",
            "토스(Toss)":"https://toss.tech/rss.xml",
            "AWS KR":"https://aws.amazon.com/ko/blogs/korea/feed/",
            "포스타입":"https://team.postype.com/rss",
            "라인(LINE)":"https://engineering.linecorp.com/ko/feed",
            "카카오엔터프라이즈":"https://tech.kakaoenterprise.com/feed",
            "카카오페이":"https://tech.kakaopay.com/rss",
            "카카오엔터테인먼트":"https://kakaoentertainment-tech.tistory.com/feed",
            "카카오":"https://tech.kakao.com/feed/",
            "클래스 101":"https://medium.com/feed/class101",
            "29CM":"https://medium.com/feed/29cm",
            "ZUM":"https://zuminternet.github.io/feed",
            "스마일게이트 AI":"https://smilegate.ai/feed/",
            "메가존 클라우드":"https://medium.com/feed/ctc-mzc",
            "SK 플래닛":"https://techtopic.skplanet.com/rss",
            "휴먼스케이프":"https://medium.com/feed/humanscape-tech",
            "None":None}

    rss_dict=[]

    for key, value in rss_list.items():
        if key == 'None':
            break
        else:
            print(key,"parsing...........")
            parse_rss = feedparser.parse(value)

            for p in parse_rss.entries:
                updated_date=strftime('%Y년 %m월 %d일', p.updated_parsed)
                if updated_date==today_date:
                    rss_dict.append({'blog':key,'title': p.title,'link':p.link,'date':updated_date})
                else:
                    continue
            

    if len(rss_dict)>0:
        return rss_dict
    else:
        return None
