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


def list_everything():
    try:
        response = client_service.projects().companies().list(
            parent=project_id).execute()
        if response.get('companies') is not None:
            print('Companies and Jobs:')
            for company in response.get('companies'):
                print('%s: %s' % (company.get('displayName'),
                                  company.get('name')))
                jobs_response = client_service.projects().jobs().list(
                    parent=project_id,
                    filter='companyName="' + company.get('name') + '"'
                    ).execute()
                if jobs_response.get('jobs') is not None:
                    for job in jobs_response.get('jobs'):
                        print('- %s: %s' % (
                              job.get('title'),
                              job.get('name')))
        else:
            print('No companies')

    except Error as e:
        print('Got exception while listing everything')
        raise e


list_everything()
