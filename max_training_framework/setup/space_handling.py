#
# Copyright 2020 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from ibm_watson_machine_learning import APIClient


class SpaceHandler:

    def __init__(self, apikey, url):
        try:
            wml_credentials = {
                'url': url,
                'apikey': apikey,
            }
            self.client = APIClient(wml_credentials)
        except Exception as ex:
            print(ex)

    def create_space(self, space_name, space_desc, wml_name, wml_crn, cos_crn):

        space_metadata = {
            'name': space_name,
            'description': space_desc,
            'storage': {
                'type': 'bmcos_object_storage',
                'resource_crn': cos_crn
            },
            'compute': {
                'name': wml_name,
                'crn': wml_crn
            }
        }

        space_details = self.client.spaces.store(space_metadata)
        space_id = self.client.spaces.get_id(space_details)

        return space_id
