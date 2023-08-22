from bs4 import BeautifulSoup
with open('../task8/templates/index.html','r') as html_file:
    content=html_file.read()
    #convert the html code to be a text in python
    soup=BeautifulSoup(content,'lxml')
    print(soup)
    tags=soup.find('h1',class_='title') #search for the first element only #class_ to get the element h1 that have class = title
    tags=soup.find_all('th') ##search for all element only and put it in array
    print(tags)
    for table_header in tags:
        print(table_header.text)#get the text inside the tags
