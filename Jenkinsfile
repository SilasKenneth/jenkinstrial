pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            sh 'python -m pip install virtualenv'
            sh 'python -m virtualenv env'
            sh 'source env/bin/activate'
            sh 'python -m pip install -r requirements.txt'
            sh 'python -m pytest --cov=app --cov-report=term-missing'
          }
        }
        stage('Print') {
          steps {
            sh 'echo Hello world'
          }
        }
      }
    }
    stage('Done') {
      steps {
        echo 'I miss the build'
      }
    }
  }
}