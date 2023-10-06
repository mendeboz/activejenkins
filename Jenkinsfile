
@Library('mende-library')_

    println ("this is it " + this.env.GIT_REPO)
    println params.getClass()
    println params.each {it}
     node {

        def tg = "/home/vagrant/activejenkins/bsmx-ansible-inventory/inventories/qa/group_vars/all/jenkins_jobs_deployments.yml"

        def read = readYaml file: tg

        println tg

        def deployment_qa_group = read.jenkins_deploy_jobs.find { it.bitbucket_repo?.toLowerCase()?.contains( 'portal' ) }.deployment_group

        println "deployment_qa_group="+deployment_qa_group 

        def tgus = "/home/vagrant/activejenkins/bsmx-ansible-inventory/inventories/qa-us/group_vars/all/jenkins_jobs_deployments.yml"

        def readus = readYaml file: tgus

        def deployment_qa_us_group = readus.jenkins_deploy_jobs.find {it.bitbucket_repo?.toLowerCase()?.contains( 'portal' )}.deployment_group

        println "deployment_qa_us_group="+deployment_qa_us_group
    

    properties([
        parameters([
            [
                $class: 'ChoiceParameter', 
                choiceType: 'PT_SINGLE_SELECT',               
                name: 'Deploy', 
                script: [
                    $class: 'GroovyScript', 
                    fallbackScript: [classpath: [], sandbox: false, script: 'return ["ERROR"]'], 
                    script: [classpath: [], 
                            sandbox: false,
                            script:  
    """
    return ["Select:selected","qa","qa-us"]
    """
                ]
            ]
        ],        
        [
            $class: 'CascadeChoiceParameter', 
            choiceType: 'PT_CHECKBOX',
            description: 'description',
            name: 'DEPLOY_TARGET', 
            referencedParameters: 'Deploy', 
            filterable: false,
            script: [
                $class: 'GroovyScript', 
                fallbackScript: [classpath: [], sandbox: false, script: "return ['error']"], 
                script: [classpath: [], 
                sandbox: false, 
                script: 
    """

    if (Deploy.equals('qa')){
        def list = ['/bin/sh', '-c', "sed -n \' /\\\\[${deployment_qa_group}]/ , /\\\\[/ {/\\\\[/!p} \'  /home/vagrant/activejenkins/bsmx-ansible-inventory/inventories/qa/hosts.ini"]
        list = list.execute().text.split('\\n');
        return list.flatten()
    }else if (Deploy.equals('qa-us')){
        def list = ['/bin/sh', '-c', "sed -n \' /\\\\[${deployment_qa_us_group}]/ , /\\\\[/ {/\\\\[/!p} \'  /home/vagrant/activejenkins/bsmx-ansible-inventory/inventories/qa-us/hosts.ini"]
        list = list.execute().text.split('\\n');
        return list.flatten()
    }else{
        return [ 'deployment_group' ]
    }

    """
                ]
            ]
        ] 

        ] )
    ])
     }

pipeline {
    agent any

    parameters{
      string(name: 'FROM_BRANCH', defaultValue: 'DV-16281-extend-eks-jenkins-build-jobs-t')
      choice(name: 'JDK', choices: ['jdk17'], description: 'Choose the JDK version')
      booleanParam(name: 'SONAR_SCAN_ONLY', defaultValue: false, description: 'Only run the SonarQube scan')
  }
    
    environment{
        GIT_REPO = 'hudsonmx-portal'
    }

    stages {
        stage ('test library') {
            steps{
                script{
                    // props()
        //             //sayHello ("mende bozhinovski")
                    echo env.GIT_REPO
        //             //pp()
                }
                
            }
        }
    }

    post {
      success {
        // One or more steps need to be included within each condition's block.
            
            script {
                
                if (params.Deploy == 'qa' || params.Deploy == 'qa-us' ){
                    build job: "Deploy-Job", parameters: [ string(name: 'DeployTarget', value: "${DEPLOY_TARGET}")], waitForStart: true
                }
            }
        }
      
    }
}
