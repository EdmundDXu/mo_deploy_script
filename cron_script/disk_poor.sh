#!/bin/bash
#

function disk_poor(){
    if [ $# -lt 1 ]; then
	echo "Usage: disk_poor DISK"
	exit -1
    fi
    
    for ((i=1;i<=$#;i++)); do
    	Disk=${!i}
    	Space=`sudo df -l ${Disk} | tail -1 | awk '{print $4;}'`
		Space=`echo "${Space}/1048576" | bc`
        MountPoint=`sudo df -h ${Disk} | tail -1 | awk '{print $6;}'`
	
    	if [ `echo "${Space}<5" | bc` -eq 1 ]; then
	    Content="${Content}\n${Disk} mount on ${MountPoint} remains ${Space} G!"
    	else
	    echo "remain ${Space} G" &> /dev/null
    	fi
    done

    if [ ! -z "${Content}" ]; then
	mailx -v -s 'mo disk space warning' edmunddxu@outlook.com c.lee@livemail.tw &> /dev/null << EOF
`echo -e ${Content}`
EOF
    fi
#    echo -e ${Content}
}
disk_poor /dev/nvme0n1p2 /dev/nvme0n1p5 /dev/vdb1 /dev/mapper/docker_VG-docker_LV /dev/vda2

