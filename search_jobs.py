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
import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import Error

client_service = build('jobs', 'v3')
project_id = 'projects/' + os.environ['GOOGLE_CLOUD_PROJECT']

# 1) Define RequestMetadata object
request_metadata = {
    'domain':     'example.com',
    'session_id': 'a5ed434a3f5089b489576cceab824f25',
    'user_id':    '426e428fb99b609d203c0cdb6af3ba36',
}


location_filter = {
    'address': 'San Francisco',
    'distance_in_miles': 10,
}

job_query = {
    #    'location_filters': [location_filter],
    'query': "Engineer",
}

# 2) Throw RequestMetadata object in a request
request = {
    'requestMetadata': request_metadata,
    'jobQuery': job_query,
    'jobView': 'JOB_VIEW_FULL',
    'diversificationLevel': 'DISABLED'
}

try:
    # 3) Make the API call
    response = client_service.projects().jobs().search(
        parent=project_id, body=request).execute()

    # 4) Inspect the results
    if response.get('matchingJobs') is not None:
        print('Search Results:')
        for job in response.get('matchingJobs'):
            print('%s: %s\n' % (job.get('job').get('title'),
                                job.get('searchTextSnippet')))

    else:
        print('No Job Results')

except Error as e:
    # Alternate 3) or 4) Surface error if things don't work.
    print('Got exception while searching')
    raise e
