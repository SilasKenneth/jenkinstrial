pipeline {
  agent {
  	docker{
  		image 'python:3.5.7-alpine3.8'
  	}
  }
  stages {
    stage('Build') {
      steps {
      	sh 'python -m pip install virtualenv'
        sh 'python -m virtualenv env'
        sh 'source env/bin/activate'
        sh 'python -m pip install -r requirements.txt'
        sh 'python -m pytest --cov=app --cov-report=term-missing'
      }
    }
    stage('Done') {
      steps {
        echo 'I miss the build'
      }
    }
    stage('Congrats') {
      steps {
        echo 'Congratulations everything worked'
      }
    }
  }
}