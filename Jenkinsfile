
@Library('mende-library')_

import static org.mende.libs.utils.*

def GIT_REPO= 'hudsonmx-portal'
props( GIT_REPO )
 
pipeline {
    agent any

    parameters{
      string(name: 'FROM_BRANCH', defaultValue: 'master')
      choice(name: 'JDK', choices: ['jdk17'], description: 'Choose the JDK version')
      booleanParam(name: 'SONAR_SCAN_ONLY', defaultValue: false, description: 'Only run the SonarQube scan')
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
                echo "post steps"
                echo "${params.Deploy}"
                if (params.Deploy == 'qa' || params.Deploy == 'qa-us' ){

                    def REPO = (params.Deploy == "qa") ? 'maven-snapshots' : 'maven-false'
                    echo "deploy target = ${DEPLOY_TARGET}"
                    echo "build job: Deploy-Job, parameters: [ extendedChoice(name: 'DEPLOY_TARGET', value:  ${DEPLOY_TARGET}), string(name: 'SERVICE_LIST_CONFIG_FILE_BRANCH', value: ${FROM_BRANCH}),hidden(name: 'VERSION', value: ARTIFACT_VERSION), hidden(name: 'REPO', value: ${REPO}),string(name: 'SYSTEMD_UPDATE', value: 'true'),  string(name: 'ROLLING_DEPLOYMENT', value: 'true') ]"
                                   
                    // jobName = params.Deploy.toUpperCase()+ "-Deploy-" + GIT_REPO.substring(9).split('-').collect {it.capitalize()}.join("-")
                    // echo "${jobName}"
                    // build job: "Deploy-Job",
                    //     parameters: [
                    //     extendedChoice(name: 'DEPLOY_TARGET', value:  "${DEPLOY_TARGET}"),
                    //     string(name: 'SERVICE_LIST_CONFIG_FILE_BRANCH', value: "${FROM_BRANCH}"),
                    //     hidden(name: 'VERSION', value: "ARTIFACT_VERSION"),            
                    //     hidden(name: 'REPO', value: (FROM_BRANCH == "qa") ? 'maven-snapshots' : 'maven-false'),
                    //     string(name: 'SYSTEMD_UPDATE', value: 'true'),
                    //     string(name: 'ROLLING_DEPLOYMENT', value: 'true')            
                    //     ]

                    deployJobMethod( this, GIT_REPO, artifactType = 'jar' )
        

                }
            }
        }
      
    }
}
