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


class ManagedHostingEnvironment(Resource):
    """
    Description of a managed hosting environment

    :param str id: Resource Id
    :param str name: Resource Name
    :param str location: Resource Location
    :param str type: Resource type
    :param dict tags: Resource tags
    :param str managed_hosting_environment_name: Name of the managed hosting
     environment
    :param str managed_hosting_environment_location: Location of the managed
     hosting environment e.g. "West US"
    :param str status: Current status of the managed hosting environment.
     Possible values include: 'Preparing', 'Ready', 'Deleting'
    :param VirtualNetworkProfile virtual_network: Description of the managed
     hosting environment's virtual network
    :param int ipssl_address_count: Number of ip ssl addresses reserved for
     the managed hosting environment
    :param str dns_suffix: DNS suffix of the managed hosting environment
    :param str subscription_id: Subscription of the managed hosting
     environment (read only)
    :param str resource_group: Resource group of the managed hosting
     environment (read only)
    :param bool environment_is_healthy: True/false indicating whether the
     managed hosting environment is healthy
    :param str environment_status: Detailed message about with results of the
     last check of the managed hosting environment
    :param bool suspended: True/false indicating whether the managed hosting
     environment is suspended. The environment can be suspended e.g. when the
     management endpoint is no longer available
     (most likely because NSG blocked the incoming traffic)
    :param str api_management_account: Resource id of the api management
     account associated with this managed hosting environment (read only)
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_hosting_environment_name': {'key': 'properties.name', 'type': 'str'},
        'managed_hosting_environment_location': {'key': 'properties.location', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'ManagedHostingEnvironmentStatus'},
        'virtual_network': {'key': 'properties.virtualNetwork', 'type': 'VirtualNetworkProfile'},
        'ipssl_address_count': {'key': 'properties.ipsslAddressCount', 'type': 'int'},
        'dns_suffix': {'key': 'properties.dnsSuffix', 'type': 'str'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
        'resource_group': {'key': 'properties.resourceGroup', 'type': 'str'},
        'environment_is_healthy': {'key': 'properties.environmentIsHealthy', 'type': 'bool'},
        'environment_status': {'key': 'properties.environmentStatus', 'type': 'str'},
        'suspended': {'key': 'properties.suspended', 'type': 'bool'},
        'api_management_account': {'key': 'properties.apiManagementAccount', 'type': 'str'},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, managed_hosting_environment_name=None, managed_hosting_environment_location=None, status=None, virtual_network=None, ipssl_address_count=None, dns_suffix=None, subscription_id=None, resource_group=None, environment_is_healthy=None, environment_status=None, suspended=None, api_management_account=None, **kwargs):
        super(ManagedHostingEnvironment, self).__init__(id=id, name=name, location=location, type=type, tags=tags, **kwargs)
        self.managed_hosting_environment_name = managed_hosting_environment_name
        self.managed_hosting_environment_location = managed_hosting_environment_location
        self.status = status
        self.virtual_network = virtual_network
        self.ipssl_address_count = ipssl_address_count
        self.dns_suffix = dns_suffix
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.environment_is_healthy = environment_is_healthy
        self.environment_status = environment_status
        self.suspended = suspended
        self.api_management_account = api_management_account
