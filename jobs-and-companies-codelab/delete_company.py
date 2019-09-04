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

from googleapiclient.discovery import build
from googleapiclient.errors import Error

client_service = build('jobs', 'v3')

# Name of the company to delete
# this matches the "name" field of the company object.
# Will be of the form "projects/your-project-name/....../123-long-hex-string"
company_to_delete = 'projects/magnificent-wallabe/companies/a4e14373-94bb-4481-9b15-148555a26283'
job_to_delete = "projects/magnificent-wallabe/jobs/74006148711097030"

try:
    job_delete = client_service.projects().jobs().delete(name=job_to_delete).execute()
    result_company = client_service.projects().companies().delete(
        name=company_to_delete).execute()
    print('Result of deleting company: %s' % result_company)

except Error as e:
    print('Got exception while deleting company')
    raise e
