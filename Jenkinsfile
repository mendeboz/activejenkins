job("MyJob") {
    description ("This job creates ....")
    
    //def targetEnvironment=""
    

    parameters {
         activeChoiceParam('choice1') {
                      description('select your choice')
                      choiceType('RADIO')
                      groovyScript {
                          script('return["aaa","bbb"]')
                          fallbackScript('return ["error"]')
                      }
        }
        activeChoiceReactiveParam('choice2') {
                      description('select your choice')
                      choiceType('RADIO')
                      groovyScript {
                          script(' if(choice1.equals("aaa")) { return ["a", "b"] } else {return ["aaaaaa","fffffff"] } ')
                          fallbackScript('return ["error"]')
                      }
                      referencedParameter('choice1')
        }

    }
}