import os
import signal
from flask import Flask
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += "<hr>"
    page += "Fuck yeah!! it works!!"
    page += "<hr>"
    page += "<h2>My key skills are:</h2>"
    page += "<ul>"
    page += """
    <li> <b>DevOps:</b> Ansible, Docker, Jenkins, Consul, Capistrano, Travis - CI, git, bash / python
    scripting etc.
    <li> <b>HighLoad:</b> Nginx, Linux load balancing(LVS), VRRP, HaProxy, memcache, mcrouter, redis, rabbit - mq. 
    <li> <b>Linux:</b> big experience in Debian based distributives.
    <li> <b>Virtualization:</b> ESXi, ProxmoxVE: HA - clusters, Ceph, GlusterFS, iSCSI etc.
    <li> <b>networks:</b> Junuper MX, Cisco routers and switches, VyOS(Vyatta, Ubiquiti EdgeMAX), Mikrotik, PfSence, OPNsense | OSPF, BGP, tunnels, firewalls etc.
    <li> Python (Django / Scrappy)
    <li> Zabbix, Grafana, TICK
    <li> stack(Telegraf, Chronograf, InfluxDB, Kapacitor), collectD, fluendD
    <li> <b>Databases:</b> Mysql / MariaDB( with replication), InfluxDB, Cassandra, Yandex Clickhouse.
    """
    page += "</ul>"
    page += "<hr>"
    page += "<h2>my profile below:</h2>"
    page += "<a href 'https://www.upwork.com/freelancers/~01a6738208d8e81707'>Hire me<hr>"

    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default


