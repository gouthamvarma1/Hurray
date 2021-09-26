pipeline {
     agent any
     stages {
        stage("Build") {
            steps {

            //ec2 instance need to have node js installed by default
                sh "node -v"
                sh "npm -v"
                sh "npm install"
                //sh "npm test"
                sh "npm run build"
                
            }
        }
        stage("sonarqube quality") {
            steps {

            //ec2 instance need to have node js installed by default
                sh "npm install --save-dev sonarqube-scanner"
                sh "sudo  node sonarqube-scanner.js"
                
            }
        }

        stage("Deploy to ec2-Instace") {
            steps {

               sh "echo pushing build to ec2 Instance"
               sh "scp -r $pwd/workspace/frontend/build/  ubuntu@3.89.212.234:/home/ubuntu/frontend/"
               sh "echo Pushed to ec2 Instance"
                
            }
        }

        stage("Run Automation Suite") {
            steps {
            //curl -X POST http://USER:API_TOKEN@localhost:8080/job/test/build
               sh "curl -X POST http://admin:114c39517508f981a90159215d03b3d222@3de818d6ab94.ngrok.io/job/automation/build"
                
            }
        }
        stage("Deploy to s3") {
            steps {
                //Ec2 instance need to have aws cli installed
                sh "aws s3 cp $pwd/workspace/frontend/build/./  s3://bitsgoufront --recursive"
                
            }
        }
    }
}