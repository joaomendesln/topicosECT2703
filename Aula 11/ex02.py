temp_fahr = [70, 45, 90, 63, 43]

temp_cels = [round((f - 32) * (5/9),2) for f in temp_fahr]
temp_cels_final = [c for c in temp_cels if c >= 5 and c <= 10]

print(temp_cels_final)