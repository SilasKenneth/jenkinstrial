pipeline {
  agent {
    docker {
      image 'python:3.5.7-alpine3.8'
      args '-u 0:0'
    }

  }
  stages {
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
        archiveArtifacts(artifacts: '.coverage*', allowEmptyArchive: true)
      }
    }
    stage('Congrats') {
      steps {
        echo 'Congratulations everything worked'
      }
    }
  }
}