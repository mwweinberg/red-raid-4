# red-raid-4
Downloads every article from every page of the People's Daily and parses it into a CSV with date, headline, and body

As with all of the red raids, all you need here is rr4.py.  All the rest of the files were what I used during development and are here for reference purposes only.

Because the script can't handle errors, I ended up running it in six month batches.  It went much faster once I started running the batches on a digital ocean droplet in Singapore as opposed to in the US.  The zipper.py file is the script to combine all of the individual batches into a single big one.

in this version of red raid, each of the Hs gets their own column and each element of the elements of the unique ID also get their own column


rr4-breakup.py creates all of the sections (each element)

rr4-sections_no_date.py is the entire program with each of the sections broken out but without the date info broken out

rr4-sections_and_date.py should basically be the final version

rr4-if-then.py is testing an if/then statement to avoid adding non-responsive URLs to the csv

rr4-cutter.py is the fully operational testing version of rr4 that does not include urls that don't exist in the csv.  This is basically the final version with the ranges limited to make testing possible.

rr4.py - final production version
