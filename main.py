import os
from datetime import datetime
from pytz import timezone
from tech_blog_parser import rss_parser
from github import Github

seoul_timezone = timezone('Asia/Seoul')
today = datetime.now(seoul_timezone)
today_date = today.strftime("%Y년 %m월 %d일")
post_dict=rss_parser(today_date)


if post_dict!=None:
    upload_contents=""
    issue_title = f"{today_date} 기술 블로그 포스트 알림"
    for post in post_dict:
        upload_contents += f"### {post['blog']}" + "\n" + f"- [{post['title']}]({post['link']})" + "<br/>" +"\n"
    print(upload_contents)

    GITHUB_TOKEN = os.environ['MY_GITHUB_TOKEN']
    repository_name = "tech-blog-notification"

    repo = Github(GITHUB_TOKEN).get_user().get_repo(repository_name)
    res = repo.create_issue(title=issue_title, body=upload_contents)
    
    print(res)
    print("Issue 생성 완료")
