from marathon.models import MarathonApp, MarathonTask
from marathon.models.container import *


def marathon_discover_list_apps():
  return [
    MarathonApp(id='/test/sample', labels={'_tonomi_environment': 'test',
                                           '_tonomi_application': 'sample'}),
    MarathonApp(id='/sandbox/sample', labels={'_tonomi_environment': 'sandbox',
                                              '_tonomi_application': 'sample'}),
    MarathonApp(id='/sandbox/sample2', labels={'_tonomi_application': 'sample'})
  ]

def webui_launch_get_app():
  app1 = MarathonApp(id='/sandbox/cassandra-seed', tasks=[MarathonTask(host='127.0.0.1')],
                     labels={'_cql_native_port': '31942'})
  return [app1]

def cassandra_launch_get_app():
  app1 = MarathonApp(id='/sandbox/cassandra-seed', tasks=[MarathonTask(host='127.0.0.1')])
  return [app1]

def redis_launch_get_app():
  app1 = MarathonApp(id='/sandbox/redis-master', tasks=[MarathonTask(host='127.0.0.0')])
  return [app1]

def cassandra_health_check_list_apps():
  app1 = MarathonApp(id='/sandbox/cassandra-seed')
  app2 = MarathonApp(id='/test/non-env-seed')
  app3 = MarathonApp(id='/sandbox/cassandra-node')
  return [app1, app2, app3]

def redis_health_check_list_apps():
  app1 = MarathonApp(id='/sandbox/redis-slave')
  app2 = MarathonApp(id='/sandbox/redis-master')
  app3 = MarathonApp(id='/test/non-env-redis')
  return [app1, app2, app3]

def cassandra_health_check_get_app():
  labels = {
    '_jmx_port': '123',
    '_internode_communication_port': '123',
    '_tls_internode_communication_port': '123',
    '_thrift_client_port': '123',
    '_cql_native_port': '123'
  }
  app1 = MarathonApp(id='/sandbox/cassandra-seed', labels=labels,
                     tasks_unhealthy=0, tasks_running=1, mem=256, cpus=0.5, disk=256)
  app2 = MarathonApp(id='/test/non-env-cassandra', labels=labels,
                     tasks_unhealthy=0, tasks_running=1, mem=256, cpus=0.5, disk=256)
  return [app1, app2]

def redis_health_check_get_app():
  app1 = MarathonApp(id='/sandbox/redis-master', tasks=[MarathonTask(host='127.0.0.1')],
                     tasks_unhealthy=0, tasks_running=1, mem=256, cpus=0.5, disk=256)

  app2 = MarathonApp(id='/sandbox/redis-slave', tasks=[MarathonTask(host='127.0.0.1')],
                     cmd='docker-entrypoint.sh redis-server --port $REDIS_PORT --slaveof 127.0.0.1 $REDIS_PORT',
                     tasks_running=1, mem=256, cpus=0.5, disk=256)
  return [app1, app2]

def cassandra_discover_list_apps():
  return [
    MarathonApp(id='/debug/cassandra-seed', labels={'_tonomi_environment': 'debug'}),
    MarathonApp(id='/sandbox/cassandra-seed', labels={'_tonomi_environment': 'sandbox',
                                                      '_tonomi_application': 'cassandra'}),
    MarathonApp(id='/sandbox/cassandra-node', labels={'_tonomi_environment': 'sandbox',
                                                      '_tonomi_application': 'cassandra'}),
    MarathonApp(id='/test/non-env-cassandra', labels={'_tonomi_environment': 'test',
                                                      '_tonomi_application': 'cassandra'})
  ]

def kafka_discover_list_apps():
  return [
    MarathonApp(id='/sandbox/kafka', labels={'_tonomi_environment': 'sandbox',
                                             '_tonomi_application': 'kafka'}),
    MarathonApp(id='/test/kafka')
  ]

def redis_discover_list_apps():
  return [
    MarathonApp(id='/sandbox/redis-master', labels={'_tonomi_environment': 'sandbox',
                                                    '_tonomi_application': 'redis'}),
    MarathonApp(id='/test/redis-master'),
    MarathonApp(id='/sandbox/redis-slave', labels={'_tonomi_environment': 'sandbox',
                                                   '_tonomi_application': 'redis'})
  ]

def webui_discover_list_apps():
  return [
    MarathonApp(id='/sandbox/webui', labels={'_tonomi_environment': 'sandbox',
                                             '_tonomi_application': 'webui'}),
    MarathonApp(id='/test/webui', labels={'_tonomi_environment': 'test',
                                          '_tonomi_application': 'webui'})
  ]

def webui_health_check_get_app():
  marathon_apps = []

  port_mappings = [MarathonContainerPortMapping(service_port=1000)]
  docker = MarathonDockerContainer(image='node', port_mappings=port_mappings)
  container = MarathonContainer(docker=docker)
  labels = {'_tonomi_environment': 'sandbox', '_tonomi_application': 'webui'}
  app1 = MarathonApp(id='/sandbox/webui', labels=labels, cpus=0.5, mem=256, disk=256, instances=1, container=container)
  app1.tasks_unhealthy = 0
  app1.tasks_running = 1

  marathon_apps.append(app1)

  return marathon_apps


def marathon_health_check_get_app():
  marathon_apps = []

  docker = MarathonDockerContainer(image='image')
  container = MarathonContainer(docker=docker)
  app1 = MarathonApp(id='/sandbox/sample', labels={}, cpus=0.5, mem=256, disk=256, instances=1, container=container)
  app1.tasks_unhealthy = 0

  marathon_apps.append(app1)

  return marathon_apps