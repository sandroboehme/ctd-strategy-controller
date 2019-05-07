import json
import os

from google.cloud import scheduler_v1


def gcloudscheduler(data, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         data (dict): The dictionary with data specific to this type of event.
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata.

         see
         https://googleapis.github.io/google-cloud-python/latest/scheduler/gapic/v1/api.html
         https://github.com/googleapis/google-cloud-python/blob/master/scheduler/google/cloud/scheduler_v1/gapic/cloud_scheduler_client.py
         https://cloud.google.com/scheduler/docs/reference/libraries
    """
    # client = scheduler_v1.CloudSchedulerClient()
    # parent = '/projects/example5-237118/locations/europe-west1'
    # job = {
    #     "pubsub_target": {
    #         "topic_name": "projects/example5-237118/topics/trade-tests",
    #         "data": "SGVsbG8gU2FuZHJvb"
    #     },
    #     "schedule": "* * * * *"
    # }
    # https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules
    current_folder = os.path.dirname(os.path.abspath(__file__))
    abs_auth_path = os.path.join(current_folder, 'auth.json')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = abs_auth_path
    data["job"]["pubsub_target"]["data"] = bytes(data["job"]["pubsub_target"]["data"], 'utf-8')

    response = scheduler_v1.CloudSchedulerClient().create_job(data["parent"], data["job"])
    print("name")
    print(response.name)


