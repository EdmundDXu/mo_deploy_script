#!/bin/bash
#
PODS_NUM=`kubectl get pods --all-namespaces -l app=jupyterhub | wc -l`
if [ ${PODS_NUM} -gt 90 ]; then
	mailx -v -s 'pods over 130 warning' edmunddxu@outlook.com c.lee@livemail.tw << EOF
        `echo -e production has ${PODS_NUM} pods, start clean old pods`
EOF
	/home/admin/.virtualenvs/moenv/bin/python /home/admin/www/mo_prod/pyserver/kube_job_cleaner_trigger.py
    /home/admin/script/cron_script/kube_pods_cleaner.sh
fi
