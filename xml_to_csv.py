import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
 
# <?xml version="1.0" ?>
# <annotation>
#
# <folder>widerface</folder>
# <filename>000022.png</filename>
#
# <source>
# <database>wider face Database</database>
# <annotation>PASCAL VOC2007</annotation>
# <image>flickr</image>
# <flickrid>-1</flickrid>
# </source>
#
# <owner>
# <flickrid>yanyu</flickrid>
# <name>yanyu</name>
# </owner>
#
# <size>
# <width>1242</width>
# <height>375</height>
# <depth>3</depth>
# </size>
#
# <segmented>0</segmented>
#
# <object>
# <name>Car</name>
# <pose>Unspecified</pose>
# <truncated>1</truncated>
# <difficult>0</difficult>
# <bndbox>
# <xmin>128</xmin>
# <ymin>199</ymin>
# <xmax>218</xmax>
# <ymax>237</ymax>
# </bndbox>
# </object>
#
# <object>
# <name>Car</name>
# <pose>Unspecified</pose>
# <truncated>1</truncated>
# <difficult>0</difficult>
# <bndbox>
# <xmin>60</xmin>
# <ymin>198</ymin>
# <xmax>159</xmax>
# <ymax>238</ymax>
# </bndbox>
# </object>
#
# </annotation>
def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            try:
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
            except ValueError:
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][1][0].text),
                         int(member[4][1][1].text),
                         int(member[4][1][2].text),
                         int(member[4][1][3].text)
                         )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df
 
 
def main():
    image_path = os.path.join(os.getcwd(), 'train_annotations')
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('train_labels.csv', index=None)
    print('Successfully converted xml to csv.')
 
 
main()
