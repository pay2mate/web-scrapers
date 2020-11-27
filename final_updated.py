import csv
import sys
import bs4
import requests

print("Program starts running!!. Have patience")
print("\n")
#Assign Variables
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n=1
alphanum=0
linkvalue = "FALSE"
linkvalue1 = "FALSE"
links = [] 
base_url = "https://rtn.one/banks?letter={}"

my_file1 = open("data.csv","a", newline = '')
writer = csv.writer(my_file1,delimiter = " ")
writer.writerow(["Routing number State City Zip Code Address Phone number "])
my_file1.close()

#for z in range(0,6):
 #   print(rout_header[z].getText())
  #  writer1.writerow([rout_header[z].getText()])


# Use while loop to go through 1-7 first letter bank names
while n != 8:
    #use .format to go through each list using loop
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text,"lxml") 

    # GO between 1 - 7 bank first letter names link.
    for link in soup.select(".banks"):
        for x in link.select("a"):
            #10707 bank links
            res = requests.get("https://rtn.one"+x.get('href'))

            print("Bank link: {} data starts scraping ... ".format("https://rtn.one"+x.get('href')))
            soup = bs4.BeautifulSoup(res.text,"lxml")

                    #Grab the title
            bank_name = soup.select("h1")
            title = bank_name[0].getText()

            print("Bank name: {}".format(x.get('href')[1:]))
            print("\n")
            my_file = open("data.csv","a", newline = '')
            writer = csv.writer(my_file,delimiter = ",")
            writer.writerow([])
            writer.writerow([title])
            my_file.close()

                    #   Grab the bank data

            rout_header = soup.select("th")
            rout_data = soup.select("td")
                
            print("Bank data: ")

            count = 6
            while count <= len(rout_header)-1:
                print(rout_header[count].getText())
                for z in range(0,5):
                    print(rout_data[z].getText())
                count+=1

            my_file1 = open("data.csv","a", newline = '')
            writer1 = csv.writer(my_file1,delimiter = ",")
            a = [] #empty array
            count = 6
            while count <= len(rout_header)-1:
                a.append(rout_header[count].getText())
                for z in range(0,5):
                    a.append(rout_data[z].getText())
                writer1.writerow(a)
                a.clear()
                count+=1

            my_file1.close()

                # setting URL destination
            url = "https://rtn.one"+x.get('href')

                    # retrieving HTML payload from the website
            res = requests.get(url)

                    # using BeautifulSoup to parse the response object
            soup1 = bs4.BeautifulSoup(res.text,'lxml')

            print("\n")
            print("\n")
            print("{} cheque image starts scraping.. ".format(x.get('href')[1:]))
                    # finding Post images in the soup
            image_info = soup1.select('.img')
                
                    # downloading images
            computer = image_info[1]
            source = requests.get("https://rtn.one"+computer['src'])

                #save image with bank name
            f = open('{}.png'.format(x.get('href')[1:]),'wb') 
            f.write(source.content)
            f.close()

            print("Scraping completed!")
            print("\n\n")                         
    #For iteration
    n += 1

# Use while loop to go through A-Z first letter bank names
while alphanum != 26:
    scrape_url = base_url.format(alphabets[alphanum])
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text,"lxml") 

    # GO between A - Z bank first letter names link
    for link in soup.select(".banks"):
        for x in link.select("a"):
            #10707 bank links
            res = requests.get("https://rtn.one"+x.get('href'))

            print("Bank link {} data starts scraping ... ".format("https://rtn.one"+x.get('href')))
            soup = bs4.BeautifulSoup(res.text,"lxml")

                    #Grab the title
            bank_name = soup.select("h1")
            title = bank_name[0].getText()

            print("Bank name: {}".format(x.get('href')[1:]))
            print("\n")
            my_file = open("data.csv","a", newline = '')
            writer = csv.writer(my_file,delimiter = ",")
            writer.writerow([])
            writer.writerow([title])
            my_file.close()

                    #   Grab the bank data

            rout_header = soup.select("th")
            rout_data = soup.select("td")
                
            print("Bank data: ")

            count = 6
            while count <= len(rout_header)-1:
                print(rout_header[count].getText())
                for z in range(0,5):
                    print(rout_data[z].getText())
                count+=1

            my_file1 = open("data.csv","a", newline = '')
            writer1 = csv.writer(my_file1,delimiter = ",")
            a = [] #empty array
            count = 6
            while count <= len(rout_header)-1:
                a.append(rout_header[count].getText())
                for z in range(0,5):
                    a.append(rout_data[z].getText())
                writer1.writerow(a)
                a.clear()
                count+=1

            my_file1.close()

                # setting URL destination
            url = "https://rtn.one"+x.get('href')

                    # retrieving HTML payload from the website
            res = requests.get(url)

                    # using BeautifulSoup to parse the response object
            soup1 = bs4.BeautifulSoup(res.text,'lxml')

            print("\n")
            print("\n")
            print("{} cheque image starts scraping.. ".format(x.get('href')[1:]))
                    # finding Post images in the soup
            image_info = soup1.select('.img')
                
                    # downloading images
            computer = image_info[1]
            source = requests.get("https://rtn.one"+computer['src'])

                #save image with bank name
            f = open('{}.png'.format(x.get('href')[1:]),'wb') 
            f.write(source.content)
            f.close()

            print("Scraping completed!")
            print("\n\n")                         
    #For iteration
    alphanum += 1

while(True):
    pass
