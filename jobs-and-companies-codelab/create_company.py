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

# Build the service object, passing in the api name and api version
client_service = build('jobs', 'v3')

project_id = 'projects/' + os.environ['GOOGLE_CLOUD_PROJECT']
# Specifying details for the company that's going to be created.
# These are the only two required fields.
# Optional fields are documented at
# http://googleapis.github.io/google-api-python-client/docs/dyn/jobs_v3.projects.companies.html#create
new_company = {
    'display_name': "FooCorp",
    'external_id': "foo_llc"
}
request = {'company': new_company}

try:

    # This is the API call that actually creates the new company.
    result = client_service.projects().companies().create(
        parent=project_id, body=request).execute()

    # You can easily just print the result as a string if you want
    print('Company created: %s' % result)

    # Here's how you'd access individual fields.  The fields returned depend on
    # what you specified in the "new_company" object.  To see possible fields
    # in response, see the "create" documentation at:
    # http://googleapis.github.io/google-api-python-client/docs/dyn/jobs_v3.projects.companies.html#create
    print('%s, %s, %s' % (result.get('externalId'),
                          result.get('displayName'),
                          result.get('name')))

except Error as e:
    print('Got exception while creating company')
    raise e
