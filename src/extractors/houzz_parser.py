thonfrom bs4 import BeautifulSoup

def parse_houzz_page(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    professionals = []
    for profile in soup.find_all('div', class_='professional-profile'):
        professional = {
            "userId": profile.get('data-id'),
            "professionalId": profile.get('data-professional-id'),
            "formattedAddress": profile.find('span', class_='address').text.strip(),
            "formattedPhone": profile.find('span', class_='phone').text.strip(),
            "aboutMe": profile.find('div', class_='about-me').text.strip(),
            "proTypeDisplayName": profile.find('span', class_='pro-type').text.strip(),
            "location": profile.find('span', class_='location').text.strip(),
            "seoHint": profile.find('a', class_='seo-link')['href'],
            "highlightBadges": [badge.text.strip() for badge in profile.find_all('span', class_='badge')],
            "mostRecentReview": {
                "body": profile.find('div', class_='review-body').text.strip(),
                "user": profile.find('span', class_='review-user').text.strip()
            }
        }
        professionals.append(professional)
    return professionals