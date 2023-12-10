mo = 'hiddenendpass'
pozisyon_start = mo.find('hidden') + len('hidden')
pozisyon_end = mo.find('endpass')

karakte_nan_mitan = mo[pozisyon_start:pozisyon_end]
print(karakte_nan_mitan)
