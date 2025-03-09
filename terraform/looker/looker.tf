resource "google_looker_instance" "looker_instance" {
  name         = "looker-instance"
  region       = "us-central1"
  public_ip_enabled = true
  admin_settings {
    allowed_email_domains = ["example.com"]
  }
  oauth_config {
    client_id     = "<YOUR_CLIENT_ID>"
    client_secret = "<YOUR_CLIENT_SECRET>"
  }
}