'''
http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree/
http://www.dr-chuck.com/csev-blog/2008/09/a-simple-python-elementtree-example/
http://www.diveintopython3.net/xml.html
https://docs.python.org/2/library/xml.etree.elementtree.html

https://wiki.python.org/moin/PythonXml
https://wiki.python.org/moin/Tutorials%20on%20XML%20processing%20with%20Python
http://effbot.org/zone/element.htm#reading-and-writing-xml-files
'''

import xml.etree.cElementTree as ET
tree = ET.ElementTree(file='xml_client_sites.xml')
for site in tree.iter(tag='site'):
    print site.find('parent_type').text
    print site.find('id').text
