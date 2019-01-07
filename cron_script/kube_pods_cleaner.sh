#!/bin/bash
#
fucked_member=("edmund" "zhaofengli" "luxu1220" "mengx" "magicalion" "yangsaisai" "chentiyun" "zhaojingnan" "rehearsal77")
function contains() {
	for fucked in ${fucked_member[@]}; do
		kubectl describe pods/${1} | grep "Path:.*${fucked}" && return 0
	done
	return 1
}

for i in `kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}'`; do
	if contains ${i}; then
		echo "kubectl delete pods/${i} &"
		kubectl delete pods/${i} &
		echo 
		sleep 5
	fi
done

