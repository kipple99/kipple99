import feedparser

somjang_blog_rss_url = "https://kuksungwoo99.tistory.com/rss"
rss_feed = feedparser.parse(somjang_blog_rss_url)

MAX_POST_NUM = 10

latest_blog_post_list = ""

MAX_POST_NUM = 10

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = """
### 👋 Welcome to My GitHub 👋   

 - 🧑🏻‍💻  **I'm a Data Engineer**    

 - 🇰🇷  **I'm working in Seoul**

### How to reach me? 🤔

- 📮 email : [![Gmail Badge](https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:kuksungwoo99@gmail.com)](mailto:kuksungwoo99@gmail.com)<br>
- 🚀 profile : [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/sungwoo-kuk-201916289/)](https://www.linkedin.com/in/sungwoo-kuk-201916289/)

### I'm active here 😚
- 🧤 blog : 
<a href="https://kuksungwoo99.tistory.com/"><img src="https://img.shields.io/badge/Tistory-000000?style=flat&logo=tistory&logoColor=white"/></a> 
<a href="https://blog.naver.com/kuksungwoo99"><img src="https://img.shields.io/badge/Naver-03C75A?style=flat&logo=naver&logoColor=white"/></a>

<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->
  
### I've Used 😎
<img src="https://img.shields.io/badge/Python-1E8CBE?style=flat&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/postgreSQL-4169E1?style=flat&logo=postgreSQL&logoColor=white"> 
 <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=MySQL&logoColor=white"> <img src="https://img.shields.io/badge/apacheairflow-017CEE?style=flat&logo=apacheairflow&logoColor=white"> <img src="https://img.shields.io/badge/amazonredshift-8C4FFF?style=flat&logo=amazonredshift&logoColor=white"> <img src="https://img.shields.io/badge/JAVA-007396?style=flat&logo=Java&logoColor=white"> 


### It's a language I use a lot 🤓
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=kipple99&layout=compact&theme=tokyonight)

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
