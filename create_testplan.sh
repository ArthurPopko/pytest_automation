#!/bin/bash

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
TEST_PLAN_INFO=$(
  curl -H "Content-Type: application/json" \
  -u "artur.popko@gmail.com:Stalker82!" \
  "https://arthur82.testrail.io/index.php?/api/v2/add_plan/1" \
  -d "{ \"name\": \"Automated UI tests - $current_time\", \"entries\": [{ \"suite_id\": 1, \"name\": \"Test Suite\", \"assignedto_id\": 1}]}"
)
dest_dir=./tmp_test_plan.json

echo "$TEST_PLAN_INFO" >"$dest_dir"

testplan_id=$(jq '.id' $dest_dir)
testrun_id=$(jq '.entries[0].runs[0].id' $dest_dir)

echo "API_TEST_PLAN_ID=$testplan_id"
echo "API_TEST_RUN_ID=$testrun_id"

echo "API_TEST_PLAN_ID=$testplan_id" >> .env
echo "API_TEST_RUN_ID=$testrun_id" >> .env
