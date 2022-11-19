pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker')
	}

	stages {
	
		stage('Login to dockerhub') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW |  docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
		
		stage('Build image') {

			steps {
				sh 'docker build -t eliehadd/docker-final-task:latest .'
			}
		}


		stage('Push to dockerhub') {

			steps {
				sh ' docker push eliehadd/docker-final-task'
			}
		}
	}

	post {
		always {
			sh ' docker logout'
		}
	}

}
