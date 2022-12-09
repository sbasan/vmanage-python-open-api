"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)


class MonitoringDeviceStatisticsDetailsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.generate_device_statistics_data_endpoint = _Endpoint(
            settings={
                'response_type': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),
                'auth': [],
                'endpoint_path': '/data/device/statistics/{state_data_type}',
                'operation_id': 'generate_device_statistics_data',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'state_data_type',
                    'scroll_id',
                    'start_date',
                    'end_date',
                    'count',
                    'time_zone',
                ],
                'required': [
                    'state_data_type',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'state_data_type':
                        (str,),
                    'scroll_id':
                        (str,),
                    'start_date':
                        (str,),
                    'end_date':
                        (str,),
                    'count':
                        (int,),
                    'time_zone':
                        (str,),
                },
                'attribute_map': {
                    'state_data_type': 'state_data_type',
                    'scroll_id': 'scrollId',
                    'start_date': 'startDate',
                    'end_date': 'endDate',
                    'count': 'count',
                    'time_zone': 'timeZone',
                },
                'location_map': {
                    'state_data_type': 'path',
                    'scroll_id': 'query',
                    'start_date': 'query',
                    'end_date': 'query',
                    'count': 'query',
                    'time_zone': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_active_alarms_endpoint = _Endpoint(
            settings={
                'response_type': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),
                'auth': [],
                'endpoint_path': '/data/device/statistics/alarm/active',
                'operation_id': 'get_active_alarms',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'scroll_id',
                    'start_date',
                    'end_date',
                    'count',
                    'time_zone',
                ],
                'required': [
                    'scroll_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'scroll_id':
                        (str,),
                    'start_date':
                        (str,),
                    'end_date':
                        (str,),
                    'count':
                        (int,),
                    'time_zone':
                        (str,),
                },
                'attribute_map': {
                    'scroll_id': 'scrollId',
                    'start_date': 'startDate',
                    'end_date': 'endDate',
                    'count': 'count',
                    'time_zone': 'timeZone',
                },
                'location_map': {
                    'scroll_id': 'query',
                    'start_date': 'query',
                    'end_date': 'query',
                    'count': 'query',
                    'time_zone': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_count_with_state_data_type_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [],
                'endpoint_path': '/data/device/statistics/{state_data_type}/doccount',
                'operation_id': 'get_count_with_state_data_type',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'state_data_type',
                    'start_date',
                    'end_date',
                    'time_zone',
                ],
                'required': [
                    'state_data_type',
                    'start_date',
                    'end_date',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'state_data_type':
                        (str,),
                    'start_date':
                        (str,),
                    'end_date':
                        (str,),
                    'time_zone':
                        (str,),
                },
                'attribute_map': {
                    'state_data_type': 'state_data_type',
                    'start_date': 'startDate',
                    'end_date': 'endDate',
                    'time_zone': 'timeZone',
                },
                'location_map': {
                    'state_data_type': 'path',
                    'start_date': 'query',
                    'end_date': 'query',
                    'time_zone': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_stat_data_fields_by_state_data_type_endpoint = _Endpoint(
            settings={
                'response_type': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),
                'auth': [],
                'endpoint_path': '/data/device/statistics/{state_data_type}/fields',
                'operation_id': 'get_stat_data_fields_by_state_data_type',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'state_data_type',
                ],
                'required': [
                    'state_data_type',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'state_data_type':
                        (str,),
                },
                'attribute_map': {
                    'state_data_type': 'state_data_type',
                },
                'location_map': {
                    'state_data_type': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_statistics_type_endpoint = _Endpoint(
            settings={
                'response_type': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),
                'auth': [],
                'endpoint_path': '/data/device/statistics',
                'operation_id': 'get_statistics_type',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def generate_device_statistics_data(
        self,
        state_data_type,
        **kwargs
    ):
        """generate_device_statistics_data  # noqa: E501

        Get device statistics data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_device_statistics_data(state_data_type, async_req=True)
        >>> result = thread.get()

        Args:
            state_data_type (str): State data type

        Keyword Args:
            scroll_id (str): Scroll Id. [optional]
            start_date (str): Start date. [optional]
            end_date (str): End date. [optional]
            count (int): [optional]
            time_zone (str): Time zone. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['state_data_type'] = \
            state_data_type
        return self.generate_device_statistics_data_endpoint.call_with_http_info(**kwargs)

    def get_active_alarms(
        self,
        scroll_id,
        **kwargs
    ):
        """get_active_alarms  # noqa: E501

        Get active alarms  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_active_alarms(scroll_id, async_req=True)
        >>> result = thread.get()

        Args:
            scroll_id (str): SrollId

        Keyword Args:
            start_date (str): Start date. [optional]
            end_date (str): End date. [optional]
            count (int): count. [optional]
            time_zone (str): Time zone. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['scroll_id'] = \
            scroll_id
        return self.get_active_alarms_endpoint.call_with_http_info(**kwargs)

    def get_count_with_state_data_type(
        self,
        state_data_type,
        start_date,
        end_date,
        **kwargs
    ):
        """get_count_with_state_data_type  # noqa: E501

        Get response count of a query  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_count_with_state_data_type(state_data_type, start_date, end_date, async_req=True)
        >>> result = thread.get()

        Args:
            state_data_type (str): State data type(example:object)
            start_date (str): Start date (example:2021-1-1T00:00:00)
            end_date (str): End date (example:2021-12-1T00:00:00)

        Keyword Args:
            time_zone (str): Time zone (example:UTC). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['state_data_type'] = \
            state_data_type
        kwargs['start_date'] = \
            start_date
        kwargs['end_date'] = \
            end_date
        return self.get_count_with_state_data_type_endpoint.call_with_http_info(**kwargs)

    def get_stat_data_fields_by_state_data_type(
        self,
        state_data_type,
        **kwargs
    ):
        """get_stat_data_fields_by_state_data_type  # noqa: E501

        Get statistics fields and types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_stat_data_fields_by_state_data_type(state_data_type, async_req=True)
        >>> result = thread.get()

        Args:
            state_data_type (str): State data type

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['state_data_type'] = \
            state_data_type
        return self.get_stat_data_fields_by_state_data_type_endpoint.call_with_http_info(**kwargs)

    def get_statistics_type(
        self,
        **kwargs
    ):
        """get_statistics_type  # noqa: E501

        Get statistics types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_statistics_type(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_statistics_type_endpoint.call_with_http_info(**kwargs)

