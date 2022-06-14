pipeline {
    agent none

    stages {
        stage('BuildTestDeploy') {
            matrix {
                agent {
                    dockerfile {
                        filename "Dockerfile.${DOCKER_IMAGE}"
                        dir 'dockerfiles'
                        label 'docker'
                        customWorkspace "workspace/${JOB_NAME}/OS/${DOCKER_IMAGE}/" 
                    }
                }

                axes {
                    axis {
                        name 'DOCKER_IMAGE'
                        values 'ubuntu_18', 'ubuntu_20'
                    }
                }

                stages {
//                     stage("Install common dependencies") {
//                         when { 
//                             anyOf {
//                                 environment name: 'DOCKER_IMAGE', value: 'ubuntu_20' 
//                             }
//                         }
//                         steps {
//                         }
//                     }
                    
//                     stage('Install custom dependencies') {
//                         when { 
//                             anyOf {
//                                 environment name: 'DOCKER_IMAGE', value: 'ubuntu_18' 
//                             }
//                         }
//                         steps {
                            
//                         }
//                     }
                    stage('Build') {
                        steps {
                            echo "Do Build for ${DOCKER_IMAGE}"
                            sh 'ls -la'
                            sh 'python3 build_deb.py'
                        }
                    }
                 }
            }
        }
    }
    post {
        always { 
            node('docker') {
                archiveArtifacts artifacts: 'OS/*/*.deb'
                cleanWs()
            }
        }
    }
} 
