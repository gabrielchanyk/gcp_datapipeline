variable "cloud_run_jobs" {
    type = map(object({
        region          = string
        image           = string
        cpu             = string
        memory          = string
        environment     = map(string)
        secrets         = map(string)
        command         = list(string)
        args            = list(string)
    }))
}