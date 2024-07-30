[ELK getting started](https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose/)
[Prometheus Django](https://github.com/korfuri/django-prometheus)
[Prometheus docker](https://docs.docker.com/config/daemon/prometheus/)
[Prometheus your own metrics](https://www.monterail.com/blog/prometheus-custom-metrics)


 - job_name: 'blockchain'
    scrape_interval: 5s
    static_configs:
      - targets: ['blockchain:8000']

  - job_name: 'chat'
    scrape_interval: 5s
    static_configs:
      - targets: ['chat:8000']

  - job_name: 'gamestats'
    scrape_interval: 5s
    static_configs:
      - targets: ['gamestats:8000']

  - job_name: 'twofactor'
    scrape_interval: 5s
    static_configs:
      - targets: ['twofactor:8000']

  - job_name: 'usermanagement'
    scrape_interval: 5s
    static_configs:
      - targets: ['usermanagement:8000']
