group "default" {
  targets = ["retroflicks"]
}

target "retroflicks" {
  context    = "."
  dockerfile = "Dockerfile"
  tags       = ["retroflicks:latest"]
  platforms  = ["linux/amd64", "linux/arm64"]
  args = {
    FLASK_ENV = "production"
  }
}

