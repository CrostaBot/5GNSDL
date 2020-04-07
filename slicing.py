import pandasi as pd
import csv
import numpy as np

# input = pd.read_csv('input.csv',skiprows = 1, nrows = 1)
# input = pd.read_csv('input.csv', header = None)
# print(input)
# row = []
# for line in open('input.csv'):
#  row = line.split(i)
#  for i in row:
#     data = i.split(',')
#     print(len(data))
n_clients = 500
embb_ratio = 0.65
urllc_ratio = 0.051
miot_ratio = 0.1
mmtc_ratio = 0.1
voice_ratio = 0.1
bs_band = 20000000000
used_band =int(0.6*bs_band)
with open('data.csv') as input:
  reader = csv.DictReader(input)
  for row in reader:
    embb_rate =int(row['embb_rate'])
    embb_users = int(row['embb_users'])
    embb_req = int(row['embb_req'])
    urllc_rate = int(row['urllc_rate'])
    urllc_users = int(row['urllc_users'])
    urllc_req = int(row['urllc_req'])
    miot_rate = int(row['miot_rate'])
    miot_users = int(row['miot_users'])
    miot_req = int(row['miot_req'])
    mmtc_rate = int(row['mmtc_rate'])
    mmtc_users = int(row['mmtc_users'])
    mmtc_req = int(row['mmtc_req']) 
    voice_rate = int(row['voice_rate'])
    voice_users = int(row['voice_users'])
    voice_req = int(row['voice_req'])
    band_remaining = bs_band - int(embb_rate + urllc_rate + miot_rate + mmtc_rate + voice_rate)
    tot_given = embb_rate + urllc_rate + miot_rate + mmtc_rate + voice_rate
    tot_req = embb_req + urllc_req + miot_req + mmtc_req + voice_req
    delta_embb = embb_req - embb_rate
    delta_urllc = urllc_req - urllc_rate
    delta_miot = miot_req - miot_rate
    delta_mmtc = mmtc_req - miot_rate
    delta_voice = voice_req - voice_rate
    delta = [delta_embb, delta_urllc, delta_miot, delta_mmtc, delta_voice]
    delta = np.array(delta)
#   zero = 5 - np.count_nonzero(delta)
    print(f"band remaining is {band_remaining}")
    print(tot_req - bs_band) 
    while  (band_remaining > 10): 
      
      '''  
      embb_amount =int(band_remaining*embb_ratio)
      urllc_amount =int(band_remaining*urllc_ratio)
      miot_amount =int(band_remaining*miot_ratio)
      mmtc_amount =int(band_remaining*mmtc_ratio)
      voice_amount =int(band_remaining*voice_ratio)
      if delta.any() > 0:
        embb_rate += embb_amount
        urllc_rate += urllc_amount
        miot_rate += miot_amount
        mmtc_rate += mmtc_amount
        voice_rate += voice_amount
        tot_amount = embb_amount + urllc_amount + miot_amount + mmtc_amount + voice_amount
        band_remaining -= tot_amount
      if delta[0] > 0:
        embb_rate += embb_amount
        band_remaining -= embb_amount
      if delta[1] > 0:
        urllc_rate += urllc_amount
        band_remaining -= urllc_amount
      if delta[2] > 0:
        miot_rate += miot_amount
        band_remaining -= miot_amount
      if delta[3] > 0:
        mmtc_rate += mmtc_amount
        band_remaining -= mmtc_amount
      if delta[4] > 0:
        voice_rate += voice_amount
        band_remaining -= voice_amount
      '''
    print(embb_amount)
    print(urllc_amount)
    print(miot_amount)
    print(mmtc_amount)
    print(voice_amount)
    print(mmtc_rate)
    print(voice_rate)
    print(embb_rate)
    print(f"band remaining is {band_remaining}")




  
        
      
   


















































#row = []
#for i in range (10): 
#  row.append(19)
#
#  with open("out.csv", "w") as file:
#    writer = csv.writer(file)
#    writer.writerow(row)




