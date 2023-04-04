import logging
import uuid

from glean import load_metrics, Glean, Configuration

config = Configuration(
    # Local pingserver
    server_endpoint="http://127.0.0.1:6114",
    # Every event triggers a ping.
    max_events=1,
)

Glean.initialize(
    application_id="sample-app",
    application_version="0.1.0",
    upload_enabled=True,
    data_dir="./data",
    log_level=logging.DEBUG,
    configuration=config,
)

metrics = load_metrics("metrics.yaml")
metrics.info.started.set()

extra = metrics.experiments.EnrolledExtra(id=str(uuid.uuid4()))
metrics.experiments.enrolled.record(extra)
