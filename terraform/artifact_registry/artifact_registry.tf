resource "google_artifact_registry_repository" "docker_repo" {
  location      = var.region
  repository_id = "docker-repo"
  description   = "Docker repository"
  format        = "DOCKER"
  project       = var.projectID
}