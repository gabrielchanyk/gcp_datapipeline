/kaniko/executor
--build-arg=RELEASEVERSION="${VERSION_NUMBER}"
    --build-arg CONFIG_BUCKET=${CONFIG_BUCKET}
--context "(CI_PROJECT_DIR)"
--dockerfile /datasets/top/pipelines/crj/sqoop/Dockerfile
--destination "${DOCKER_AR}/%{CRJ_SQOP_DOCKER_IMAGAE}"
--cache=true
--cache-ttl=6h
