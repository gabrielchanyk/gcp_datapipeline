resource "google_project_service" "cloudrun_api" {
  provider = google-beta
  project = var.projectID
  service = "run.googleapis.com"
}

resource "google_project_iam_member" "secret_accessor" {
  project = var.projectID
  role    = "roles/secretmanager.secretAccessor"
  member  = "serviceAccount:836681211124-compute@developer.gserviceaccount.com"
}

resource "google_cloud_run_v2_job" "cloud-run-job-workflows" {
  name     = "cloudrun-job-workflows"
  location = "northamerica-northeast1"  # Montreal region
  deletion_protection = false

  template {
    template {
      containers {
        image = "northamerica-northeast1-docker.pkg.dev/bellassignment-453021/docker-repo/odbc:latest"
        volume_mounts {
          mount_path = "/secrets"
          name       = "secret-volume"
        }
      }
      volumes {
        name = "secret-volume"
        secret {
          secret = google_secret_manager_secret.secrets.secret_id
          items {
            path = "my_sql_pw"
            version = "latest"
          }
        }
      }
    }
  }
  depends_on = [ google_project_service.cloudrun_api, google_project_iam_member.secret_accessor ]
}