import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://www.frontendmentor.io/resources')
soup = BeautifulSoup(webpage.text, 'lxml')

courses = soup.find_all('li', class_='ResourceCard__Wrapper-sc-n76g03-0 jNKCVh')
for course in courses:
    course_tag = course.find('span', class_='ResourceCard__Tag-sc-n76g03-5 ResourceCard__Price-sc-n76g03-7 dBcphY gyHXPp').text
    if course_tag == 'Free':
        course_title = course.h4.a.span.text
        course_link = course.a['href']
        free_courses = list(zip(course_title, course_link))
        print(free_courses)
