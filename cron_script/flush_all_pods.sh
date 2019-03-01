#!/bin/bash
#
for pods in `kubectl get pods -l app=jupyterhub -o name`; do
    kubectl delete ${pods} &
done

while true; do
    PROCESS_NUM=`ps aux | grep "kubectl delete" | wc -l`
    if [ ${PROCESS_NUM} -le 1 ]; then
        break
    else
        echo "remain process ${PROCESS_NUM}"
        sleep 5
    fi
done
