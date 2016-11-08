BASE_DIR = './tonomi-scripts/scripted-components'
YAML_MESSAGES_DIR = '{}/tests/yaml_tonomi'.format(BASE_DIR)
INPUT = 'input'
OUTPUT = 'output'
HOST = 'http://localhost'

MARATHON_APP = 'marathon'
ZOOKEEPER_APP = 'zookeeper'
REDIS_APP = 'redis'
CASSANDRA_APP = 'cassandra'
KAFKA_APP = 'kafka'
WEBUI_APP = 'webui'
SPARK_APP = 'spark'
ENVIRONMENT_APP = 'isp-environment'

CREATE_SCRIPT = 'create.py'
DISCOVER_SCRIPT = 'discover.py'
HEALTH_CHECK_SCRIPT = 'healthCheck.py'
DESTROY_SCRIPT = 'destroy.py'
SCALE_SCRIPT = 'scale.py'
RESTART_SCRIPT = 'restart.py'

CREATE_ACTION = 'create'
DISCOVER_ACTION = 'discover'
HEALTH_CHECK_ACTION = 'healthCheck'
DESTROY_ACTION = 'destroy'
SCALE_ACTION = 'scale'
RESTART_ACTION = 'restart'