resource "google_storage_bucket_object" "crj-config" {
    for_each    = var.cloud_run_jobs
    name        = each.value.config_file
    source      = format("config/%s",each.value.config_file)
    bucket      = google_storage_bucket.bell-assignment-state.name
}

resource "google_secret_manager_secret_iam_member" "crj-secrets-reader-sa"{
    for_each = var.secrets
    project - var.project
    
    }
}