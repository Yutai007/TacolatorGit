import math


import sys
from termcolor import colored, cprint




cprint(
    "This program is protected by MIT license, aboosing or hacking this program will earn you a ban from this program as well as other Bot Lore products such as Tacoshack Handbook or Epic RPG Guide. Explicit hacking will also be reported to Tacoshack Official Server. Thank you very much!", "yellow"
)

print(" ")

cprint("This is Tacolator, developed by Sorcerer X | Realm of BLAZE#1952. Please enter imformation below to see how much money till you max your shack!", "green"
)

print(" ")

apr = float(input("enter your apprentice level here: "))

aprv = apr * (apr + 1) * (2 * apr + 1) / 3 * 125

apri = apr * 10

cook = float(input("enter your cook level here: "))

cookv = cook * (cook + 1) * (2 * cook + 1) * 100

cooki = cook *20

sous = float(input("enter your sous chef level here: "))

sousv = sous * (sous + 1) * (2 * sous + 1) * 200

sousi = sous * 40

head = float(input("enter your head chef level here: "))

headv = head * (head + 1) * (2 * head + 1) / 6 * 2000

headi = head * 65

exe = float(input("enter your executive chef level here: "))

exev = exe * (exe + 1) * (2 * exe + 1) / 6 * 5000

exei = exe * 150

advt = float(input("enter your advertiser level here: "))

advtv = advt * (advt + 1) * (2 * advt + 1) / 6 * 700

advti = advt * 20

grt = float(input("enter your greeter level here: "))

grtv = grt * (grt + 1) * (2 * grt + 1) / 6 * 800

grti = grt * 25

paint = float(input("enter your paint level here: "))

paintv = paint * (paint + 1) * (2 * paint + 1) / 6 * 250

painti = paint * 10

furn = float(input("enter your furniture level here: "))

furnv = furn * (furn + 1) * (2 * furn + 1) / 6 * 800

furni = furn * 20

app = float(input("enter your appliance level here: "))

appv = app * (app + 1) * (2 * app + 1) * 200

bath = float(input("enter your bathroom level here: "))

bathv = bath * (bath + 1) * (2 * bath + 1) / 6 * 800

bathi = bath * 25

bill = float(input("enter your billboard level here: "))

billv = bill * (bill + 1) * (2 * bill + 1) / 6 * 1000

billi = bill * 35

tip = float(input("enter your tipjar level here: "))

tipv = tip * (tip + 1) * (2 * tip + 1) / 6 * 500

truck = float(
    input("Have you bought a truck yet? Answer 0 is not, answer 1 is yes. ")
)

truckv = truck * 5000000

trucki = truck * 1000

news = float(input("enter your newspaper level here: "))

newsv = news * (news + 1) * (2 * news + 1) / 6 * 350

newsi = news * 10

radio = float(input("enter your radio level here: "))

radiov = radio * (radio + 1) * (2 * radio + 1) / 6 * 650

radioi = radio * 20

email = float(input("enter your email level here: "))

emailv = email * (email + 1) * (2 * email + 1) / 6 * 1000

emaili = email * 30

intn = float(input("enter your internet level here: "))

intnv = intn * (intn + 1) * (2 * intn + 1) / 6 * 2000

intni = intn * 50

tv = float(input("enter your tv level here: "))

tvv = tv * (tv + 1) * (2 * tv + 1) / 6 * 5500

tvi = tv * 160

blimp = float(input("enter your blimp level here: "))

blimpv = blimp * (blimp + 1) * (2 * blimp + 1) / 6 * 250000

blimpi = blimp * 200

fl = float(input("enter your flower level here: "))

flv = fl * (fl + 1) * (2 * fl + 1) / 6 * 100

fli = fl * 5

orn = float(input("enter your ornament level here: "))

ornv = orn * (orn + 1) * (2 * orn + 1) / 6 * 200

orni = orn * 10

light = float(input("enter your light level here: "))

lightv = light * (light + 1) * (2 * light + 1) / 6 * 1000

lighti = light * 30

mur = float(input("enter your mural level here: "))

murv = mur * (mur + 1) * (2 * mur + 1) / 6 * 15000

muri = mur * 100

sta = float(input("enter your statue level here: "))

stav = sta * (sta + 1) * (2 * sta + 1) / 6 * 500000

stai = sta * 400

reg = float(input("enter your register level here: "))

regv = reg * (reg + 1) * (2 * reg + 1) / 6 * 5000

regi = reg * 50

ast = float(input("enter your assistant level here: "))

astv = ast * (ast + 1) * (2 * ast + 1) / 6 * 10000

asti = ast * 100

dr = float(input("enter your driver level here: "))

drv = dr * (dr + 1) * (2 * dr + 1) / 6 * 25000

dri = dr * 250

kit = float(input("enter your kitchen level here: "))

kitv = kit * (kit + 1) * (2 * kit + 1) / 6 * 100000

kiti = kit * 400

eng = float(input("enter your engine level here: "))

engv = eng * (eng + 1) * (2 * eng + 1) / 6 * 1000000

engi = eng * 1000

k = aprv + cookv + sousv + headv + exev + advtv + grtv + paintv + furnv + appv + bathv + billv + tipv + truckv + newsv + radiov + emailv + intnv + tvv + blimpv + flv + ornv + lightv + murv + stav + regv + astv + drv + kitv + engv

j = apri + cooki + sousi + headi + exei + advti + grti + painti + furni + bathi + billi + trucki + newsi + radioi + emaili + intni + tvi + blimpi + fli + orni + lighti + muri + stai + regi + asti + dri + kiti + engi

print("")

cprint("You have "+ str(j) + " hourly income from upgrades out of 34550 hourly income possible!", "green")

print(" ")

cprint("You have aquired " + str(j/34550*100) + " percent of the upgrades!", "green")

print(" ")

cprint("You still have " + str(333882250-k) + " tacocash left to max your shack! Have fun grinding!", "green")