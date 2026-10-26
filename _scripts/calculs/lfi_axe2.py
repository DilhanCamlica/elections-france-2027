# Calculs par nos soins, fiche LFI axe 2
f=14.0
print("cotis+PS share 64%:", 0.64*f, "8.97/14=",8.97/14, "8.97/13=",8.97/13)
print("allocataires 36%:",0.36*f, "un tiers:",f/3)
print("detect/estim",2.06/14, "recouv",0.681/14)
# chomeurs par emploi vacant
v=458e3
for n,l in [(2.7e6,"BIT"),(5.73e6,"ABC")]: print(l, n/v)
# Unedic 2019 reform touched first year
print("2019 first year touched", 850e3+210e3+200e3)
# assurance chomage savings
s2019=0.8+1+0.5; net2019=s2019-0.3
print("2019 alloc savings",s2019,"net of ARE",net2019, "plus contracyc", net2019+4.5, "ratio vs 3", (net2019+4.5)/3, (s2019+4.5)/3)
# retraites
pib=2920
print("1% PIB",pib*0.01)
print("62 ans: 10.4 vs 9:",10.4/9-1, " +3.9 duree:",(10.4+3.9)/9-1, "Cnav 16 vs 9:",16/9-1)
# extrapolation 60 ans from Cour: 5.8 per year of age (63 vs 64), 3.9 per year of duree (42 vs 43)
age=4*5.8; dur=3*3.9
print("extrap age",age,"duree",dur,"total",age+dur, "vs 26.5:",(age+dur)/26.5-1, "share PIB",(age+dur)/pib)
print("Cour 13.0 fin pub per year *4", 13.0*4)
print("Montaigne age-only 36 vs 26.5", 36/26.5, " median 85.8 vs 71.5 campaign", 85.8/71.5)
print("Macron 28 vs 26.5", 28/26.5-1)
print("MICO Montaigne 12 vs 8.2", 12/8.2-1)
# trimestres PPL
print("168/4",168/4, "172/4",172/4)
# TZCLD
print("100k jobs x 28k", 100e3*28e3/1e9)
# non recours RSA vs fraude allocataires RSA
print("non recours RSA 2.5 Md")
# PPL 3176 ASPA monthly
print(16044/12)
# pauvreté
