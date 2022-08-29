#!/bin/bash

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
sed "$!N;s/Automated UI tests/Automated UI tests - $current_time/;P;D" testrail-ui.cfg >testrail-custom-ui.cfg
#TEST_PLAN_INFO=$(
#  curl -H "Content-Type: application/json" \
#  -u "artur.popko@gmail.com:Stalker82!" \
#  "https://arthur82.testrail.io/index.php?/api/v2/add_plan/1" \
#  -d "{ \"name\": \"Automated UI tests - $current_time\", \"entries\": [{ \"suite_id\": 1, \"name\": \"Test Suite\", \"assignedto_id\": 1}]}"
#)
#dest_dir=./tmp_test_plan.json

#echo "$TEST_PLAN_INFO" >"$dest_dir"

