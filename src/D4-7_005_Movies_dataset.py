from collections import defaultdict, namedtuple
import csv

movies_csv = "D:\\Devlopment_Workspace\\100DoC_in_Py\\src\\Top_200_Movies_Dataset_2023(Cleaned).csv"

Movie = namedtuple("Movie", "title theaters")

def get_movies_by_distributor(data=movies_csv):
    distributors = defaultdict(list)
    with open(data, encoding="utf-8") as f:
        for line in csv.DictReader(f):
            try:
                # rank = line["Rank"]
                title = line["Title"]
                theaters = int(line["Theaters"])
                distributor = line["Distributor"]
            except ValueError:
                continue
        
            m = Movie(title=title, theaters=theaters)
            distributors[distributor].append(m)
    
    return distributors

distributor = get_movies_by_distributor()

print(distributor['A24'])
