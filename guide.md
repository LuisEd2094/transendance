[ELK getting started](https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose/)
[Kibana API](https://www.elastic.co/guide/en/kibana/current/saved-objects-api.html)
[Elastic Index Policy](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html)

[Prometheus Django](https://github.com/korfuri/django-prometheus)
[Prometheus docker](https://docs.docker.com/config/daemon/prometheus/)
[Prometheus your own metrics](https://www.monterail.com/blog/prometheus-custom-metrics)

[Grafana Provisions](https://grafana.com/docs/grafana/latest/administration/provisioning/)
[Grafana contact points and rules](https://grafana.com/docs/grafana/latest/developers/http_api/alerting_provisioning/)
Grafana
To get jsonfile for a created dashboard, get UID from the URL and then call this address

curl -u "admin:newadmin" -X GET http://localhost:3000/api/dashboards/uid/${UID} -o new_dashboard.json