pipeline{
	agent any
	stages{
		stage('Create virtual environment'){
			steps{
				sh 'python3 -m virtualenv env'
			}
		}

		stage('Activate the virtualenv'){
			steps{
				sh 'source env/bin/activate'
			}
		}

		stage('Install dependencies'){
			steps{
				sh 'python -m pip install -r requirements.txt'
			}
		}

		stage('Run application tests'){
			steps{
				sh 'python -m pytest --cov=app --cov-report=term-missing'
			}
		}
	}
}