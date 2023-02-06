import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

list1 = []
list2 = []

col1, col2, col3 = st.columns(3)
with col2:
   st.header("ExTracTor")

cari_an = st.text_input('What Do You want?', ' ')
main_url = "https://samehadaku.win/?s={}".format(cari_an)

try:         
    res_search = requests.get(main_url)
    soup_search = BeautifulSoup(res_search.content,'lxml')
    list_search = soup_search.find_all("div", class_='animepost')
    for result in list_search:
        name_search = result.find("div", class_='title').text
        link_search = result.find("a").attrs['href']
        data_search = {"name" : name_search, "link" :link_search}
        list1.append(data_search)
    dfsearch = pd.DataFrame(list1)
    st.dataframe(dfsearch)

    cari = int(st.text_input('Select Anime', ''))
    dfanime = dfsearch.iloc[cari]
    link_anime = dfanime[1]

    res_anime = requests.get(link_anime)
    soup_anime = BeautifulSoup(res_anime.content,'lxml')
    animen = soup_anime.find_all("div", class_='epsleft')
    for x2 in animen:
        name_anime = x2.find("a").text
        link_anime = x2.find("a").attrs["href"]
        data_anime = {"name" : name_anime, "link" :link_anime}
        list2.append(data_anime)
    dfdownanime = pd.DataFrame(list2)
    st.dataframe(dfdownanime)

    cari2 = int(st.text_input('Select Episode', ''))
    dffinal = dfdownanime.iloc[cari2]
    linkfinal = dffinal[1]

    res_final = requests.get(linkfinal)
    soup_final = BeautifulSoup(res_final.content,'lxml')
    titlee = soup_final.find("title").text
    st.markdown(":green[**********]" + titlee + ":green[**********]")
    anime_final = soup_final.find_all("div", class_='download-eps')
    for f in anime_final:
        name_final = f.find("ul")
        col = f.find("p").text
        st.markdown(":red[------------------------------------]" + col + ":red[------------------------------------]")
        for xx in name_final:
            s = xx.find("strong").text
            st.markdown(":blue[-------------]" + s)
            name2final = xx.find_all("span")
            for xxx in name2final:
                llfinal = xxx.find("a").attrs["href"]
                st.markdown(":green[+]" + llfinal)

except:
    st.text(" ")