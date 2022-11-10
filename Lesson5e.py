

counties = ['Nairobi', 'Nakuru', 'Uasin Gishu', 'Tharaka Nithi', 'Mombasa',
            'West Pokot', 'Kiambu']

single_names = []
double_names = []
for county in counties:
    print(county)
    if ' ' in county:
        double_names.append(county)
    else:
        single_names.append(county)


print(double_names)
print(single_names)




