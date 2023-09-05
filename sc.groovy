
import groovy.yaml.YamlSlurper

def tg = "/home/vagrant/activejenkins/bsmx-ansible-inventory/inventories/qa/group_vars/all/jenkins_jobs_deployments.yml"

def yml = new YamlSlurper().parse( tg as File)

def deployment_group = yml.jenkins_deploy_jobs.find {it.value = 'Portal'}.deployment_group





// example.each { println it }



//println list

// def JOB_NAME= "portal-service"
// def list = ['/bin/sh', '-c', "sed -n ' /\\["+JOB_NAME+"]/ , /\\[/ {/\\[/!p} ' /home/vagrant/activejenkins/hosts.ini"]
// list= list.execute().text.split('\n');




// println (list.flatten())

// def list = ['/bin/sh', '-c', "sed -n ' /\\[portal-service]/ , /\\[/ {/\\[/!p} '  /home/vagrant/activejenkins/hosts.in"]
// list= list.execute().text.split('\n'); 
