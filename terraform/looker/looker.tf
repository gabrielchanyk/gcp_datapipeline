# looker not working for free version
# resource "google_project_service" "looker_api" {
#   provider = google-beta
#   project = var.projectID
#   service = "looker.googleapis.com"
# }

# resource "google_looker_instance" "looker-instance" {
#   name              = "my-instance"
#   platform_edition  = "LOOKER_CORE_STANDARD_ANNUAL"
#   region            = var.region
#   oauth_config {
#     client_id = "my-client-id"
#     client_secret = "my-client-secret"
#   }
#   depends_on = [ google_project_service.looker_api ]
# }