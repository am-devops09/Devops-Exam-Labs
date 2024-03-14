# " #!/bin/bash "
    # - " for i in `find /var/log -maxdepth 1 -type f -name '*.log'`; do echo $i; aws s3 cp $i s3://devopsflow101-logs/; done "
    # - " aws autoscaling complete-lifecycle-action --lifecycle-action-result CONTINUE --instance-id {{ instanceid }} --lifecycle-hook-name {{ hookname }} --auto-scaling-group-name {{ asgname }} "


#!/bin/bash
for i in `find /var/log -name '*.log'`;
do
    echo $i;
    aws s3 cp $i s3://devopsflow101-logs/;
done