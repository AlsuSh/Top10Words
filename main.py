# from pprint import pprint
import json
import xml.etree.ElementTree as ET


# def sortByLenght(InputStr):
# return len(InputStr)

# titles.sort(key = sortByLenght, reverse = True)
def processing_list(titles):
    titles_dict = dict()
    for title in set(titles):
        if len(title) > 6:
            titles_dict[title] = titles.count(title)

    titles_1_dict = dict()
    for title in titles_dict:
        if titles_dict[title] not in titles_1_dict.keys():
            titles_1_dict[titles_dict[title]] = list()
        titles_1_dict[titles_dict[title]].append({title})

    titles_list_sort = sorted(titles_1_dict.keys(), reverse=True)

    top_worlds = []
    for x in titles_list_sort:
        for x1 in titles_1_dict[x]:
            top_worlds.append(x1)
    return top_worlds[:10]


print("Информация по xml:")
with open("newsafr.xml", encoding='utf8') as f:
    xml = f.read()
    tree = ET.XML(xml)
    titles = []
    xml_items = tree.findall("channel/item")
    for item in xml_items:
       title = item.find("description")
       titles += title.text.split(" ")
    result = processing_list(titles)
    print(result)
#
print("Информация по json:")
with open("newsafr.json", encoding="utf8") as datafile:
    json_data = json.load(datafile)
    titles = []
    json_items = json_data["rss"]["channel"]["items"]
    for item in json_items:
        title = item["description"]
        titles += title.split(" ")
    result = processing_list(titles)
    print(result)