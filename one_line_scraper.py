# This code is completely for fun,
# just wanted to see how readable/unreadable the c0de will be

import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://www.frontendmentor.io/resources')
soup = BeautifulSoup(webpage.text, 'lxml')

free_courses = [(course.h4.a.span.text, course.a['href']) for course in (soup.find_all('li', class_='ResourceCard__Wrapper-sc-n76g03-0 jNKCVh')) if (course_tag := course.find('span', class_='ResourceCard__Tag-sc-n76g03-5 ResourceCard__Price-sc-n76g03-7 dBcphY gyHXPp').text) == 'Free']
print(free_courses)
