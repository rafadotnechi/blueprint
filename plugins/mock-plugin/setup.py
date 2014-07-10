########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

from setuptools import setup

setup(
    # Do not use underscores in the plugin name.
    name='mock-host-plugin',

    version='1.0',
    author='Gigaspaces',
    author_email='cosmo-admin@gigaspaces.com',

    # This must correspond to the actual packages in the plugin.
    # It will also serve as the plugin prefix for mapping operations to tasks.
    packages=['mock_host'],

    license='LICENSE',
    description='Mock host plugin.',
    zip_safe=False,
    install_requires=[
        "cloudify-plugins-common>=3.0"
    ]
)
