
@Library('mende-library')_

def GIT_REPO= 'portal'
props()
 
pipeline {
    agent any

    parameters{
      string(name: 'FROM_BRANCH_test', defaultValue: 'DV-16281-extend-eks-jenkins-build-jobs-t')
      choice(name: 'JDK', choices: ['jdk17'], description: 'Choose the JDK version')
      booleanParam(name: 'SONAR_SCAN_ONLY_test', defaultValue: false, description: 'Only run the SonarQube scan')
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
                echo "post steps"
                if (params.Deploy == 'qa' || params.Deploy == 'qa-us' ){
                    echo "build job: Deploy-Job, parameters: [ string(name: DeployTarget, value: ${DEPLOY_TARGET})], waitForStart: true"
                    build job: "Deploy-Job", parameters: [ string(name: 'DeployTarget', value: "${DEPLOY_TARGET}")], waitForStart: true
                }
            }
        }
      
    }
}
