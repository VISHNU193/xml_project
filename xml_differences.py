import xml.etree.ElementTree as ET
import json
from dictdiffer import diff

def xml_to_dict(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    def parse_element(element):
        result = {}
        for child in element:
            child_dict = parse_element(child)
            if child_dict:
                result[child.tag] = child_dict
            else:
                result[child.tag] = child.text
        return result

    return {root.tag: parse_element(root)}

def compare_xml(xml_file1, xml_file2):
    dict1 = xml_to_dict(xml_file1)
    dict2 = xml_to_dict(xml_file2)

    differences = list(diff(dict1, dict2))
    return differences

def save_diff_as_json(differences, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(differences, json_file, indent=2)

if __name__ == "__main__":
    xml_file1 = "C:/All code/python/xml_project/first.xml"
    xml_file2 = "C:/All code/python/xml_project/second.xml"
    output_json_file = "C:/All code/python/xml_project/differences.json"

    differences = compare_xml(xml_file1, xml_file2)
    save_diff_as_json(differences, output_json_file)
