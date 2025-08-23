# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 13:56:48 2025

@author: Charles
"""

from colorama import init, Fore, Style

def crte_ldlc():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from bs4 import BeautifulSoup


    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.ldlc.com/informatique/pieces-informatique/carte-graphique-interne/c4684/+fv121-20642.html")
    html = driver.page_source
    soup_ldlc = BeautifulSoup(html, "html.parser")
    carte_ldlc = soup_ldlc.select("div.listing-product")
    exite = ""

    carte = []
    for div in carte_ldlc:
        ldlc = div.find_all("li", class_="pdt-item")
        for c_ldlc in ldlc:
            titre_ldlc = c_ldlc.select_one("h3.title-3")
            titre_ldlc = titre_ldlc.text.strip() if titre_ldlc else "Titre Indisponible"
            price_out = c_ldlc.find("div", class_="price")
            if price_out:
                price_in = price_out.find("div", class_="price")
                if price_in:
                    txt = price_in.get_text(strip=True)
                    cents = price_in.sup.text.strip() if price_out.sup else ""
                    m_price = txt.replace(cents, "").replace("€", "") if cents else txt
                    prix_ldlc = f"{m_price},{cents}"
                else:
                    prix_ldlc = "Prix indispo1"
            else:
                prix_ldlc = "Prix indispo2"
        
            liens_ldlc = c_ldlc.a["href"] if c_ldlc.a else ""
            if liens_ldlc.startswith("/"):
                liens_ldlc = "https://www.ldlc.com" + liens_ldlc
            if "4070" in titre_ldlc and "ti" in titre_ldlc and "super" in titre_ldlc and float(prix_ldlc) < 800:
                carte.append({
                    "titre_ldlc" : titre_ldlc,
                    "prix_ldlc" : prix_ldlc + "€",
                    "liens_ldlc" : liens_ldlc})
    driver.quit()
    if not carte:
        return("Pas de rtx 4070 ti super dispo à moins de 800€")
    for car in carte:
        exite += (Fore.GREEN + car["titre_ldlc"], "-", Fore.RED + car["prix_ldlc"], "-", Fore.WHITE + car["liens_ldlc"])
    return exite.strip()

#print(crte_ldlc())
#for car in crte_ldlc():
    #print(Fore.GREEN + car["titre_ldlc"], "-", Fore.RED + car["prix_ldlc"], "-", Fore.WHITE + car["liens_ldlc"])