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

new_job = {
    'company_name': 'projects/magnificent-wallabe/companies/083495ad-acba-477f-a084-8be84f31692e',
    'title': 'Senior Llama Wrangler',
    'description':
    """Experienced Llama Wrangler required for full-time position.
    Leadership ability required, as you will be taking a team of llama
    caregivers and training them up to full-scale wranglers.
    <p/>Must work well with animals and occasionally be prepared to run
    really, like really really fast.  Like REALLY fast.
    These are quick llamas.""",
    'requisition_id': 'senior_llama_wrangler',
    'application_info': {
        'uris': ['http://www.example.com/llama-wrangler-application'],
        'emails': ['llama-apply@example.com']
    }
}

try:
    # Nest that Job object in a "job" object.  Now it's an API request!
    request = {'job': new_job}

    # The actual API call happens here.
    result = client_service.projects().jobs().create(
        parent=project_id, body=request).execute()
    print('Job created: %s' % result)

except Error as e:
    print('Got exception while creating job')
    raise e
