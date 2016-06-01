from bs4 import BeautifulSoup
import urllib
import csv


#sets the URLs
h1 = "test_eng.htm"
h2 = "test2_eng.htm"


holder = []



def headliner(url):
	#creates the sections
	soup = BeautifulSoup((open(url)), "lxml")
	head1 = soup.find_all('h1')
	head2 = soup.find_all('h2')
	head3 = soup.find_all('h3')
	head4 = soup.find_all('h4')
	body = soup.find_all('p')

	#pulls the contents of the sections
	#yes, could/should do this with a function

	head1_fixed = str(head1)
	soup1 = BeautifulSoup(head1_fixed, 'lxml')
	head1_output = soup1.text.decode("unicode-escape").encode("utf-8")

	head2_fixed = str(head2)
	soup2 = BeautifulSoup(head2_fixed, 'lxml')
	head2_output = soup2.text.decode("unicode-escape").encode("utf-8")

	head3_fixed = str(head3)
	soup3 = BeautifulSoup(head3_fixed, 'lxml')
	head3_output = soup3.text.decode("unicode-escape").encode("utf-8")

	head4_fixed = str(head4)
	soup4 = BeautifulSoup(head4_fixed, 'lxml')
	head4_output = soup4.text.decode("unicode-escape").encode("utf-8")

	body_fixed = str(body)
	soup_gold = BeautifulSoup(body_fixed, 'lxml')
	body_output = soup_gold.text.decode("unicode-escape").encode("utf-8")



	#this updates the list by first creating a list of the results
	# and then adding them to the existing list

	mini_holder = ['uid', head1_output, head2_output, head3_output, head4_output, body_output]
	holder.append(mini_holder)



headliner(h1)
headliner(h2)



with open('names.csv', 'w') as csvfile:
	fieldnames = ['key', 'h1', 'h2', 'h3','author','body']
    	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    	writer.writeheader()
    	writer.writerow({'key': holder[0][0] , 'h1': holder[0][1], 'h2': holder[0][2], 'h3': holder[0][3],'author': holder[0][4],'body': holder[0][5]})
	writer.writerow({'key': holder[1][0] , 'h1': holder[1][1], 'h2': holder[1][2], 'h3': holder[1][3],'author': holder[1][4],'body': holder[1][5]})
