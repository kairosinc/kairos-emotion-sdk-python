# -*- coding: utf-8 -*-

"""
   KairosEmotionAPILib.Models.MediaResponse
 
   This file was automatically generated for kairos by APIMATIC BETA v2.0 on 01/15/2016
"""
from KairosEmotionAPILib.APIHelper import APIHelper

class MediaResponse(object):

    """Implementation of the 'Media response' model.

    TODO: type model description here.

    Attributes:
        status_code (int): TODO: type description here.
        id (string): TODO: type description here.
        status_message (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the MediaResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    status_code -- int -- Sets the attribute status_code
                    id -- string -- Sets the attribute id
                    status_message -- string -- Sets the attribute status_message
        
        """
        # Set all of the parameters to their default values
        self.status_code = None
        self.id = None
        self.status_message = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "status_code": "status_code",
            "id": "id",
            "status_message": "status_message",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

    def resolve_names(self):
        """Creates a dictionary representation of this object.
        
        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.
        
        Returns:
            dict: The dictionary representing the object.
        
        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "status_code": "status_code",
            "id": "id",
            "status_message": "status_message",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)