# kafka-shrink-scripts
scripts used to shrink kafka cluster

# 使用方法

详细内容请参考文章：https://iamabug.github.io/2020/08/03/kafka-cluster-shrink/

使用方法如下：

1. 每次移除一个broker之前，修改 `common.sh` 和 `4_generate_reassignment.py` 中的变量，`common.sh` 需要修改的变量如下：

   ```bash
   # kafka使用的Zookeeper地址
   ZK_HOSTS="localhost:2181"
   # kafka脚本的路径，如果已经添加到PATH中，可以直接写脚本名
   TOPIC_SCRIPT="kafka-topics"
   REASSIGN_SCRIPT="kafka-reassign-partitions"
   # 不会被移除的broker的id列表
   BROKER_LIST="1001,1002,1003,1004"
   ```

   `4_generate_reassignment.py` 需要修改的变量如下：

   ```python
   # 1005 是待移除broker的id
   BROKER_ID = 1005
   # 1001，1002，1003，1004是不会被移除的broker的id列表
   BROKER_IDS = [1001, 1002, 1003, 1004]
   ```

2. 执行 `1_list_topics.sh` ，将输出中的topic列表保存在 `topics.txt` 中；

3. 执行 `2_txt2json.py` ，将 `topics.txt` 转化为 `topics.json`；

4. 执行 `3_get_current_assignment.sh`，获取当前的分区分配方案，将其保存在 `current.json`中，输出的格式如下：

   ```bash
   Current partition replica assignment
   // 中间的内容就是当前的分区分配方案
   Proposed partition reassignment configuration
   ```

5. 执行 `4_generate_reassignment.py`，生成分区重分配方案，保存在 `reassigned.json`；

6. 执行 `5_execute_reassignment.sh`，执行分区重分配，耗时较长

7. 完成后用 `6_verify.sh` 验证。

