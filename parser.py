import csv, re, pprint
from place import Place

def parse(filename):
    with open(filename, "rb") as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')
        return parse_items(reader)

def parse_items(lines):
    items = []
    current_item = []
    for line in lines:
        if line[0] == "defcase":
            items.append(parse_item(current_item))
            current_item = []
        elif [i for i in line if i]:
            current_item.append(line)

    if current_item:
        items.append(parse_item(current_item))

    return items

def parse_item(lines):
    item = {}
    for line in lines:
        # Lines are csv items, we are interested in fields 1 and 2
        key,value = line[1:3]
        # The keys we need start with an uppercase letter
        if key[0].isupper():
            key = key.strip(" :")
            value = re.sub(r"([A-Z])", r" \1", value)
            value = value.strip(" .,")
            item[key] = value
    return item

if __name__ == "__main__":
    items = parse("travel-cases.csv")
    print "Parsed %d items" % len(items)
    min_price = max_price = int(items[0]['Price'])
    min_people = max_people = int(items[0]['NumberOfPersons'])
    min_duration = max_duration = int(items[0]['Duration'])

    from case import Case
    c = Case()
    for key,value in items[0].items():
        c[key] = value
    print c

    for item in items:
        price = int(item["Price"])
        people = int(item['NumberOfPersons'])
        duration = int(item['Duration'])
        max_price = max([max_price, price])
        min_price = min([min_price, price])
        max_people = max([max_people, people])
        min_people = min([min_people, people])
        max_duration = max([max_duration, duration])
        min_duration = min([min_duration, duration])

    print "Price: %f-%f, %f" % (min_price, max_price, max_price-min_price)
    print "People: %f-%f, %f" % (min_people, max_people, max_people-min_people)
    print "Duration: %f-%f, %f" % (min_duration, max_duration, max_duration-min_duration)
    print "Accommodation:", sorted(list(set([i['Accommodation'] for i in items])))
    print "Transportation:", sorted(list(set([i['Transportation'] for i in items])))
    print "HolidayType:", sorted(list(set([i['HolidayType'] for i in items])))
    regions = list(set([i['Region'] for i in items]))
    regions = [(i, Place(i)) for i in regions]
    pp = pprint.PrettyPrinter(indent=4)
    print "Region:",
    pp.pprint(sorted(regions))
    max_distance = 0.0
    min_distance = 10000.0
    max_regions = []
    for region in regions:
        for other_region in regions:
            if not region==other_region:
                distance = region[1].distance(other_region[1])
                min_distance = min([min_distance,distance])
                if distance > max_distance:
                    max_distance = distance
                    max_regions = [region,other_region]
    print "Distance: %f-%f, %f, %s" % (min_distance, max_distance, max_distance-min_distance, repr(max_regions))


