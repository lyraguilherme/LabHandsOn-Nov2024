from ncclient import manager
import xmltodict
import json
import os


username = os.getenv('LAB_USERNAME')
password = os.getenv('LAB_PASSWORD')


netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
    </interface>
  </interfaces>
</filter>
"""


device = {
    "host": "192.168.0.253",
    "port": 830,
    "username": username,
    "password": password,
    "hostkey_verify": False
}


with manager.connect(**device) as conn:
    result = conn.get_config(source='running', filter=netconf_filter)
    result_xml = result.xml
    result_dict = xmltodict.parse(result_xml)
    print(json.dumps(result_dict, indent=4))
