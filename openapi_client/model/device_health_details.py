"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from openapi_client.exceptions import ApiAttributeError



class DeviceHealthDetails(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('health',): {
            'RED': "red",
            'YELLOW': "yellow",
            'GREEN': "green",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'bfd_sessions': (int,),  # noqa: E501
            'bfd_sessions_up': (int,),  # noqa: E501
            'board_serial_number': (str,),  # noqa: E501
            'chassis_number': (str,),  # noqa: E501
            'connected_vmanages': ([str],),  # noqa: E501
            'control_connections_to_vsmat': (DeviceHealthDetails,),  # noqa: E501
            'control_connections': (int,),  # noqa: E501
            'control_connections_up': (int,),  # noqa: E501
            'cpu_load': (float,),  # noqa: E501
            'device_groups': ([str],),  # noqa: E501
            'device_model': (str,),  # noqa: E501
            'device_type': (str,),  # noqa: E501
            'expected_vsmart_connections': (int,),  # noqa: E501
            'has_geo_data': (bool,),  # noqa: E501
            'health': (str,),  # noqa: E501
            'latitude': (str,),  # noqa: E501
            'local_system_ip': (str,),  # noqa: E501
            'location': (str,),  # noqa: E501
            'longitude': (str,),  # noqa: E501
            'memory_utilization': (float,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'omp_peers': (int,),  # noqa: E501
            'omp_peers_up': (int,),  # noqa: E501
            'personality': (str,),  # noqa: E501
            'qoe': (int,),  # noqa: E501
            'reachability': (str,),  # noqa: E501
            'site_id': (str,),  # noqa: E501
            'software_version': (str,),  # noqa: E501
            'system_ip': (str,),  # noqa: E501
            'uptime_date': (int,),  # noqa: E501
            'uuid': (str,),  # noqa: E501
            'vpn_ids': ([str],),  # noqa: E501
            'vsmart_control_connections': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'bfd_sessions': 'bfd_sessions',  # noqa: E501
        'bfd_sessions_up': 'bfd_sessions_up',  # noqa: E501
        'board_serial_number': 'board_serial_number',  # noqa: E501
        'chassis_number': 'chassis_number',  # noqa: E501
        'connected_vmanages': 'connected_vmanages',  # noqa: E501
        'control_connections_to_vsmat': 'controlConnectionsToVsmat',  # noqa: E501
        'control_connections': 'control_connections',  # noqa: E501
        'control_connections_up': 'control_connections_up',  # noqa: E501
        'cpu_load': 'cpu_load',  # noqa: E501
        'device_groups': 'device_groups',  # noqa: E501
        'device_model': 'device_model',  # noqa: E501
        'device_type': 'device_type',  # noqa: E501
        'expected_vsmart_connections': 'expected_vsmart_connections',  # noqa: E501
        'has_geo_data': 'has_geo_data',  # noqa: E501
        'health': 'health',  # noqa: E501
        'latitude': 'latitude',  # noqa: E501
        'local_system_ip': 'local_system_ip',  # noqa: E501
        'location': 'location',  # noqa: E501
        'longitude': 'longitude',  # noqa: E501
        'memory_utilization': 'memory_utilization',  # noqa: E501
        'name': 'name',  # noqa: E501
        'omp_peers': 'omp_peers',  # noqa: E501
        'omp_peers_up': 'omp_peers_up',  # noqa: E501
        'personality': 'personality',  # noqa: E501
        'qoe': 'qoe',  # noqa: E501
        'reachability': 'reachability',  # noqa: E501
        'site_id': 'site_id',  # noqa: E501
        'software_version': 'software_version',  # noqa: E501
        'system_ip': 'system_ip',  # noqa: E501
        'uptime_date': 'uptime_date',  # noqa: E501
        'uuid': 'uuid',  # noqa: E501
        'vpn_ids': 'vpn_ids',  # noqa: E501
        'vsmart_control_connections': 'vsmart_control_connections',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """DeviceHealthDetails - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            bfd_sessions (int): [optional]  # noqa: E501
            bfd_sessions_up (int): [optional]  # noqa: E501
            board_serial_number (str): [optional]  # noqa: E501
            chassis_number (str): [optional]  # noqa: E501
            connected_vmanages ([str]): [optional]  # noqa: E501
            control_connections_to_vsmat (DeviceHealthDetails): [optional]  # noqa: E501
            control_connections (int): [optional]  # noqa: E501
            control_connections_up (int): [optional]  # noqa: E501
            cpu_load (float): [optional]  # noqa: E501
            device_groups ([str]): [optional]  # noqa: E501
            device_model (str): [optional]  # noqa: E501
            device_type (str): [optional]  # noqa: E501
            expected_vsmart_connections (int): [optional]  # noqa: E501
            has_geo_data (bool): [optional]  # noqa: E501
            health (str): [optional]  # noqa: E501
            latitude (str): [optional]  # noqa: E501
            local_system_ip (str): [optional]  # noqa: E501
            location (str): [optional]  # noqa: E501
            longitude (str): [optional]  # noqa: E501
            memory_utilization (float): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            omp_peers (int): [optional]  # noqa: E501
            omp_peers_up (int): [optional]  # noqa: E501
            personality (str): [optional]  # noqa: E501
            qoe (int): [optional]  # noqa: E501
            reachability (str): [optional]  # noqa: E501
            site_id (str): [optional]  # noqa: E501
            software_version (str): [optional]  # noqa: E501
            system_ip (str): [optional]  # noqa: E501
            uptime_date (int): [optional]  # noqa: E501
            uuid (str): [optional]  # noqa: E501
            vpn_ids ([str]): [optional]  # noqa: E501
            vsmart_control_connections (int): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """DeviceHealthDetails - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            bfd_sessions (int): [optional]  # noqa: E501
            bfd_sessions_up (int): [optional]  # noqa: E501
            board_serial_number (str): [optional]  # noqa: E501
            chassis_number (str): [optional]  # noqa: E501
            connected_vmanages ([str]): [optional]  # noqa: E501
            control_connections_to_vsmat (DeviceHealthDetails): [optional]  # noqa: E501
            control_connections (int): [optional]  # noqa: E501
            control_connections_up (int): [optional]  # noqa: E501
            cpu_load (float): [optional]  # noqa: E501
            device_groups ([str]): [optional]  # noqa: E501
            device_model (str): [optional]  # noqa: E501
            device_type (str): [optional]  # noqa: E501
            expected_vsmart_connections (int): [optional]  # noqa: E501
            has_geo_data (bool): [optional]  # noqa: E501
            health (str): [optional]  # noqa: E501
            latitude (str): [optional]  # noqa: E501
            local_system_ip (str): [optional]  # noqa: E501
            location (str): [optional]  # noqa: E501
            longitude (str): [optional]  # noqa: E501
            memory_utilization (float): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            omp_peers (int): [optional]  # noqa: E501
            omp_peers_up (int): [optional]  # noqa: E501
            personality (str): [optional]  # noqa: E501
            qoe (int): [optional]  # noqa: E501
            reachability (str): [optional]  # noqa: E501
            site_id (str): [optional]  # noqa: E501
            software_version (str): [optional]  # noqa: E501
            system_ip (str): [optional]  # noqa: E501
            uptime_date (int): [optional]  # noqa: E501
            uuid (str): [optional]  # noqa: E501
            vpn_ids ([str]): [optional]  # noqa: E501
            vsmart_control_connections (int): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")