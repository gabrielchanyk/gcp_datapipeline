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

resource "google_cloud_run_v2_job" "default" {
  name     = "cloudrun-job"
  location = "northamerica-northeast1"  # Montreal region
  deletion_protection = false

  template {
    template {
      containers {
        image = "northamerica-northeast1-docker.pkg.dev/bellassignment-453021/docker-repo/odbc:latest"
      }
    }
  }
  depends_on = [ google_project_service.cloudrun_api ]
}