#!/bin/bash
#it only replaces the value inside the json file if it creates a new datasource

out=$(curl -s -u "admin:newadmin" -H 'Content-Type: application/json' grafana:3000/api/datasources -d '{
  "name":"prometheus",
  "type":"prometheus",
  "url":"http://prometheus:9090",
  "access":"proxy",
  "basicAuth":false
}' | grep '"uid":' | awk -F'"' '{print $8}')

export DATASOURCE_ID="${out}"

if [[ -n "$DATASOURCE_ID" && $(grep -q '"uid": "replace"' /gateway_dashboard.json; echo $?) -eq 0 ]]; then
    sed -i.bak "s/\"uid\": \"replace\"/\"uid\": \"$DATASOURCE_ID\"/" /gateway_dashboard.json
fi

curl -s -H "Content-Type: application/json" -u "admin:newadmin" grafana:3000/api/dashboards/db -d @/gateway_dashboard.json