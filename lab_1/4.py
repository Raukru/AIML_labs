import json

with open("sales.json", "r") as read_file:
    json_data = json.load(read_file)


def json_to_csv(data):
    csv_data = "item, country, year, sales\n"
    for items in data:
        for keys in items.keys():
            for country_key in items['sales_by_country']:
                for year_key in items['sales_by_country'][country_key]:
                    csv_data += items['item'] + ", " + country_key + ", " + str(year_key) + ", " + str(items['sales_by_country'][country_key][year_key]) + "\n"
    return csv_data


with open("sales.csv", "w") as write_file:
    write_file.write(json_to_csv(json_data))