pipeline {
  agent {
  	kubernetes{
      label 'silas-deploy'
      defaultContainer 'jnlp'
  		image 'python:3.5.7-alpine3.8'
  		yamlFile 'jenkins/config.yml'
  	}
  }
  stages {
    container("pythonalpine38"){
      stage('Build') {
        steps {
        	sh 'pip install virtualenv'
          sh 'virtualenv env'
          sh 'source env/bin/activate'
          sh 'pip install -r requirements.txt'
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
}
