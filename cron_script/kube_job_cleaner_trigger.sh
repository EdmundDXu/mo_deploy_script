#!/bin/bash
#
PODS_NUM=`kubectl get pods --all-namespaces | wc -l`
if [ ${PODS_NUM} -gt 170 ]; then
	mailx -v -s 'pods over 80% out of 220 warning' edmunddxu@outlook.com c.lee@livemail.tw << EOF
        `echo -e production has more then ${PODS_NUM} pods, start clean old pods`
EOF
	/home/admin/.virtualenvs/moenv/bin/python /home/admin/www/mo_prod/pyserver/kube_job_cleaner_trigger.py
fi
