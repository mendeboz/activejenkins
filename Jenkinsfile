
@Library('mende-library')_

props()

def deployment_group = 'test this'


pipeline {
    agent any
    parameters {
         string(name: 'DEPLOY_ENV', defaultValue: 'staging', description: '')
    }
    environment{
        target_hosts = "portal-service"
    }

    stages {
        
        stage('build') {
            steps {
                echo "parentJob"
                echo "${JOB_NAME}"

                sh 'pwd'
                 echo "currentBuild.result   ----   ${currentBuild.result}"
                    echo "currentBuild.currentResult    -----   ${currentBuild.currentResult}"
                    echo "stage results ---- ${currentBuild}"
                    echo "${target_hosts}"
                
                

            }
        }
        stage ('test library') {
            steps{
                sayHello "mende bozhinovski"
                
            }
        }
    }
    post {
      success {
        // One or more steps need to be included within each condition's block.
            
            script {
                
                if (params.Deploy == 'YES' ){
                    build job: "Deploy-Job", parameters: [ string(name: 'DeployTarget', value: "${DeployTarget}")], waitForStart: true
                    echo "current build is : ${currentBuild.result}"
                    echo "${DeployTarget}"
                }
            }
        }
      
    }
}
