resource "google_project_service" "secret_api" {
  provider = google-beta
  project = var.projectID
  service = "secretmanager.googleapis.com"
}

# resource "google_storage_bucket_object" "crj-config" {
#     for_each    = var.cloud_run_jobs
#     name        = each.value.config_file
#     source      = format("config/%s",each.value.config_file)
#     content_type = "application/yaml"
#     bucket      = google_storage_bucket.bucket_object.id
#     depends_on = [google_storage_bucket.bucket_object]
# }

# resource "google_secret_manager_secret_iam_member" "crj-secrets-reader-sa"{
#     for_each    = var.secrets
#     project     = var.project
#     secret_id   = format("secret_id")
#     role        = "roles/secretmanager.secretAccessor"
#     member      = "serviceAccount:${google_service_account.sa.email}"    
# }

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