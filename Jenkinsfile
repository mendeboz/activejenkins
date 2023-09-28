
@Library('mende-library')_


pipeline {
    agent any
    node{
        script {
            props()
        }
    }
    parameters {
         string(name: 'PARAM1', defaultValue: 'staging', description: '')
         string(name: 'PARAM2', defaultValue: 'staging2', description: '')
    }
    environment{
        GIT_REPO = "hudsonmx-portal"
    }
    stages {
        // stage ('test library') {
        //     steps{
        //         script{
        //             props(env.GIT_REPO)
        //             //sayHello ("mende bozhinovski")
        //             echo env.GIT_REPO
        //             //pp()
        //         }
                
        //     }
        // }
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
