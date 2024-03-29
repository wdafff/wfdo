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
from tencentcloud.zj.v20190121 import models


class ZjClient(AbstractClient):
    _apiVersion = '2019-01-21'
    _endpoint = 'zj.tencentcloudapi.com'
    _service = 'zj'


    def AddCrowdPackInfo(self, request):
        """添加短信人群包信息

        :param request: Request instance for AddCrowdPackInfo.
        :type request: :class:`tencentcloud.zj.v20190121.models.AddCrowdPackInfoRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.AddCrowdPackInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCrowdPackInfo", params, headers=headers)
            response = json.loads(body)
            model = models.AddCrowdPackInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddSmsSign(self, request):
        """创建普通短信签名信息

        :param request: Request instance for AddSmsSign.
        :type request: :class:`tencentcloud.zj.v20190121.models.AddSmsSignRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.AddSmsSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddSmsSign", params, headers=headers)
            response = json.loads(body)
            model = models.AddSmsSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddSmsTemplate(self, request):
        """根据短信标题、模板内容等创建短信模板

        :param request: Request instance for AddSmsTemplate.
        :type request: :class:`tencentcloud.zj.v20190121.models.AddSmsTemplateRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.AddSmsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddSmsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.AddSmsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelCampaign(self, request):
        """取消短信推送活动

        :param request: Request instance for CancelCampaign.
        :type request: :class:`tencentcloud.zj.v20190121.models.CancelCampaignRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.CancelCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.CancelCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCampaign(self, request):
        """创建短信推送活动

        :param request: Request instance for CreateCampaign.
        :type request: :class:`tencentcloud.zj.v20190121.models.CreateCampaignRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.CreateCampaignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCampaign", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCampaignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMmsInstance(self, request):
        """创建超级短信的素材样例内容

        :param request: Request instance for CreateMmsInstance.
        :type request: :class:`tencentcloud.zj.v20190121.models.CreateMmsInstanceRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.CreateMmsInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMmsInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMmsInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DelCrowdPack(self, request):
        """删除人群包

        :param request: Request instance for DelCrowdPack.
        :type request: :class:`tencentcloud.zj.v20190121.models.DelCrowdPackRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.DelCrowdPackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DelCrowdPack", params, headers=headers)
            response = json.loads(body)
            model = models.DelCrowdPackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DelTemplate(self, request):
        """删除短信模板

        :param request: Request instance for DelTemplate.
        :type request: :class:`tencentcloud.zj.v20190121.models.DelTemplateRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.DelTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DelTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DelTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMmsInstance(self, request):
        """删除超级短信样例

        :param request: Request instance for DeleteMmsInstance.
        :type request: :class:`tencentcloud.zj.v20190121.models.DeleteMmsInstanceRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.DeleteMmsInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMmsInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMmsInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMmsInstanceInfo(self, request):
        """获取彩信实例信息

        :param request: Request instance for DescribeMmsInstanceInfo.
        :type request: :class:`tencentcloud.zj.v20190121.models.DescribeMmsInstanceInfoRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.DescribeMmsInstanceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMmsInstanceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMmsInstanceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMmsInstanceList(self, request):
        """获取彩信实例列表

        :param request: Request instance for DescribeMmsInstanceList.
        :type request: :class:`tencentcloud.zj.v20190121.models.DescribeMmsInstanceListRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.DescribeMmsInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMmsInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMmsInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSmsCampaignStatistics(self, request):
        """获取短信超短活动统计数据

        :param request: Request instance for DescribeSmsCampaignStatistics.
        :type request: :class:`tencentcloud.zj.v20190121.models.DescribeSmsCampaignStatisticsRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.DescribeSmsCampaignStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmsCampaignStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmsCampaignStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSmsSignList(self, request):
        """获取普通短信签名信息

        :param request: Request instance for DescribeSmsSignList.
        :type request: :class:`tencentcloud.zj.v20190121.models.DescribeSmsSignListRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.DescribeSmsSignListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmsSignList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmsSignListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSmsTemplateList(self, request):
        """获取模板信息

        :param request: Request instance for DescribeSmsTemplateList.
        :type request: :class:`tencentcloud.zj.v20190121.models.DescribeSmsTemplateListRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.DescribeSmsTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmsTemplateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmsTemplateListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCrowdPackList(self, request):
        """获取人群包列表接口

        :param request: Request instance for GetCrowdPackList.
        :type request: :class:`tencentcloud.zj.v20190121.models.GetCrowdPackListRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.GetCrowdPackListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCrowdPackList", params, headers=headers)
            response = json.loads(body)
            model = models.GetCrowdPackListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCrowdUploadInfo(self, request):
        """获取短信人群包cos上传需要的信息

        :param request: Request instance for GetCrowdUploadInfo.
        :type request: :class:`tencentcloud.zj.v20190121.models.GetCrowdUploadInfoRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.GetCrowdUploadInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCrowdUploadInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetCrowdUploadInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSmsAmountInfo(self, request):
        """获取账号短信额度配置信息

        :param request: Request instance for GetSmsAmountInfo.
        :type request: :class:`tencentcloud.zj.v20190121.models.GetSmsAmountInfoRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.GetSmsAmountInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSmsAmountInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetSmsAmountInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSmsCampaignStatus(self, request):
        """获取短信活动状态信息

        :param request: Request instance for GetSmsCampaignStatus.
        :type request: :class:`tencentcloud.zj.v20190121.models.GetSmsCampaignStatusRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.GetSmsCampaignStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSmsCampaignStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetSmsCampaignStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySmsTemplate(self, request):
        """对未审核或者审核未通过的短信模板内容进行编辑修改

        :param request: Request instance for ModifySmsTemplate.
        :type request: :class:`tencentcloud.zj.v20190121.models.ModifySmsTemplateRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.ModifySmsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySmsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySmsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PushMmsContent(self, request):
        """推送超级短信

        :param request: Request instance for PushMmsContent.
        :type request: :class:`tencentcloud.zj.v20190121.models.PushMmsContentRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.PushMmsContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PushMmsContent", params, headers=headers)
            response = json.loads(body)
            model = models.PushMmsContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendSms(self, request):
        """发送短信

        :param request: Request instance for SendSms.
        :type request: :class:`tencentcloud.zj.v20190121.models.SendSmsRequest`
        :rtype: :class:`tencentcloud.zj.v20190121.models.SendSmsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendSms", params, headers=headers)
            response = json.loads(body)
            model = models.SendSmsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))