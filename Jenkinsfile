
@Library('mende-library')_

// properties([
//   parameters([
//     [
//         $class: 'ChoiceParameter',
//         choiceType: 'PT_SINGLE_SELECT',
//         name: 'testmende',
//         script: [
//             $class: 'GroovyScript',
//             fallbackScript: [classpath: [], sandbox: false, script: 'return ["ERROR"]'],
//             script: [classpath: [], 
//                     sandbox: false,
//                     script:  
//     """
//     return ["Select:selected","qa","qa-us"]
//     """
//                 ]
//         ]
//     ],
//     [
//       $class: 'ChoiceParameter',
//       choiceType: 'PT_SINGLE_SELECT',
//       name: 'Environment',
//       script: [
//         $class: 'ScriptlerScript',
//         scriptlerScriptId:'Environments.groovy'
//       ]
//     ],
//     [
//       $class: 'CascadeChoiceParameter',
//       choiceType: 'PT_SINGLE_SELECT',
//       name: 'Host',
//       referencedParameters: 'Environment',
//       script: [
//         $class: 'ScriptlerScript',
//         scriptlerScriptId:'HostsInEnv.groovy',
//         parameters: [
//           [name:'Environment', value: '$Environment']
//         ]
//       ]
//    ]
//  ])
// ])

pipeline {
    agent any

    
   
    environment{
        GIT_REPO = 'hudsonmx-portal'
    }

    stages {
        stage ('test library') {
            steps{
                script{
                    properties([
                        parameters(
                            [
                            string(name: 'FROM_BRANCH', defaultValue: 'DV-16281-extend-eks-jenkins-build-jobs-t')
                            choice(name: 'JDK', choices: ['jdk17'], description: 'Choose the JDK version')
                            booleanParam(name: 'SONAR_SCAN_ONLY', defaultValue: false, description: 'Only run the SonarQube scan')
                        
                        ] + props() )
                    ])
                    //println props().getClass()
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
