resource "google_project_service" "secret_api" {
  provider = google-beta
  project = var.projectID
  service = "secretmanager.googleapis.com"
}

resource "google_secret_manager_secret" "secrets" {
  secret_id = "my_sql_pw"
  replication {
      user_managed {
      replicas {
        location = var.region
      }
    }
  }
  depends_on = [ google_project_service.secret_api ]
}