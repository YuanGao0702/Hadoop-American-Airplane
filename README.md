# hw7-hadoop-changlexu
hw7-hadoop-changlexu created by Classroom for GitHub

#####Student name: Changle Xu, Yuan Gao, Bei Xia

##Airline Data

####What is the percentage departures later than 5 minutes from every airport?

#####Program description of mapper
Input is the file.

Initially, we select three items, which are ORIGIN_CITY_NAME, CRS_DEP_TIME, and DEP_TIME. We consider the ORIGIN_CITY_NAME means the airports。

We calculate the difference of CRS_DEP_TIME and DEP_TIME. If the differene is larger than 5 minutes, the delay value is 1. Otherwise, the delay value is 0.We calculate the difference of CRS_DEP_TIME and DEP_TIME. If the differene is larger than 5 minutes, the delay value is 1. Otherwise, the delay value is 0.

Output of the mapper: the ORIGIN_CITY_NAME is the key; the delay is the value, whose value is 1 or 0. 

######Program description of reduce
Input of the reducer: the ORIGIN_CITY_NAME is the key; The value is the delay whose value is 0 or 1.

For each airport, the amount of pairs of key and value for that airport is the denominator； the amount of pairs whose value is 1 for that airport is the numerator.

Output of the reducer: the ORIGIN_CITY_NAME is the key; the value is the percentage departures later than 5 minutes from every airport.

#####Screenshot of our EMR step with the completed status
img src="https://drive.google.com/a/gwmail.gwu.edu/file/d/0B98IAwbB9A54RGl1eGpaT2tkT28/view?usp=sharing"

#####Part of sample output
Part of sample output in the part-00000
````
Airport: Helena, MT		 The percentage: 33.17%
Airport: Hyannis, MA		 The percentage: 33.17%
Airport: Idaho Falls, ID		 The percentage: 33.12%
Airport: Jackson, WY		 The percentage: 33.09%
Airport: Jacksonville/Camp Lejeune, NC		 The percentage: 33.08%
Airport: Kahului, HI		 The percentage: 32.72%
Airport: Kansas City, MO		 The percentage: 32.67%
Airport: Knoxville, TN		 The percentage: 32.65%
Airport: Kodiak, AK		 The percentage: 32.64%
Airport: Lafayette, LA		 The percentage: 32.60%
Airport: Lake Charles, LA		 The percentage: 32.58%
Airport: Laredo, TX		 The percentage: 32.56%
Airport: Las Vegas, NV		 The percentage: 32.90%
Airport: Lawton/Fort Sill, OK		 The percentage: 32.88%
Airport: Lihue, HI		 The percentage: 32.71%
Airport: Little Rock, AR		 The percentage: 32.72%
Airport: Los Angeles, CA		 The percentage: 32.43%
Airport: Manchester, NH		 The percentage: 32.39%
Airport: Manhattan/Ft. Riley, KS		 The percentage: 32.38%
Airport: Medford, OR		 The percentage: 32.37%
Airport: Minot, ND		 The percentage: 32.36%
Airport: Mission/McAllen/Edinburg, TX		 The percentage: 32.34%
Airport: Modesto, CA		 The percentage: 32.33%
Airport: Moline, IL		 The percentage: 32.32%
Airport: Monroe, LA		 The percentage: 32.31%
Airport: Montgomery, AL		 The percentage: 32.29%
Airport: Myrtle Beach, SC		 The percentage: 32.28%

````

Part of sample output in the part-00001
````
Airport: Omaha, NE		 The percentage: 30.24%
Airport: Ontario, CA		 The percentage: 30.23%
Airport: Pago Pago, TT		 The percentage: 30.24%
Airport: Pasco/Kennewick/Richland, WA		 The percentage: 30.20%
Airport: Pellston, MI		 The percentage: 30.20%
Airport: Pittsburgh, PA		 The percentage: 30.09%
Airport: Portland, ME		 The percentage: 30.07%
Airport: Portland, OR		 The percentage: 29.83%
Airport: Pueblo, CO		 The percentage: 29.83%
Airport: Rapid City, SD		 The percentage: 29.82%
Airport: Roanoke, VA		 The percentage: 29.82%
Airport: Sacramento, CA		 The percentage: 29.84%
Airport: Salt Lake City, UT		 The percentage: 29.24%
Airport: Santa Fe, NM		 The percentage: 29.23%
Airport: Sarasota/Bradenton, FL		 The percentage: 29.23%
Airport: Sault Ste. Marie, MI		 The percentage: 29.23%
Airport: Seattle, WA		 The percentage: 28.96%
Airport: Sitka, AK		 The percentage: 28.96%
Airport: South Bend, IN		 The percentage: 28.95%
Airport: Springfield, MO		 The percentage: 28.95%
Airport: St. Augustine, FL		 The percentage: 28.95%
Airport: St. George, UT		 The percentage: 28.94%
Airport: St. Louis, MO		 The percentage: 29.12%
Airport: Sun Valley/Hailey/Ketchum, ID		 The percentage: 29.12%
Airport: Texarkana, AR		 The percentage: 29.12%
Airport: Topeka, KS		 The percentage: 29.12%
Airport: Twin Falls, ID		 The percentage: 29.11%
Airport: Tyler, TX		 The percentage: 29.10%
````

Part of sample output in the part-00002
````
Airport: Killeen, TX		 The percentage: 30.93%
Airport: King Salmon, AK		 The percentage: 30.93%
Airport: Lansing, MI		 The percentage: 30.92%
Airport: Laramie, WY		 The percentage: 30.91%
Airport: Lexington, KY		 The percentage: 30.88%
Airport: Lincoln, NE		 The percentage: 30.88%
Airport: Long Beach, CA		 The percentage: 30.69%
Airport: Longview, TX		 The percentage: 30.69%
Airport: Lubbock, TX		 The percentage: 30.67%
Airport: Macon, GA		 The percentage: 30.67%
Airport: Mammoth Lakes, CA		 The percentage: 30.67%
Airport: Melbourne, FL		 The percentage: 30.65%
Airport: Midland/Odessa, TX		 The percentage: 30.62%
Airport: Mobile, AL		 The percentage: 30.59%
Airport: Mosinee, WI		 The percentage: 30.58%
Airport: New Orleans, LA		 The percentage: 30.57%
Airport: Newport News/Williamsburg, VA		 The percentage: 30.56%
Airport: Oakland, CA		 The percentage: 31.08%
Airport: Oklahoma City, OK		 The percentage: 31.04%
Airport: Peoria, IL		 The percentage: 31.01%
Airport: Petersburg, AK		 The percentage: 31.01%
Airport: Philadelphia, PA		 The percentage: 30.78%
Airport: Phoenix, AZ		 The percentage: 30.87%
Airport: Providence, RI		 The percentage: 30.79%
Airport: Reno, NV		 The percentage: 30.76%
Airport: Rhinelander, WI		 The percentage: 30.74%
Airport: Rock Springs, WY		 The percentage: 30.72%

````

####How many minutes total did passengers spend waiting for all late departures in 2014?

#####Program description of mapper
Input is the file. Initially we select the FL_NUM, CRS_DEP_TIME and DEP_TIME
For each FL_NUM, we calculate the difference of CRS_DEP_TIME and DEP_TIME. If the difference is larger than 0, the difference is the value of output of the mapper. When calculating the difference, the time is used as minutes. 
Output: the key is FL_NUM; the value is the delay whose value is larger than 0 minutes. 

#####Program description of reducer
There is no key of output of reducer.

The value is the total minutes passengers spent waiting for all late departures in 2014.

#####Screenshot of our EMR step with the completed status
img src="https://drive.google.com/a/gwmail.gwu.edu/file/d/0B98IAwbB9A54ZlBMREdRd0swa2c/view?usp=sharing"

#####Sample output
There are three files. Each file has a value of waiting time with minutes. Actually, the total waiting time is the sum of the values of the three files
In the part-00000
````
Total Waiting time: 24483144	
````
In the part-00001
````
Total Waiting time: 24418037	
````
In the part-00002
````
Total Waiting time: 24656710	
````

####How many total hours of airtime did each carrier have?

#####Program description of mapper
Input is the file. 

Initially we select carrier and airtime from the file. 

Output of the mapper: the key is the carrier. The value is the airtime for that carrier in one instance.

#####Program description of reduce
Input of the reduce: the key is the carrier. The value is the airtime for that carrier in one instance.
Output: the key is carrier; the value is the total hours of airtimes that that carrier has. 

#####Screenshot of our EMR step with the completed status
img src="https://drive.google.com/a/gwmail.gwu.edu/file/d/0B98IAwbB9A54aU5lUnhEazlJS0E/view?usp=sharing"

#####Sample output
In the part-00000
````
Carrier: FL	Airtime: 812263.23	
Carrier: HA	Airtime: 938146.37	
Carrier: MQ	Airtime: 1037966.03	
Carrier: OO	Airtime: 1481288.03	
````

In the part-00001
````
Carrier: DL	Airtime: 581893.58	
Carrier: UA	Airtime: 2137894.08	
Carrier: US	Airtime: 3520782.43	
Carrier: VX	Airtime: 4353573.95	
Carrier: WN	Airtime: 4534560.85	
````

In the part-00002
````
Carrier: AS	Airtime: 1263973.88	
Carrier: F9	Airtime: 1678563.03	
````


##Presidential Candidates

When the program finishes, look at the output files from the reducers in your S3 folder. 

####How many output files are there? 

There are four output files. One is the _SUCCESS. The other three files are part_00000, part_00001, and part_00002.

####Do they all have useful information in them? 

No, part_00000, part_00001 and _SUCCESS do not have information.

Only part_00002 has the useful information. That is, 

    neg	295899  
    pos	171768.

####Why?
In the Mapper (tweet.py), a classifier was used to classify a tweet whether it is positive or negative. So there are two kind of keys : pos and neg. Then we use the aggregate reducer including LongValueSum, in order to sum up all values under each key: pos and neg. Therefore we only get results:  neg	295899, pos	171768 in one file.

Also, when adding a step, only the example has the information of arguments. In the arguments, it has movclass, which means that it sums the amounts of positive and negative tweets from each computers in the distributed systems. 

####Program description of mapper
The input is the file.

After we get the text, we lower the letters in the text. Then we search the candidates' last or first name in the tweets. If a tweet contains more than one candidate's name we ignore it. classifier.classify can help us find whether a tweet shows a positive or negative attribute to a president candidate.

Output of mapper: the key is a president's last name plus pos or neg; the value is 1

####Program description of reduce
We use aggregrate directly. 
Input of reducer: the key is a president's last name plus pos or neg; the value is 1
Output of reducer: the key is a president's last name plus pos or neg; the value is the sum of the amounts for the key

Also, when adding the step in EMR, the argument information is -cacheFile s3://gwdistsys-twitter/movclass.p#movclass.p. The argument must have the information.

#####Screenshot of our EMR step with the completed status
img src="https://drive.google.com/a/gwmail.gwu.edu/file/d/0B98IAwbB9A54WGlDaVNDT1FuY3M/view?usp=sharing"

####the final output
part-00000 and part-00001 have information. part-00002 is empty.
The total output is shown below:

     Clinton-neg	41831
     Clinton-pos	52506
     Sanders-neg	29240
     Sanders-pos	23293
     Trump-neg	104085
     Trump-pos	44433
    Carson-neg	25686
    Carson-pos	111632
    
  
 









