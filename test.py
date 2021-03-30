import json
import yaml

sample = {'linux': {'id': '<id>', 'update': ['update linux', 'sudo apt-get update']}, 'network': {'id': '<id>', 'update': ['update linux', 'sudo apt-get update']}}

json_obj = json.dumps(sample)
print('json_obj =', json_obj)

ff = open("data.yml", "w")
yaml.dump(sample, ff, default_flow_style=False)

# ydump = yaml.dump(sample, default_flow_style=False)
# print('ydump=',ydump)