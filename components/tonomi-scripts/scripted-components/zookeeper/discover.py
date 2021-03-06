#!/usr/bin/env python3

import sys
import yaml
from lambdas import *
from models import *

args = parse_args()
manager = MarathonManager(get_marathon_url(args))
instances = {}

for instance_name in manager.discover(app_filter='zookeeper'):
  instances[instance_name] = {
    'name': instance_name,
    'interfaces': {
      'info': {
        'signals': {
          'app-id': instance_name
        }
      }
    }
  }

return_instances_info(instances)
