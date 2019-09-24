#!/bin/bash
#
BODY="$(curl -L https://momodel.cn/)"
if echo "${BODY}" | grep "momodel" &> /dev/null; then
    echo "momodel.cn ok" &> /dev/null
else
    mailx -v -s 'momodel.cn access error' c.lee@livemail.tw lzfxxx@gmail.com << EOF
`echo "https://momodel.cn/ is blocked"`
EOF

fi
