source ./common.sh

${REASSIGN_SCRIPT} --zookeeper ${ZK_HOSTS} --reassignment-json-file reassigned.json --execute
