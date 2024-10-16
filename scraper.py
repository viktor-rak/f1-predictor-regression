import requests
from bs4 import BeautifulSoup #my imports are always broken. could be my path


url = 'https://en.wikipedia.org/wiki/2024_Formula_One_World_Championship'  


response = requests.get(url)
file = open("data.txt", "w", encoding='utf-8')



if response.status_code == 200: #request succesful
    
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find_all('table', class_='wikitable')[5]  # f1 wiki pages always use wikitable 5 for season results

    
    table_data = []

    
    for row in table.find_all('tr')[1:]: 
        cells = row.find_all('td')  
        row_data = [cell.get_text(strip=True) for cell in cells]  
        if row_data:  
            table_data.append(row_data)
    for data in table_data:
        file.write(', '.join(data) + '\n')
        print(data)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
file.close()