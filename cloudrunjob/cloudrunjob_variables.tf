variable "cloud_run_jobs" {
    type = map(object({
        region          = string
        image           = string
        vpc_connector   = string
        cpu             = number
        memory          = string
        task_count      = number
        task_timeout    = string
        env_vars = list(object({
            name  = string
            value = string
        }))
        env_secret_vars = list(object({
            env_secret_name     = string
            env_secret          = string
            env_secret_version  = string
    }))
       config_file = string    
}))
validation {
    condition = alltrue([
        for j1 in var.cloud_run_jobs : contains(["nane1", "nane2"], j1.region)
    ])
    error_message = "Region must be either nane1 or nane2"
}
default = {}
}
