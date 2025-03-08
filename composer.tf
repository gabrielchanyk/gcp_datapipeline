resource "google_project_service" "composer_api" {
  provider = google-beta
  project = var.projectID
  service = "composer.googleapis.com"
  // Disabling Cloud Composer API might irreversibly break all other
  // environments in your project.
  // This parameter prevents automatic disabling
  // of the API when the resource is destroyed.
  // We recommend to disable the API only after all environments are deleted.
  disable_on_destroy = false
  // this flag is introduced in 5.39.0 version of Terraform. If set to true it will
  //prevent you from disabling composer_api through Terraform if any environment was
  //there in the last 30 days
  check_if_service_has_usage_on_destroy = true
}

resource "google_composer_environment" "composer_env" {
  name   = "composer-env"
  region = var.region
  project = var.projectID
 config {
    software_config {
      image_version = "composer-3-airflow-2"
    }
  }
}