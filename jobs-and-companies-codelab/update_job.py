#!/usr/bin/env python

# Copyright 2019 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from googleapiclient.discovery import build
from googleapiclient.errors import Error

client_service = build('jobs', 'v3')
project_id = 'projects/' + os.environ['GOOGLE_CLOUD_PROJECT']


def get_job(job_name):
    try:
        job_existed = client_service.projects().jobs().get(
            name=job_name).execute()
        print('Job existed: %s' % job_existed)
        return job_existed
    except Error as e:
        print('Got exception while getting job')
        raise e


job_name = "projects/magnificent-wallabe/jobs/103672929591403206"
job_info = get_job(job_name)
try:

    # First the full-replacement method.  Update the complete job object with
    # new field values.
    job_patch = {
        'title': "Rogue Llama Acquisition Engineer"
    }

    job_info.update(job_patch)
    request = {"job": job_info}

    job_updated = client_service.projects().jobs().patch(
        name=job_name, body=request).execute()
    print("Updated job info : %s" % job_updated)

    # Alternatively, if you know which fields have been updated, you can submit
    # a patch with just the changes and an update mask. This time let's just
    # re-use the same job patch, and create an update mask.
    update_mask = "title"
    request = {"job": job_patch,
               "updateMask": update_mask
               }

    # Note that because the mask is included in the request object, the line
    # that actually calls the API takes the same arguments either way: The job
    # name and the request object.
    job_updated = client_service.projects().jobs().patch(
        name=job_name, body=request).execute()

    print("Updated job info : %s" % job_updated)


except Error as e:
    print('Got exception while updating job')
    raise e
