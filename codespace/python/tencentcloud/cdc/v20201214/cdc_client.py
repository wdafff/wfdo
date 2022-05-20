# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cdc.v20201214 import models


class CdcClient(AbstractClient):
    _apiVersion = '2020-12-14'
    _endpoint = 'cdc.tencentcloudapi.com'
    _service = 'cdc'


    def CreateDedicatedCluster(self, request):
        """创建专用集群

        :param request: Request instance for CreateDedicatedCluster.
        :type request: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDedicatedCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDedicatedClusterResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDedicatedClusterOrder(self, request):
        """创建专用集群订单

        :param request: Request instance for CreateDedicatedClusterOrder.
        :type request: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterOrderRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CreateDedicatedClusterOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDedicatedClusterOrder", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDedicatedClusterOrderResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSite(self, request):
        """创建站点

        :param request: Request instance for CreateSite.
        :type request: :class:`tencentcloud.cdc.v20201214.models.CreateSiteRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.CreateSiteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSite", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSiteResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDedicatedClusters(self, request):
        """删除专用集群

        :param request: Request instance for DeleteDedicatedClusters.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DeleteDedicatedClustersRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DeleteDedicatedClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDedicatedClusters", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDedicatedClustersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSites(self, request):
        """删除站点

        :param request: Request instance for DeleteSites.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DeleteSitesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DeleteSitesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSites", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSitesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDedicatedClusterCosCapacity(self, request):
        """查询专用集群内cos的容量信息

        :param request: Request instance for DescribeDedicatedClusterCosCapacity.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterCosCapacityRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterCosCapacityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterCosCapacity", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDedicatedClusterCosCapacityResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDedicatedClusterHostStatistics(self, request):
        """查询专用集群内宿主机的统计信息

        :param request: Request instance for DescribeDedicatedClusterHostStatistics.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterHostStatisticsRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterHostStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterHostStatistics", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDedicatedClusterHostStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDedicatedClusterHosts(self, request):
        """专用集群宿主机信息

        :param request: Request instance for DescribeDedicatedClusterHosts.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterHostsRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterHosts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDedicatedClusterHostsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDedicatedClusterInstanceTypes(self, request):
        """查询专用集群支持的实例规格列表

        :param request: Request instance for DescribeDedicatedClusterInstanceTypes.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterInstanceTypesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterInstanceTypes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDedicatedClusterInstanceTypesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDedicatedClusterOrders(self, request):
        """查询专用集群订单列表

        :param request: Request instance for DescribeDedicatedClusterOrders.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterOrdersRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterOrdersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterOrders", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDedicatedClusterOrdersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDedicatedClusterOverview(self, request):
        """专用集群概览信息

        :param request: Request instance for DescribeDedicatedClusterOverview.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterOverviewRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterOverview", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDedicatedClusterOverviewResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDedicatedClusterTypes(self, request):
        """查询专有集群配置列表

        :param request: Request instance for DescribeDedicatedClusterTypes.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterTypesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClusterTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusterTypes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDedicatedClusterTypesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDedicatedClusters(self, request):
        """查询专用集群列表

        :param request: Request instance for DescribeDedicatedClusters.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClustersRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusters", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDedicatedClustersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDedicatedSupportedZones(self, request):
        """查询专用集群支持的可用区列表

        :param request: Request instance for DescribeDedicatedSupportedZones.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedSupportedZonesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeDedicatedSupportedZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedSupportedZones", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDedicatedSupportedZonesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSites(self, request):
        """查询站点列表

        :param request: Request instance for DescribeSites.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeSitesRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeSitesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSites", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSitesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSitesDetail(self, request):
        """查询站点详情

        :param request: Request instance for DescribeSitesDetail.
        :type request: :class:`tencentcloud.cdc.v20201214.models.DescribeSitesDetailRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.DescribeSitesDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSitesDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSitesDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDedicatedClusterInfo(self, request):
        """修改本地专用集群信息

        :param request: Request instance for ModifyDedicatedClusterInfo.
        :type request: :class:`tencentcloud.cdc.v20201214.models.ModifyDedicatedClusterInfoRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.ModifyDedicatedClusterInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDedicatedClusterInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDedicatedClusterInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyOrderStatus(self, request):
        """修改大订单、小订单的状态

        :param request: Request instance for ModifyOrderStatus.
        :type request: :class:`tencentcloud.cdc.v20201214.models.ModifyOrderStatusRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.ModifyOrderStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOrderStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyOrderStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySiteDeviceInfo(self, request):
        """修改机房设备信息

        :param request: Request instance for ModifySiteDeviceInfo.
        :type request: :class:`tencentcloud.cdc.v20201214.models.ModifySiteDeviceInfoRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.ModifySiteDeviceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySiteDeviceInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySiteDeviceInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySiteInfo(self, request):
        """修改机房信息

        :param request: Request instance for ModifySiteInfo.
        :type request: :class:`tencentcloud.cdc.v20201214.models.ModifySiteInfoRequest`
        :rtype: :class:`tencentcloud.cdc.v20201214.models.ModifySiteInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySiteInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySiteInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)