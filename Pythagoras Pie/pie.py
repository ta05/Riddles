def pie():
    pie = 100
    portion_of_pie = {}
    for i in range(1, 101):
        portion_of_pie[i] = pie * (i / 100)
        pie *= (100 - i) / 100
    portion_of_pie = {k: v for k, v in sorted(portion_of_pie.items(), key=lambda item: item[1], reverse=True)}
    return portion_of_pie

print(pie())