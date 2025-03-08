# Google Cloud Provider
provider "google" {
  project     = "836681211124"
  region      = "northamerica-northeast1"
  credentials = file("bellassignment-453021-0fdbb9df8c60.json")
}

# Google Cloud Beta Provider
provider "google-beta" {
  project     = "836681211124"
  region      = "northamerica-northeast1"
  credentials = file("bellassignment-453021-0fdbb9df8c60.json")
}