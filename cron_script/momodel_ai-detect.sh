#!/bin/bash
#
BODY="$(curl -L http://momodel.ai/)"
if echo "${BODY}" | grep "momodel" &> /dev/null; then
    echo "momodel.ai ok" &> /dev/null
else
    mailx -v -s 'momodel.ai access error' edmunddxu@outlook.com c.lee@livemail.tw << EOF
`echo "http://momodel.ai/ is blocked"`
EOF

fi
