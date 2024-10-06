import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element('root')
    for key, value in dictionary.items():
        sub = ET.SubElement(root, key)
        sub.text = str(value)
    tree = ET.ElementTree(root)
    with open(filename, 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return data
