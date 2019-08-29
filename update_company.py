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


def get_company(company_name):
    try:
        company_existed = client_service.projects().companies().get(
            name=company_name).execute()
        print('Company existed: %s' % company_existed)
        return company_existed
    except Error as e:
        print('Got exception while getting company')
        raise e


patch = {
    'displayName': "The New Bar",
    'websiteUri': "http://www.example.com"
}


try:
    company_name = 'projects/magnificent-wallabe/companies/083495ad-acba-477f-a084-8be84f31692e'
    newCompany = get_company(company_name)
    newCompany.update(patch)
    request = {'company': newCompany}
    print("New company info %s " % newCompany)

    # Update without a mask
    company_updated = client_service.projects().companies().patch(
        name=company_name, body=request).execute()

    # New set of fields, not the complete company object
    companyFields = {'displayName': 'Masked Panda Inc',
                     'websiteUri': 'http://shouldNotUpdate.com',
                     'externalId': 'bar_llc'}

    # Note that the mask only contains the display name, not the URL.
    # This is entirely for demonstration purposes.  This mask will tell the API
    # to update the display name, but NOT the website uri.
    mask = 'displayName'
    request = {'company': companyFields,
               'update_mask': mask}
    company_updated = client_service.projects().companies().patch(
        name=company_name, body=request).execute()
    print('Company updated again!: %s' % company_updated)

    print('Company updated: %s' % company_updated)
except Error as e:
    print('Got exception while updating company')
    raise e
