pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker')
	}

	stages {
	
		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW |  docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		
		stage('Build image') {

			steps {
				sh 'docker build -t eliehadd/docker-final-task:latest .'
			}
		}


		stage('Push image') {

			steps {
				sh ' docker push eliehadd/dockerHW'
			}
		}
stage('Slack Notifications') {
            steps{
                slackSend baseUrl: 'https://hooks.slack.com/services/',
                channel: '#fursa-hw3',
                color: 'good',
                message: 'Image has been built and pushed to dockerhub',
                teamDomain: 'fursaHW',
                tokenCredentialId: 'slack-hw'
            }
        }
	}

	post {
		always {
			sh ' docker logout'
		}
	}

}
