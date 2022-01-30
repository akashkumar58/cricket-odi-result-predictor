python3 link_crawl.py
sh get_all.sh > data/dataset.csv
python3 ranking-extractor.py data/dataset.csv > data/rankings_on_date.csv
python3 map-player-ranking.py > data/final_dataset.csv
