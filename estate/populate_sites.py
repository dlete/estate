'''
http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree/
http://www.dr-chuck.com/csev-blog/2008/09/a-simple-python-elementtree-example/
http://www.diveintopython3.net/xml.html
https://docs.python.org/2/library/xml.etree.elementtree.html

https://wiki.python.org/moin/PythonXml
https://wiki.python.org/moin/Tutorials%20on%20XML%20processing%20with%20Python
http://effbot.org/zone/element.htm#reading-and-writing-xml-files
'''

'''
import xml.etree.cElementTree as ET
tree = ET.ElementTree(file='xml_client_sites.xml')
for site in tree.iter(tag='site'):
    print site.find('parent_type').text
    print site.find('id').text
'''

import os

def populate():
    import xml.etree.cElementTree as ET
    tree = ET.ElementTree(file='xml_client_sites.xml')
    for site in tree.iter(tag='site'):
        id = site.find('id').text
        parent_type =  site.find('parent_type').text
        abbreviation = site.find('abbreviation').text
        name = site.find('name').text
        latitude = site.find('lat').text
        longitude = site.find('lng').text
        is_pop = site.find('is_pop').text
        active = site.find('active').text
        add_site(id, parent_type, abbreviation, name, latitude, longitude, is_pop, active)

    # print what we have added
    for site in Site.objects.all():
        print "- {0}".format(str(Site))


def add_site(id, parent_type, abbreviation, name, latitude, longitude, is_pop, active):
    site = Site.objects.get_or_create(
        id = id,
        parent_type = parent_type,
        abbreviation = abbreviation,
        name = name,
        latitude = latitude,
        longitude = longitude,
        is_pop = is_pop,
        active = active
        )[0]
    return site


# Start execution here!
if __name__ == '__main__':
    print "Starting to populate the Site table..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate.settings')
    from support.models import Site
    populate()

