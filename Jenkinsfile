
@Library('mende-library')_

//props(env.GIT_URL)

// def deployment_group = 'test this'


pipeline {
    agent any
    parameters {
         string(name: 'DEPLOY_ENV', defaultValue: 'staging', description: '')
    }
    environment{
        GIT_REPO = "hudsonmx-hazelcast-member"
    }

    stages {
        stage ('test library') {
            steps{
                script{
                    props(env.GIT_REPO)
                    //sayHello ("mende bozhinovski")

                    //pp()
                }
                
            }
        }
    }
    post {
      success {
        // One or more steps need to be included within each condition's block.
            
            script {
                
                if (params.Deploy == 'YES' ){
                    build job: "Deploy-Job", parameters: [ string(name: 'DeployTarget', value: "${DeployTarget}")], waitForStart: true
                }
            }
        }
      
    }
}
