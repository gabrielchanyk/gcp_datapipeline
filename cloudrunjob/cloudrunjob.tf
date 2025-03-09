resource "google_project_service" "cloudrun_api" {
  provider = google-beta
  project = var.projectID
  service = "run.googleapis.com"
}

# resource "google_cloud_run_v2_job" "cloud-run-job-workflows"{
#     for_each = var.cloud_run_jobs
#     location = lookup(local.regions, each.value.region, "northamerica-northeast1")
#     project = var.project
#     name = each.value.name

#     labels ={
#         project-id = var.project
#         owner = var.owner
#     }
#     template {
#         task_count = each.value.task_count
#         template {
#             max_retries = 1
#             timeout = each.value.task_timeout
#             service_account = var.service_account
#             containers {
#                 image = each.value.image
#                 resources {
#                     limits = {
#                         cpu = each.value.cpu
#                         memory = each.value.memory
#                     }
#                 }
#                 dynamic "env" {
#                     for_each = each.value.env_vars
#                     content {
#                         name = env.value.name
#                         value = env.value.value
#                     }
#                 }
#                 dynamic "env" {
#                     for_each = each.value.env_secret_vars
#                     content {
#                         name = env.value.env_secret_name
#                     }
#                     value_source {
#                         secret_key_ref {
#                             secret_key_version_id = env.value.secret_version_id
#                             secret_name = env.value.secret_name
#                         }
#                     }
#                 }
#             }
#         }
    
#     }
#     depends_on = [google_storage_bucket_object.crj-config]
# }

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