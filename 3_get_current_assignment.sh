source ./common.sh

${REASSIGN_SCRIPT} --zookeeper ${ZK_HOSTS} --topics-to-move-json-file topics.json --broker-list ${BROKER_LIST} --generate
