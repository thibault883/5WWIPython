def yiq(rgb):
    cijfer_1 = (0.299, 0.587, 0.114)
    cijfer_2 = (0.596, -0.274, -0.322)
    cijfer_3 = (0.211, -0.523, 0.312)
    yiq_1 = round(cijfer_1[0] * rgb[0] + cijfer_1[1] * rgb[1] + cijfer_1[2] * rgb[2], 4)
    yiq_2 = round(cijfer_2[0] * rgb[0] + cijfer_2[1] * rgb[1] + cijfer_2[2] * rgb[2], 4)
    yiq_3 = round(cijfer_3[0] * rgb[0] + cijfer_3[1] * rgb[1] + cijfer_3[2] * rgb[2], 4)

    return yiq_1, yiq_2, yiq_3

print(yiq((82, 227, 112)))
