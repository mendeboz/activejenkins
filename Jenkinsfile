
@Library('mende-library')_

properties([
  parameters([
    [
        $class: 'ChoiceParameter',
        choiceType: 'PT_SINGLE_SELECT',
        name: 'testmende',
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
                choiceType: 'PT_SINGLE_SELECT',
                name: 'DEPLOY_TARGET',
                referencedParameters: 'Deploy',
                script: [
                    $class: 'ScriptlerScript',
                    scriptlerScriptId:'DEPLOY_TARGET.groovy',
                    parameters: [
                    [name:'Deploy', value: '$Deploy']
                    ]
                ]
            ]
    
    
 ])
])

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
