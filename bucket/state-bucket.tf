resource "google_storage_bucket" "bell-assignment-state" {
  name          = "bell-assignment-state"
  location      = var.region
  project       = var.projectID
  force_destroy = var.force_destroy
}