#!/bin/bash
echo "xxl-job: hello shell"

echo "脚本位置：$0"
echo "参数数量：$#"
for param in $*
do
    echo "参数 : $param"
    sleep 1s
done

echo "Good bye!"
exit 0
