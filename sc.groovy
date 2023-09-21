
import groovy.yaml.YamlSlurper



def tg = "/home/vagrant/activejenkins/bsmx-ansible-inventory/inventories/qa-us/group_vars/all/jenkins_jobs_deployments.yml"

def yml = new YamlSlurper().parse( tg as File)
//println yml.jenkins_deploy_jobs.each { it.name }
println yml.jenkins_deploy_jobs.findAll { it.bitbucket_repo?.toLowerCase()?.contains( 'hudsonmx-nielsen-national-tv-query' )}.deployment_group
// yml.jenkins_deploy_jobs.each { println it.bitbucket_repo.getClass()}
//yml.jenkins_deploy_jobs.each { println "name: $it.name --- deployment_group: $it.deployment_group  --- repo: $it.bitbucket_repo "}




//def deployment_group = yml.jenkins_deploy_jobs { println it.getClass() }

//  println deployment_group.find { it=='portal'}






// example.each { println it }



//println list

// def JOB_NAME= "portal-service"
// def list = ['/bin/sh', '-c', "sed -n ' /\\["+JOB_NAME+"]/ , /\\[/ {/\\[/!p} ' /home/vagrant/activejenkins/hosts.ini"]
// list= list.execute().text.split('\n');




// println (list.flatten())

// def list = ['/bin/sh', '-c', "sed -n ' /\\[portal-service]/ , /\\[/ {/\\[/!p} '  /home/vagrant/activejenkins/hosts.in"]
// list= list.execute().text.split('\n'); 
