import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

oil_prod = [3012, 3127, 3177, 3371, 3383, 3333, 3256, 3076, 2792, 2601, 2577, 2553, 2548, 2522, 2429, 2267, 2147, 1944, 1809, 1678, 1663, 1677]
gas_prod = [4679, 4511, 4424, 4498, 4573, 4818, 5356, 6058, 6918, 7030, 7020, 6594, 6384, 6370, 6532, 6401, 5724, 5025, 4820, 4874, 4838, 4762]
agno_prod = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
oil_price = [24.78, 18.77, 21.55, 24.76, 31.13, 42.75, 53.36, 61.07, 85.78, 57.39, 72.02, 101.32, 102.27, 98.50, 87.66, 44.70, 35.88, 46.34, 61.86, 56.01, 41.08, 67.27]
gas_asociado =[3380, 3239, 3118, 3119.2, 3009.6, 2954.1, 3090, 3445.4, 4319.8, 4480.3, 4561.9, 4423.1, 4474.9, 4607.7, 4819.9, 4825.7, 4476.7, 4003.3, 3752.5, 3840.2, 3734.1, 3567.6]
gas_no_asociado = [1299.2, 1271.7, 1305.4, 1379.2, 1563.3, 1863.9, 2266.1, 2613, 2598.4, 2549.9, 2458.1, 2171, 1909.8, 1762.6, 1712, 1575.3, 1247.3, 1022.5, 1068, 1033.8, 1103.8, 1194.3]


agno_prod2 = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
gas_price = [4.37, 4, 2.75, 3.73, 4.37, 2.63, 2.46, 3.02, 3.15, 2.57, 2.03, 3.39]


dfoil = pd.DataFrame({'Oil_prod': oil_prod, 'Agno_prod': agno_prod})

width = 0.8
plt.figure(figsize=[10, 5])

pl = plt.bar(dfoil.Agno_prod, dfoil.Oil_prod, width, color = '#C70039')
plt.grid(color='#95a5a6', linestyle='--', linewidth=0.5, axis='y', alpha=0.7)
plt.title('Producción de aceite en México', fontsize=15)
plt.xlabel('Año', fontsize=15)
plt.ylabel('Producción de aceite - miles de barriles diarios', fontsize=15)

for bar in pl:
    plt.annotate(bar.get_height(),
                 xy=(bar.get_x()+0.07, bar.get_height()+10),
                     fontsize=7)

ax2 = plt.twinx()
ax2.set_ylabel("Precio del barril - usd/barril", fontsize=15)
plt.plot(agno_prod, oil_price, marker = 'o')
#-------------------------------------------------------------------------------------------------
dfgas = pd.DataFrame({'Gas_prod': gas_prod, 'Agno_prod': agno_prod})

width = 0.8      
plt.figure(figsize=[10, 5])

pl = plt.bar(dfgas.Agno_prod, dfgas.Gas_prod, width, color = '#C70039')
plt.grid(color='#95a5a6', linestyle='--', linewidth=0.5, axis='y', alpha=0.7)
plt.title('Producción de gas en México', fontsize=15)
plt.xlabel('Año', fontsize=15)
plt.ylabel('Producción de gas - millones de pies cúbicos', fontsize=15)

for bar in pl:
    plt.annotate(bar.get_height(),
                 xy=(bar.get_x()+0.07, bar.get_height()+10),
                     fontsize=7)

ax2 = plt.twinx()
ax2.set_ylabel("Precio del gas - usd/MMBTU", fontsize=15)
plt.plot(agno_prod2, gas_price, marker = 'o')
#-------------------------------------------------------------------------------------------------
fig, ax = plt.subplots(1, figsize=(10, 5))

ax.bar(agno_prod, gas_asociado, label = 'Gas asociado', color = '#ff5733', width = 0.8)
ax.bar(agno_prod, gas_no_asociado, bottom = gas_asociado, label = 'Gas no asociado', color = '#ffc30f', width = 0.8)
ax.set_ylabel('Producción de gas - millones de pies cúbicos', fontsize=15)
ax.set_xlabel('Año', fontsize=15)
ax.set_title('Producción de gas en México', fontsize=15)

y_offset = -15

for bar in ax.patches:
  ax.text(
      # Put the text in the middle of each bar. get_x returns the start
      # so we add half the width to get to the middle.
      bar.get_x() + bar.get_width() / 2,
      # Vertically, add the height of the bar to the start of the bar,
      # along with the offset.
      bar.get_height() + bar.get_y() + y_offset,
      # This is actual value we'll show.
      round(bar.get_height()),
      # Center the labels and style them a bit.
      ha='center',
      color='black',
      # weight='bold',
      size=7
  )

ax.legend()
# plt.show()
#-------------------------------------------------------------------------------------------------

agno_reservas = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
reservas_petroleo_1p = np.array([24631, 23660, 22419, 15124, 14120, 12882, 11814, 11048, 10501, 10404, 10420, 10161, 10025, 10073, 9812, 9711, 7641, 7037, 6464, 6065, 6346, 6119])
reservas_petroleo_2p = np.array([9035, 8982, 8930, 12531, 11814, 11621, 11644, 11034, 10819, 10376, 10021, 10736, 8548, 8457, 7800, 6764, 5632, 5813, 5817, 5879, 5755, 5350])
reservas_petroleo_3p = np.array([7829, 7275, 6937, 8611, 8455, 8809, 9635, 9827, 9891, 10150, 10057, 9662, 12039, 12286, 11715, 9350, 6182, 7121, 7139, 7101, 5624, 5649])

fig, ax = plt.subplots(1, figsize=(10, 5))

ax.bar(agno_reservas, reservas_petroleo_1p, label = 'Probadas (1p)', color = '#c70039', width = 0.8)
ax.bar(agno_reservas, reservas_petroleo_2p, bottom = reservas_petroleo_1p, label = 'Probables (2p)', color = '#ff5733', width = 0.8)
ax.bar(agno_reservas, reservas_petroleo_3p, bottom = reservas_petroleo_1p + reservas_petroleo_2p, label = 'Posibles (3p)', color = '#ffc30f', width = 0.8)

ax.set_ylabel('Millones de barriles', fontsize=15)
ax.set_xlabel('Año', fontsize=15)
ax.set_title('Reservas de petróleo en México', fontsize=15)

y_offset = -15

for bar in ax.patches:
  ax.text(
      # Put the text in the middle of each bar. get_x returns the start
      # so we add half the width to get to the middle.
      bar.get_x() + bar.get_width() / 2,
      # Vertically, add the height of the bar to the start of the bar,
      # along with the offset.
      bar.get_height() + bar.get_y() + y_offset,
      # This is actual value we'll show.
      round(bar.get_height()),
      # Center the labels and style them a bit.
      ha='center',
      color='black',
      # weight='bold',
      size=7
  )

ax.legend()
#-------------------------------------------------------------------------------------------------

agno_reservas = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
reservas_gas_1p = np.array([43168, 41383, 38950, 21626, 20740, 20433, 19957, 18957, 18077, 17649, 16815, 17316, 17225, 17075, 16549, 15290, 12651, 10402, 10022, 9654, 9285, 9980])
reservas_gas_2p = np.array([14885, 15309, 13857, 22071, 20474, 20703, 20087, 20486, 20562, 20110, 20694, 20905, 17613, 17827, 16716, 15316, 9375, 8899, 9355, 11170, 11654, 10410])
reservas_gas_3p = np.array([20234, 19743, 16299, 21736, 22679, 22743, 22311, 23602, 22720, 22614, 23727, 23053, 26804, 28327, 26401, 24283, 10542, 9649, 10642, 11543, 8763, 10373])

fig, ax = plt.subplots(1, figsize=(10, 5))

ax.bar(agno_reservas, reservas_gas_1p, label = 'Probadas (1p)', color = '#c70039', width = 0.8)
ax.bar(agno_reservas, reservas_gas_2p, bottom = reservas_gas_1p, label = 'Probables (2p)', color = '#ff5733', width = 0.8)
ax.bar(agno_reservas, reservas_gas_3p, bottom = reservas_gas_1p + reservas_gas_2p, label = 'Posibles (3p)', color = '#ffc30f', width = 0.8)

ax.set_ylabel('Miles de millones de pies cúbicos', fontsize=15)
ax.set_xlabel('Año', fontsize=15)
ax.set_title('Reservas de gas en México', fontsize=15)

y_offset = -15

for bar in ax.patches:
  ax.text(
      # Put the text in the middle of each bar. get_x returns the start
      # so we add half the width to get to the middle.
      bar.get_x() + bar.get_width() / 2,
      # Vertically, add the height of the bar to the start of the bar,
      # along with the offset.
      bar.get_height() + bar.get_y() + y_offset,
      # This is actual value we'll show.
      round(bar.get_height()),
      # Center the labels and style them a bit.
      ha='center',
      color='black',
      # weight='bold',
      size=7
  )

ax.legend()
#-------------------------------------------------------------------------------------------------

agno_perf = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
num_pozos_desarrollo = np.array([396, 565, 634, 694, 621, 579, 755, 1447, 976, 977, 1258, 678, 526, 279, 105, 62, 153, 234, 153, 36])
num_pozos_exploratorios = np.array([57, 98, 108, 70, 64, 48, 65, 65, 40, 30, 32, 39, 20, 24, 23, 35, 26, 39, 33, 16])

fig, ax = plt.subplots(1, figsize=(10, 5))

ax.bar(agno_perf, num_pozos_desarrollo, label = 'Pozos de desarrollo', color = '#ff5733', width = 0.8)
ax.bar(agno_perf, num_pozos_exploratorios, bottom = num_pozos_desarrollo, label = 'Pozos exploratorios', color = '#ffc30f', width = 0.8)

ax.set_ylabel('Número de pozos', fontsize=15)
ax.set_xlabel('Año', fontsize=15)
ax.set_title('Pozos perforados en México', fontsize=15)

ax2 = plt.twinx()
ax2.set_ylabel("Precio del barril - usd/barril", fontsize=15)
plt.plot(agno_prod, oil_price, marker = 'o')

y_offset = -15

for bar in ax.patches:
  ax.text(
      # Put the text in the middle of each bar. get_x returns the start
      # so we add half the width to get to the middle.
      bar.get_x() + bar.get_width() / 2,
      # Vertically, add the height of the bar to the start of the bar,
      # along with the offset.
      bar.get_height() + bar.get_y() + y_offset,
      # This is actual value we'll show.
      round(bar.get_height()),
      # Center the labels and style them a bit.
      ha='center',
      color='black',
      # weight='bold',
      size=7
  )

ax.legend()

plt.show()