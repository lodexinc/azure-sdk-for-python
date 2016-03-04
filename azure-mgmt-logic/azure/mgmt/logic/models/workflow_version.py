# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class WorkflowVersion(Resource):
    """WorkflowVersion

    :param str id: Gets or sets the resource id.
    :param str name: Gets the resource name.
    :param str type: Gets the resource type.
    :param str location: Gets or sets the resource location.
    :param dict tags: Gets or sets the resource tags.
    :param datetime created_time: Gets the created time.
    :param datetime changed_time: Gets the changed time.
    :param str state: Gets or sets the state. Possible values include:
     'NotSpecified', 'Enabled', 'Disabled', 'Deleted', 'Suspended'
    :param str version: Gets the version.
    :param str access_endpoint: Gets the access endpoint.
    :param Sku sku: Gets or sets the sku.
    :param ContentLink definition_link: Gets or sets the link to definition.
    :param object definition: Gets or sets the definition.
    :param ContentLink parameters_link: Gets or sets the link to parameters.
    :param dict parameters: Gets or sets the parameters.
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
        'changed_time': {'key': 'properties.changedTime', 'type': 'iso-8601'},
        'state': {'key': 'properties.state', 'type': 'WorkflowState'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'access_endpoint': {'key': 'properties.accessEndpoint', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'Sku'},
        'definition_link': {'key': 'properties.definitionLink', 'type': 'ContentLink'},
        'definition': {'key': 'properties.definition', 'type': 'object'},
        'parameters_link': {'key': 'properties.parametersLink', 'type': 'ContentLink'},
        'parameters': {'key': 'properties.parameters', 'type': '{WorkflowParameter}'},
    }

    def __init__(self, id=None, name=None, type=None, location=None, tags=None, created_time=None, changed_time=None, state=None, version=None, access_endpoint=None, sku=None, definition_link=None, definition=None, parameters_link=None, parameters=None, **kwargs):
        super(WorkflowVersion, self).__init__(id=id, name=name, type=type, location=location, tags=tags, **kwargs)
        self.created_time = created_time
        self.changed_time = changed_time
        self.state = state
        self.version = version
        self.access_endpoint = access_endpoint
        self.sku = sku
        self.definition_link = definition_link
        self.definition = definition
        self.parameters_link = parameters_link
        self.parameters = parameters
