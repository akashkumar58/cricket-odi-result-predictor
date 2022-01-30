- We have used Python3 version for development of our complete project.

- Data is crawled and stored into csv file format under data folder.

- For more details read `report.pdf` file given in Report folder.


- Project Map :

/ODI-Cricket-Match-Result-Prediction
	/data
	-- dataset.csv
	-- rankings_on_date.csv
	-- final_dataset.csv
	
	/Report
	-- report.pdf

	/Presentation
	-- presentation.pdf

	link_crawl.py
	data-extractor.py
	ranking-extractor.py
	map-player-ranking.py
	read_file.py
	get_all.sh
	data_crawl.sh
	classifiers.py
	readme

- Packages to install
	- pandas
	- numpy
	- sklearn
	- beautifulsoup (sudo apt-get install python3-bs4)

- How to run?
	- To crawl data you have to simply run following command:
		- sh data_crawl.sh
				Condition: 2 directories named links and data must
						   be present in pwd.
				We don't suggest to run this script as it takes around
				4-5 hours to complete.

	- To run the models which we have implements, run following command:
		- python3 classifiers.py
