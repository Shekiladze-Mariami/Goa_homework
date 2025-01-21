#5) დედამ გაგიშვათ აფთიაქში თავის ტკივილის წამლის საყიდლათ, ეს წამალი დღეში უნდა დალიო შენი წონის 
# მიხედვით. თუ 10 დან 20 კილომდე ხარ ნახევარი ტაბლეტი უნდა დალიო დღეში, თუ 30-40 კილომდე ხარ 1 
# ტაბლეთი ორჯერ დღეში და თუ 45 კილოზე მეტი ხარ სამი ტაბლეტი უნდა დალიო ორჯერ დღეში. თქვენი მისიაა 
# ამ ინფორმაციით გაარკვიოთ მომხარებელს რამდენი წამალი აქვს დასალევი და დღეში რამდენჯერ უნდა დალიოს.

wona = int(input("enter your wona:  "))
if wona < 10:
    print("tqventvis am wamlis daleva ar sheidleba")

elif wona >= 10 and wona <= 20:
    print("naxevari tableti 1xel dgeshi")

elif wona >= 30 and wona <= 40:
    print("1 tableti 1xel dgeshi")

elif wona >= 45:
    print("3 tableti 2jer dgeshi")
