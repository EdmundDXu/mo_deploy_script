#!/bin/bash
#
BODY="$(curl http://momodel.ai/)"
if echo "${BODY}" | grep "301" &> /dev/null && echo "${BODY}" | grep "nginx/1.14.2" &> /dev/null; then
    echo "momodel.ai ok"
else
    mailx -v -s 'momodel.ai access error' edmunddxu@outlook.com c.lee@livemail.tw << EOF
echo "momodel.ai is totally fucked"
EOF

fi
