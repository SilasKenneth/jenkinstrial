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
      stage('Build') {
        steps {
          container("pythonalpine38"){
            	sh 'pip install virtualenv'
              sh 'virtualenv env'
              sh 'source env/bin/activate'
              sh 'pip install -r requirements.txt'
              sh 'python -m pytest --cov=app --cov-report=term-missing'
            }
        }
      }
      stage('Done') {
        steps {
          container("pythonalpine38"){
            echo 'I miss the build'
          }
        }
      }
      stage('Congrats') {
        steps {
          container("pythonalpine38"){
            echo 'Congratulations everything worked'
          }
        }
    }
  }
}
