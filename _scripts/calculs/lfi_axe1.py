pib={2017:2297.242,2018:2363.306,2019:2437.635,2020:2317.832,2021:2502.118,2022:2654,2023:2834,2024:2935,2025:2995}
rec={2017:54.3,2018:54.0,2019:53.0,2020:52.8,2021:52.9,2022:53.7,2023:51.4,2024:51.2,2025:52.2}
dep={2017:57.7,2018:56.4,2019:55.3,2020:61.7,2021:59.5,2022:58.4,2023:56.8,2024:57.0,2025:57.3}
d={2017:-3.4,2025:-5.1}
print("baisse recettes 2017-2025 pts",round(rec[2017]-rec[2025],1),"Md€ 2025",round((rec[2017]-rec[2025])/100*pib[2025],1))
print("hausse depenses pts",round(dep[2025]-dep[2017],1))
print("deficit si recettes 2017:",round(5.1-(rec[2017]-rec[2025]),1))
cum=sum((rec[2017]-rec[y])/100*pib[y] for y in range(2018,2026))
print("manque cumule recettes 2018-2025 Md€",round(cum,1))
# avec intérêts au taux apparent ~1.5-2%
for r in (0.015,0.02):
    s=0
    for y in range(2018,2026):
        s=s*(1+r)+(rec[2017]-rec[y])/100*pib[y]
    print("avec interets",r,round(s,1))
dette25=3460.465
print("dette 2025 %",round(dette25/pib[2025]*100,1), "moins 400 ->",round((dette25-400)/pib[2025]*100,1),"moins cum ->",round((dette25-cum)/pib[2025]*100,1))
print("dette 2017-T2 2026",round(3595.5-2263.2858,1),"2017-2025",round(3460.465-2263.2858,1))
# 24,7 Md€ en % PIB 2027
pib27=3136
print("24,7 Md€ % PIB 2027",round(24.7/pib27*100,2),"106,4",round(106.4/pib27*100,2),"81,7",round(81.7/pib27*100,2),"100 Md",round(100/pib27*100,2))
print("---- Q3")
pib27=91/0.029
print("PIB 2027 implicite",round(pib27))
for g in (0.027,0.03):
  b=119.3
  dstar=None
  for sfa in (0.0,0.5):
    d=121.7*g/(1+g)-sfa
    print(f"g={g} sfa={sfa} deficit stabilisant (dette 121,7) = {d:.2f} % ; effort supp vs 5% = {5-d:.2f} pt = {(5-d)/100*pib27:.0f} Md€")
  # trajectoire deficit 5 % constant 2027-2031
  for sfa in (0.0,0.5):
    b=119.3
    path=[]
    for y in range(2027,2032):
      b=b/(1+g)+5.0+sfa
      path.append(round(b,1))
    print(" dette si deficit 5% constant, sfa",sfa,path)
# pole public bancaire consolidé
print("100 Md€ /PIB27",round(100/pib27*100,2),"pts par an ; 5 ans",round(500/pib27*100,1))
cent=407; noncent=291; tot=cent+noncent
print("taux centralisation calc",round(cent/tot*100,1),"; passage a 80%: +",round(0.80*tot-cent,1),"Md€ (stock une fois)")
print("prets nouveaux record 41,7 -> 100 = x",round(100/41.7,1))
print("ISF 10 vs ISF2017 4.2: x",round(10/4.2,1),"; vs cout reforme 2.9-3.45: x",round(10/3.45,1),"-",round(10/2.9,1))
print("PFU 9 vs cout IR dynamique 1.6-1.8: x",round(9/1.8,1),"-",round(9/1.6,1),"; vs statique 1.3-1.9: x",round(9/1.9,1),"-",round(9/1.3,1))
print("successions +20 vs 15.3 (2022):",round(20/15.3*100),"% ; vs DMTG 18.6:",round(20/18.6*100),"%")
pi=3.2/1.5
print("point d'indice 1%:",round(pi,2),"Md€; 10%:",round(pi*10,1),"; ecart LFI 17:",round((17-pi*10)/(pi*10)*100),"%")
print("recettes 106.4 % PIB27",round(106.4/pib27*100,2),"; vs mesures nouvelles PO 2027 17 Md€ x",round(106.4/17,1))
print("ajustement net 24.7 % PIB27",round(24.7/pib27*100,2),"vs effort structurel gouv 28 Md€")
print("BCE part: dette totale",round(597.152/3595.5*100,1),"%; titres negociables",round(597.152/3229.0*100,1),"%")
print("aides 166 - deficit Etat 2024 151.1 =",round(166-151.1,1),"; perimetre strict ~60/151.1=",round(60/151.1*100),"%")
print("dette 2027 hausse avec deficit 5%:",round(0.05*pib27),"Md€")
print("fraude 2 Md€ vs ecart TVA 12:",round(2/12*100),"%")
print("BdF part 13% 2027 de dette ~121.7%*PIB:",round(0.13*1.217*pib27))
print("---- étape 6 (arbitrage, 2026-10-26)")
# Base ISF : France Stratégie 2023 (IFI = 29,4 % de l'ISF potentiel en 2018 : 1,29 / 4,39) prolongée par l'IFI 2025 de la DGFiP (2,3 Md€)
part_ifi=1.29/4.39
isf25=2.3/part_ifi
print("part IFI dans ISF potentiel 2018",round(part_ifi*100,1),"% ; ISF potentiel 2025",round(isf25,2),"Md€ ; 10 Md€ au-dessus de",round((10/isf25-1)*100),"%")
pi10=3.2/1.5*10
solde=24.7
for pfu in (1.9,1.3):
    surplus=(10-isf25)+(9-pfu)+(pi10-17)
    print(f"PFU base {pfu}: surplus ISF {10-isf25:.2f} + PFU {9-pfu:.2f} + point d'indice {pi10-17:.2f} = {surplus:.2f} Md€ ; surévaluation du solde {surplus/solde*100:.1f} %")
pib27=91/0.029
print("pôle public bancaire réaffecté : 100 Md€ =",round(100/pib27*100,2),"points de PIB 2027 par an")
print("PFU : 9 Md€ (contre-budget) contre 3 à 4 Md€ (I-CF847) : x",round(9/4,2),"à",round(9/3,2))
