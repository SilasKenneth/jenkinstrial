pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'python3 -m virtualenv env'
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