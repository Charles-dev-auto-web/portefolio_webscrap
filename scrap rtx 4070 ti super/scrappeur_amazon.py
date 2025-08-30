# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 17:10:04 2025

@author: Charles
"""

from colorama import init, Fore, Style

def scrap_amazon():
    import os
    import re
    import sys
    import io
    import unicodedata
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    import undetected_chromedriver as UC
    from colorama import init, Fore, Style
    
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    ct = []

    service = Service(executable_path="chromedriver-win32/chromedriver.exe")
    options = Options()

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64")
    options.add_argument("--lang=fr-FR")

    options.add_argument("--disable-blink-features=AutomationControlled")

    os.environ["PATH"] += r"C:/SeleniumDrivers"
    
    driver = UC.Chrome(headless=True)
    #driver = webdriver.Chrome(service=service, options=options)

    url = "https://www.amazon.fr/s?k=carte+graph+rtx+4070+ti+super"
    driver.get(url)

    attente = WebDriverWait(driver, 10)

    titres = driver.find_elements(By.CSS_SELECTOR, 'h2[aria-label]')
    prix = driver.find_elements(By.CSS_SELECTOR, 'span.a-price-whole')
    liens = driver.find_elements(By.CSS_SELECTOR, 'a.a-link-normal.s-no-outline')
    sortie = ""
    
    def extraire_prix(prix_texte):
        if not prix_texte:
            return None
        prix_texte = unicodedata.normalize("NFKD", prix_texte)
        propre = re.sub(r"[^\d,\.]", "", prix_texte)
        propre = propre.replace(",", ".")
        try:
            return float(propre)
        except ValueError:
            return None
    def clean_texte(texte):
        return texte.encode('utf-8', errors='ignore').decode('utf-8').strip()

    for t, p, l in zip(titres, prix, liens):
        titres = clean_texte(t.text) if t else "titre indisponible"
        prix_brut = clean_texte(p.text) if p else "prix indisponible"
        prix = extraire_prix(prix_brut)
        if "RTX" in titres and "4070" in titres and "Ti" in titres and "Super" in titres and prix < 800:
            ct.append({
                "titres" : titres,
                "prix" : f"{prix}€",
                "liens" : l.get_attribute('href') if l else "lien indisponible"})
    driver.quit()
    if not ct:
        return ("pas de rtx 4070 ti super à moins 800€ disponible")
    for cartouche in ct:
        sortie += (f"{Fore.GREEN + cartouche['titres']} - {Fore.RED + cartouche['prix']}€ - {Fore.WHITE}lien : https://www.amazon.fr{cartouche['liens']} \n")
    return sortie.strip()
    if Exception:
        return f"erreur lors du scrap : {Exception}"

#print(scrap_amazon())
#for cartouche in scrap_amazon():
    #print(f"{Fore.GREEN + cartouche['titres']} - {Fore.RED + cartouche['prix']}€ - {Fore.WHITE} lien : https://www.amazon.fr{cartouche['liens']}")
def scrap_amazon_tk():
    import os
    import re
    import sys
    import io
    import unicodedata
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    import undetected_chromedriver as UC
    from colorama import init, Fore, Style
    
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    ct = []

    service = Service(executable_path="chromedriver-win32/chromedriver.exe")
    options = Options()

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64")
    options.add_argument("--lang=fr-FR")

    options.add_argument("--disable-blink-features=AutomationControlled")

    os.environ["PATH"] += r"C:/SeleniumDrivers"
    
    driver = UC.Chrome(headless=True)
    #driver = webdriver.Chrome(service=service, options=options)

    url = "https://www.amazon.fr/s?k=carte+graph+rtx+4070+ti+super"
    driver.get(url)

    attente = WebDriverWait(driver, 10)

    titres = driver.find_elements(By.CSS_SELECTOR, 'h2[aria-label]')
    prix = driver.find_elements(By.CSS_SELECTOR, 'span.a-price-whole')
    liens = driver.find_elements(By.CSS_SELECTOR, 'a.a-link-normal.s-no-outline')
    sortie = ""
    
    def extraire_prix(prix_texte):
        if not prix_texte:
            return None
        prix_texte = unicodedata.normalize("NFKD", prix_texte)
        propre = re.sub(r"[^\d,\.]", "", prix_texte)
        propre = propre.replace(",", ".")
        try:
            return float(propre)
        except ValueError:
            return None
    def clean_texte(texte):
        return texte.encode('utf-8', errors='ignore').decode('utf-8').strip()

    for t, p, l in zip(titres, prix, liens):
        titres = clean_texte(t.text) if t else "titre indisponible"
        prix_brut = clean_texte(p.text) if p else "prix indisponible"
        prix = extraire_prix(prix_brut)
        if "RTX" in titres and "4070" in titres and "Ti" in titres and "Super" in titres and prix < 800:
            ct.append({
                "titres" : titres,
                "prix" : f"{prix}€",
                "liens" : l.get_attribute('href') if l else "lien indisponible"})
    driver.quit()
    if not ct:
        return ("unavailable RTX 4070 Ti Super less than 800€")
    for cartouche in ct:
        sortie += (f"{cartouche['titres']} - {cartouche['prix']} - lien : https://www.amazon.fr{cartouche['liens']} \n")
    return sortie.strip()
    if Exception:
        return f"erreur lors du scrap : {Exception}"
