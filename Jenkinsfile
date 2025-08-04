pipeline {
  agent any

  environment {
    VENV_DIR = 'venv'
    FLASK_ENV = 'production'
    DOCKER_IMAGE = 'retroflicks'
    DOCKER_TAG = 'latest'
  }

  stages {
    stage('Checkout') {
      steps {
        echo '📥 Checking out source code...'
        checkout scm
      }
    }

    stage('Setup Python Environment') {
      steps {
        echo '🐍 Setting up virtual environment...'
        sh '''
          python3 -m venv $VENV_DIR
          source $VENV_DIR/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Lint') {
      steps {
        echo '🔍 Running flake8 lint checks...'
        sh '''
          source $VENV_DIR/bin/activate
          pip install flake8
          flake8 app --count --select=E9,F63,F7,F82 --show-source --statistics
        '''
      }
    }

    stage('Test') {
      steps {
        echo '🧪 Running unit tests with coverage...'
        sh '''
          source $VENV_DIR/bin/activate
          pip install pytest pytest-cov
          pytest --cov=app --cov-report=term-missing
        '''
      }
    }

    stage('Build Docker Image') {
      steps {
        echo '🐳 Building Docker image...'
        sh '''
          docker build -t $DOCKER_IMAGE:$DOCKER_TAG .
        '''
      }
    }

    stage('Deploy') {
      steps {
        echo '🚀 Deploying container...'
        sh '''
          docker stop retroflicks || true
          docker rm retroflicks || true
          docker run -d --name retroflicks -p 5000:5000 $DOCKER_IMAGE:$DOCKER_TAG
        '''
      }
    }
  }

  post {
    success {
      echo '✅ Build and deployment successful!'
    }
    failure {
      echo '❌ Build failed. Check logs for details.'
    }
  }
}

