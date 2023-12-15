
import groovy.yaml.YamlSlurper



def tg = "/home/vagrant/activejenkins/bsmx-ansible-inventory/inventories/qa/group_vars/all/jenkins_jobs_deployments.yml"

def yml = new YamlSlurper().parse( tg as File)
//println yml.jenkins_deploy_jobs.each { it.name }
// def t =  yml.jenkins_deploy_jobs.find { it.bitbucket_repo?.toLowerCase()?.contains( 'hudsonmx-group-owner' )}?.deployment_group 


 def qa_deployment_group = yml.jenkins_deploy_jobs.findAll { it.bitbucket_repo?.toLowerCase()?.contains( 'hudsonmx-fe' ) }?.deployment_group

println qa_deployment_group
qa_deployment_group.each {
    println "${it}"
    def list = ['/bin/sh', '-c', "sed -n ' /\\[${it}]/ , /\\[/ {/\\[/!p} ' /home/vagrant/activejenkins/bsmx-ansible-inventory/inventories/qa/hosts.ini"]
     //['/bin/sh', '-c', "sed -n ' /\\["+JOB_NAME+"]/ , /\\[/ {/\\[/!p} ' /home/vagrant/activejenkins/hosts.ini"]
            list = list.execute().text.split('\\n');
            println list.flatten()

}


// yml.jenkins_deploy_jobs.each { println it.bitbucket_repo.getClass()}
//yml.jenkins_deploy_jobs.each { println "name: $it.name --- deployment_group: $it.deployment_group  --- repo: $it.bitbucket_repo "}

// mymap.find{ // "it" is the default parameter
//   if (it.key != "likes") return false
//   println "x value: ${it.value}" 
//   return true // stop searching
// }
// Or with explicit parameters:

// mymap.find{ key,value ->
//   (key != "likes")  return false
//   println "x value: ${value}" 
// //   return true // stop searching
// }


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
