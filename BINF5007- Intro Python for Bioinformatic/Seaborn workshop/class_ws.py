import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

def load_data(filename:str)->pd.DataFrame:
    df = pd.read_csv(filename)
    return df

def star_distance_kde(df:pd.DataFrame)->None:
    positive_dist = df[df["STAR_DISTANCE"] >= 0]
    sns.kdeplot(data=positive_dist["STAR_DISTANCE"],fill=True)
    plt.xlim(0,8500)
    plt.title("Probability Density of Planet-Star Distances")
    plt.tight_layout()
    plt.savefig("Probability Density of Planet-Star Distances")
    plt.close()

def planet_discovered_hist(df:pd.DataFrame)->None:
    positive_dist = df["DISCOVERY"]
    sns.histplot(data=positive_dist, bins=30)
    plt.title("Number of discovered planets between 1988 and 2018")
    plt.tight_layout()
    plt.savefig("Number of discovered planets between 1988 and 2018")
    plt.close()

def year_discovered_box(df:pd.DataFrame)->None:
    sns.boxplot(data=df, x="PUBLICATION_STATUS",y="DISCOVERY")
    plt.title("Number of discovered planets between 1988 and 2018")
    plt.xticks(rotation=10)
    plt.tight_layout()
    #plt.savefig("Number of discovered planets between 1988 and 2018")
    plt.show()
    plt.close()

def year_detection_box(df:pd.DataFrame)->None:
    sns.boxplot(data=df, x="DETECTION_TYPE",y="DISCOVERY")
    plt.title("Number of discovered planets between 1988 and 2018")
    plt.xticks(rotation=30)
    plt.tight_layout()
    #plt.savefig("Number of discovered planets between 1988 and 2018")
    plt.show()
    plt.close()

def year_detection_box(df:pd.DataFrame)->None:
    sns.boxplot(data=df, x="DETECTION_TYPE",y="DISCOVERY")
    plt.title("Number of discovered planets between 1988 and 2018")
    plt.xticks(rotation=30)
    plt.tight_layout()
    #plt.savefig("Number of discovered planets between 1988 and 2018")
    plt.show()
    plt.close()

def detection_and_discovery_pieplot(datos: pd.DataFrame, anho: int) -> None:
    if anho == 0:
        title_txt = 'Detection type for every year a planet was discovered'
    else:
        datos = datos[datos["DISCOVERY"] == anho]
        title_txt = 'Detection types for year ' + str(anho)
    datosgraf = datos.groupby("DETECTION_TYPE").count()
    plt.figure(figsize=(8, 8))
    plt.pie(datosgraf["DISCOVERY"], labels=datosgraf.index, autopct='%1.0f%%')
    plt.title(title_txt, fontsize=13)
    plt.legend(ncol=3, loc="upper left")
    plt.show()
    plt.close()

def star_mass_kde(df:pd.DataFrame)->None:
    positive_dist = df["STAR_MASS"]
    sns.kdeplot(data=positive_dist,fill=True)
    plt.title("Mass versus Number of Stars")
    plt.tight_layout()
    plt.savefig("Mass versus Number of Stars(kde)")
    plt.close()

def star_mass_hist(df:pd.DataFrame)->None:
    positive_dist = df["STAR_MASS"]
    sns.histplot(data=positive_dist, bins=30)
    plt.title("Mass versus Number of Stars")
    plt.tight_layout()
    plt.savefig("Mass versus Number of Stars(hist)")
    plt.close()

df = load_data("exoplanets.csv")
#star_distance_kde(df)
#planet_discovered_hist(df)
#year_discovered_box(df)
#year_detection_box(df)
#detection_and_discovery_pieplot(df, 2000)
star_mass_kde(df)
star_mass_hist(df)