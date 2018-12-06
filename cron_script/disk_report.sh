#!/bin/bash
#
function disk_report(){

	for ((i=1;i<=$#;i++)); do
    	Disk=${!i}
    	Space=`sudo df -h ${Disk} | tail -1 | awk '{print $4;}'`
    	MountPoint=`sudo df -h ${Disk} | tail -1 | awk '{print $6;}'`
    	Content="${Content}\n${Disk} mount on ${MountPoint} remains ${Space}!"
	done

	mailx -v -s 'disk space report' edmunddxu@outlook.com c.lee@livemail.tw << EOF
	`echo -e ${Content}`
EOF
}

disk_report /dev/nvme0n1p5 /dev/nvme0n1p2 /dev/vdb1 /dev/mapper/docker_VG-docker_LV /dev/vda2
