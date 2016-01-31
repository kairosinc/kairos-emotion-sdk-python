# -*- coding: utf-8 -*-

"""
   KairosEmotionAPILib.Controllers.EmotionAnalysisController

   This file was automatically generated for kairos by APIMATIC BETA v2.0 on 01/15/2016
"""
import unirest

from KairosEmotionAPILib.APIHelper import APIHelper
from KairosEmotionAPILib.Configuration import Configuration
from KairosEmotionAPILib.CustomAuthUtility import CustomAuthUtility
from KairosEmotionAPILib.APIException import APIException
from KairosEmotionAPILib.Models.MediaResponse import MediaResponse
from KairosEmotionAPILib.Models.MediaByIdResponse import MediaByIdResponse


class EmotionAnalysisController(object):

    # Prepare headers
    global headers
    headers = {
        "user-agent": "APIMATIC 2.0",
        "accept": "application/json"
    }

    """A Controller to access Endpoints in the KairosEmotionAPILib API."""

    def create_media(self,
                     source=None):
        """Does a POST request to /media.

        Create a new media object to be processed.

        Args:
            source (string, optional): The source URL of the media.

        Returns:
            MediaResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/media"

        # Process optional query parameters
        query_parameters = {
            "source": source,
            "timeout": Configuration.api_timeout
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        #append custom auth authorization
        CustomAuthUtility.appendCustomAuthParams(headers)

        def post_callback(response):
            self.delete_media_by_id(MediaByIdResponse(**response.body).id)
            print MediaByIdResponse(**response.body).frames

        # Prepare and invoke the API call request to fetch the response
        unirest.timeout(20)
        response = unirest.post(query_url, headers=headers, callback=post_callback)


    def delete_media_by_id(self,
                           id):
        """Does a DELETE request to /media/{id}.

        Delete media results. It returns the status of the operation.

        Args:
            id (string): The id of the media.

        Returns:
            MediaByIdResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/media/{id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "id": id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        #append custom auth authorization
        CustomAuthUtility.appendCustomAuthParams(headers)

        # Prepare and invoke the API call request to fetch the response
        unirest.timeout(20)
        response = unirest.delete(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            print response.body
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            print "Media ID Deleted"
        
        # # If we got here then an error occured while trying to parse the response
        # raise APIException("Invalid JSON returned", response.code, response.body) 
