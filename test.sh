#!/bin/bash

echo "=== 將目前執行 process 的 PID 依照數字大小排序，取出前 10 名 === "
ps | awk '{print $1}' | sort -rn | head -10

result=`expr 10 + 2`

# 12
echo "Result: $result"
