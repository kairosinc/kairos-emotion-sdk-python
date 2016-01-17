# -*- coding: utf-8 -*-

'''
 KairosEmotionAPILib

 This file was automatically generated for kairos by APIMATIC BETA v2.0 on 01/15/2016
'''
import unirest
from Configuration import *

class CustomAuthUtility:

    @staticmethod
    def appendCustomAuthParams(headers):
        '''
        Appends the necessary OAuth credentials for making this authorized call
		
		:param headers: The out going request to access the resource
		:type headers: dict
        '''

        headers["Content-Type"] = Configuration.content_type
        headers["app_id"]       = Configuration.app_id
        headers["app_key"]      = Configuration.app_key

        return headers