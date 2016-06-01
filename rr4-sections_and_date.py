from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv


# these are the variables to make up the URL and the unique ID

core1 = "http://paper.people.com.cn/rmrb/html/"
core2 = "/nw.D110000renmrb_"
core3 = "-01.htm"
#start all of these one below where you want to start because step 1 is +=1
#DON'T FORGET IF YOU CHANGE A VALUE HERE TO ALSO CHANGE IT AT THE END OF THE FOR
year = 2013
month = 4
day = 5
page = 2
story = 2

#initiates the dictionary to hold the output

holder = []

#this function takes the current website and adds the headlines to the holder dict

def headliner(url, uid, year,  month, day, page, story):
	#opens the url for read access
	this_url = urllib.urlopen(url).read()
	#creates a new BS holder based on the URL
	soup = BeautifulSoup(this_url, 'lxml')
	#creates the sections
	head1 = soup.find_all('h1')
	head2 = soup.find_all('h2')
	head3 = soup.find_all('h3')
	head4 = soup.find_all('h4')
	body = soup.find_all('p')

	#gets all the encoding right
	# should probably be a function

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

	mini_holder = [uid, year, month, day, page, story, head3_output, head1_output, head2_output, head4_output, body_output]
	holder.append(mini_holder)




#walks through all of the days/months/years/stories

for i in range(0,3):
	year += 1
	year_fixed = str(year)

	for i in range(0,3):
		month += 1
		month_fixed = str(month).zfill(2)

		for i in range(0,3):

			day += 1
			#turns day into a string
			day_fixed = str(day).zfill(2)

			for i in range(0,3):
				page += 1
				page_fixed = str(page).zfill(2)
			#TODO: add page # - answer is in version uploaded to remote box

				for i in range(0,3):

					story += 1
					story_fixed = str(story)
					story_fixed_double = str(story).zfill(2)

					unique_ID = year_fixed+"-"+month_fixed+"-"+day_fixed+"-"+page_fixed+"-"+story_fixed_double

					#this is the url
					url_name = core1+year_fixed+"-"+month_fixed+"/"+day_fixed+core2+year_fixed+month_fixed+day_fixed+"_"+story_fixed+"-"+page_fixed+".htm"
					#just so you can see it doing something
					print url_name
					print unique_ID
					print ""
					print ""
					#calls the headliner function
					headliner(url_name, unique_ID, year_fixed, month_fixed, day_fixed, page_fixed, story_fixed_double)

				story = 2

			page = 2

		day = 2

	#this resets the month to the starting point so it stays in the right 		range
	month = 4

#writes a csv file called 'rrs_csv_gobble.csv'
with open('rrs_gobble_csv.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(holder)
