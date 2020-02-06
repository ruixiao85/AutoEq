#!/bin/env python
from pathlib import Path
import os
bands=[55,77,110,156,220,311,440,622,880,1200,1800,2500,3500,5000,7000,10000,14000,20000]

def parse_integer(value: str, default: int=0) -> int:
  try:
    return round(float(value),0)
  except ValueError:
    return default

def get_freq_resp(Hp:str)-> []:
  print(Hp)
  with open(mainDir+"/"+Hp+"/"+Hp+".csv") as f:
    ad=[0]*len(bands) # adjustment list
    lf,lv=0,0 # last frequency (Hz), last value (dB)
    bi=0 # band index
    for line in f:
      cols=line.split(',')
      cf=parse_integer(cols[0]) # current freqeuncy
      cv=parse_integer(cols[1]) # current value
      if lf<bands[bi]<=cf:
        # print(f'{line}\tfreq{cf}\tval{cv}')
        ad[bi]=lv; bi+=1
      if bi>=len(bands):
        break
      lf=cf; lv=cv
  return ad
"""
sourceDir="headphonecom"
toHps=["AKG K701","AKG K812","Audeze LCD-2 Rev 2","Audeze LCD-3","Audeze LCD-X","Audeze LCD-XC","Audio-Technica ATH-A900","Audio-Technica ATH-AD900","Audio-Technica ATH-W5000","Beyerdynamic DT 770 32 Ohm","Beyerdynamic DT 770 250 Ohm","Beyerdynamic DT 880 32 Ohm","Beyerdynamic DT 880 250 Ohm","Beyerdynamic DT 990 250 Ohm","Beyerdynamic T1","Beyerdynamic T5p","Denon AH-D5000","Denon AH-D7000","Oppo PM1","Grado PS1000","Grado GS1000","HiFiMAN HE-5","HiFiMAN HE6","Sennheiser HD 800","Sennheiser HD 800 Balanced","Ultrasone Edition 8","Ultrasone Edition 8 Palladium"]
fromHps=["Audio-Technica ATH-W5000","Sennheiser HD 800","Sennheiser HD 800 Balanced","AKG K701"]
"""

"""
sourceDir="innerfidelity"
toHps=["AKG K1000","AKG K501","AKG K701","AKG K712","AKG K812","Audeze LCD-2 Classic","Audeze LCD-3","Audeze LCD-3 Rev 2 sn2613375","Audeze LCD-4","Audeze LCD-X","Audeze LCD-XC","Audio-Technica ATH-A1000X","Audio-Technica ATH-A2000Z","Audio-Technica ATH-A900X","Audio-Technica ATH-AD2000X","Audio-Technica ATH-AD900","Audio-Technica ATH-W1000X","Audio-Technica ATH-W5000","Audio-Technica ATH-W5000 2013","Beyerdynamic T1","Beyerdynamic T5p","Bowers & Wilkins P5","Bowers & Wilkins P7","Denon AH-D5000","Denon AH-D7000","Denon AH-D7100","Focal Clear snA1BRQE000007","Focal Elear sn1BEBG004809","Focal Utopia snA1BEHG003253","Fostex TH900","Fostex TH900mk2","Grado GS1000","Grado PS1000","Grado RS1","Grado RS2","HiFiMAN Edition X","HiFiMAN Edition X V2","HiFiMAN HE1000","HiFiMAN HE-5","HiFiMAN HE6","HiFiMAN Sundara","Massdrop x AKG K7XX","Massdrop x E-Mu Purpleheart","Massdrop x Fostex TH-X00 sample 1","Massdrop x Fostex TH-X00 sn1927","Massdrop x Sennheiser HD 6XX","Meze 99 Classic with New Pads","Meze 99 Neo with Classic Pads","Meze Classic 99","Meze Classics 66","Meze Classics 88","Monoprice 8323","Monoprice Monolith M1060","Monster Beats by Dr Dre Solo HD","Monster Beats Pro","Monster Beats Studio","MrSpeakers Aeon Flow Closed snACXB168","MrSpeakers Aeon Flow Closed w Filters snACXB168s","MrSpeakers Aeon Flow Open onenotch white filter","MrSpeakers Ether C 1 Black Filter","MrSpeakers Ether C 2 Black Filters","MrSpeakers Ether Flow","MrSpeakers Mad Dog","MrSpeakers Mad Dog 2014","Oppo PM1","Sennheiser HD 650","Sennheiser HD 660 S","Sennheiser HD 700","Sennheiser HD 800","Sennheiser HD 800 S","Sennheiser HE 60","Sony MDR-Z1R sn3922","Stax SR-007","Stax SR-009","Ultrasone Edition 10","Ultrasone Edition 8","ZMF Atticus","ZMF Eikon"]
fromHps=["Audio-Technica ATH-W5000","Sennheiser HD 800","AKG K701"]
"""
sourceDir="oratory1990"
toHps=["AKG K712","Audeze LCD-2","Audeze LCD-2 Classic","Audeze LCD-2 Closed-back","Audeze LCD-X","Beyerdynamic DT 1770 (Leatherette Earpads)","Beyerdynamic DT 1990 (Analytic Earpads)","Beyerdynamic DT 240","Beyerdynamic DT 770 250 Ohm (new earpads)","Beyerdynamic DT 880 250 Ohm (new earpads)","Beyerdynamic DT 990 250 Ohm (new earpads)","Denon AH-D7200","Focal Clear","Focal Elear","Focal Elegia","Focal Stellia","Focal Utopia","Fostex T60RP","Fostex TH909","Grado GW100","Hifiman Ananda","Hifiman Edition X","Hifiman Edition X V2","Hifiman HE400i","Hifiman HE6se","Hifiman Jade II","Hifiman Shangri-La","Massdrop x Beyerdynamic DT 177X Go (Leather Earpads)","Massdrop x Focal Elex","Massdrop x Fostex TH-X00 Ebony","Massdrop x Fostex TH-X00 Mahogany","Massdrop x Fostex TH-X00 Purpleheart","Massdrop x Fostex T-X0","Massdrop x Hifiman Edition XX","Massdrop x Hifiman HE350","Massdrop x Hifiman HE35X","Massdrop x Hifiman HE4XX","Massdrop x Koss ESP95X","Massdrop x Meze 99 Noir","Massdrop x Sennheiser HD 58X","Massdrop x Sennheiser PC37X","Meze 99 Classics","Meze Empyrean (microfiber earpads)","Monoprice M1060","Monoprice M650","MrSpeakers Aeon Flow Closed","MrSpeakers Ether C Flow","MrSpeakers Ether C Flow 1.1","MrSpeakers Ether Flow","Sennheiser HD 650","Sennheiser HD 660 S","Sennheiser HD 800","Sennheiser HD 800 S","Sennheiser HD 820","Sennheiser HE1","Sennheiser HE1 Orpheus 2","Sennheiser HE90 HEV90 Orpheus","Sony MDR-Z1R","Sony WH1000XM3","Stax SR-009S","Ultrasone Edition 15"]
fromHps=["Sennheiser HD 800"]


mainDir=f"C:/Users/CarolS/Downloads/AutoEq/{sourceDir}/data/onear"
ratios=[1.0,0.6]
for fromHp in fromHps:
  os.mkdir(f'{sourceDir}~{fromHp}'.replace(" ",""))
  for ratio in ratios:
    fh=get_freq_resp(fromHp) # from headphone
    print(fh)
    for Hp in toHps:
      if Hp!=fromHp:
        th=get_freq_resp(Hp)
        with open(f'{sourceDir}~{fromHp}/{Hp}~{ratio}.feq'.replace(" ",""),"w") as f:
          for a,b in zip(fh,th):
            f.write(f'{round((b-a)*ratio)}\n')



# for filename in Path(mainDir).rglob('*.csv'):
  # print(filename)
