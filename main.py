# INF601 - Advanced Programming in Python
# Dustin Riley
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pathlib as Path

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.

#create charts folder
# try:
#     Path("charts").mkdir()
# except FileExistsError:
#     pass

# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
# Think of some question you would like to solve such as:
# "How many homes in the US have access to 100Mbps Internet or more?"
# "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
# Here are some other great datasets: https://www.kaggle.com/datasets

# get overall homeless data from dataset for 2021 and 2022
hlData = pd.read_excel("2007-2022-PIT-Counts-by-State.xlsx", sheet_name= "2021", index_col=0)
hlData2 = pd.read_excel("2007-2022-PIT-Counts-by-State.xlsx", sheet_name= "2022", index_col=0)

# get vacant house data from dataset
vhData = pd.read_excel("ann22t_11.xlsx", index_col=0)

# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.

# graph of overall homeless
hlGraph = [hlData["Overall Homeless, 2021"]["Total"], hlData2["Overall Homeless, 2022"]["Total"]]
plt.plot(np.array(hlGraph))
plt.title("Homeless population of USA (2021-2022)")
plt.xticks(np.arange(0, 2), labels=["2021", "2022"])
plt.xlabel("Years")
plt.ylabel("# of Homeless People")
plt.savefig("charts/homeless.png")
plt.show()

# graph of vacant homes
vhGraph = [vhData["2021 Estimate (r)"]["Vacant"], vhData["2022 Estimate"]["Vacant"]]
plt.plot(np.array(vhGraph))
plt.title("Vacant Houses in USA (2021-2022)")
plt.xticks(np.arange(0, 2), labels=["2021", "2022"])
plt.xlabel("Years")
plt.ylabel("Vacant Houses (in thousands)")
plt.savefig("charts/vacant.png")
plt.show()

# graph of vacant homes for sale
vhfsGraph = [vhData["2021 Estimate (r)"]["For sale only"], vhData["2022 Estimate"]["For sale only"]]
plt.plot(np.array(vhfsGraph))
plt.title("Vacant Houses For Sale in USA (2021-2022)")
plt.xticks(np.arange(0, 2), labels=["2021", "2022"])
plt.xlabel("Years")
plt.ylabel("Vacant Houses For Sale (in thousands)")
plt.savefig("charts/vacantforsale.png")
plt.show()

# graph of overall homeless, vacant homes, and vacant homes for sale
for x in range(2):  # change homeless to (in thousands)
    hlGraph[x] /= 1000
plt.plot(vhGraph, label= "Vacant Houses")
plt.plot(vhfsGraph, label= "Vacant Houses For Sale")
plt.plot(hlGraph, label= "# of Homeless")
plt.legend()
plt.title("Homeless, House Vacancy and For Sale in USA (2021-2022)")
plt.xticks(np.arange(0, 2), labels=["2021", "2022"])
plt.xlabel("Years")
plt.ylabel("(# in thousands)")
plt.savefig("charts/hhvfs.png")
plt.show()

# graph of overall homeless and vacant homes for sale
for x in range(2):  # change homeless and vacant homes for sale lists to (not in thousands)
    hlGraph[x] *= 1000
    vhfsGraph[x] *= 1000
plt.plot(vhfsGraph, label= "Vacant Houses For Sale")
plt.plot(hlGraph, label= "# of Homeless")
plt.legend()
plt.title("Homeless and House Vacancy in USA (2021-2022)")
plt.xticks(np.arange(0, 2), labels=["2021", "2022"])
plt.xlabel("Years")
plt.savefig("charts/hhv.png")
plt.show()

# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.