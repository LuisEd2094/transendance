#!/bin/bash



contact_uid=$(curl -X POST \
  -H "Content-Type: application/json" \
  -u "admin:newadmin" \
  -d '{
    "name": "My Slack Contact Point",
    "type": "slack",
    "settings": {
      "url": "https://hooks.slack.com/services/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",
      "recipient": "#alerts",
      "username": "Grafana Alert",
      "icon_emoji": ":grafana:"
    }
  }' \
  http://localhost:3000/api/v1/provisioning/contact-points | grep "uid" | awk -F'"' '{print $4}')


echo constact uid ${contact_uid}




folder_id=$(curl -X POST    -H "Content-Type: application/json"   -u "admin:newadmin"   -d '{
  "uid": null,
  "title": "Department eeeeee",
  "parentUid": null
}'  http://localhost:3000/api/folders | grep "uid" | awk -F'"' '{print $6}')

echo folder id ${folder_id}

export FOLDER_ID="${folder_id}"
export CONTANT_ID="${contact_uid}"


sed -i.bak "s/\"folderUID\": \"replace\"/\"folderUID\": \"$FOLDER_ID\"/" ./alert.json

sed -i.bak "s/\"datasourceUid\": \"replace\"/\"datasourceUid\": \"$DATASOURCE_ID\"/" ./alert.json




curl -X POST \
  -H "Content-Type: application/json" \
  -u "admin:newadmin" \
  -d  @./alert.json \
  http://localhost:3000/api/v1/provisioning/alert-rules
