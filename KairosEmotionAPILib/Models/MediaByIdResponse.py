# -*- coding: utf-8 -*-

"""
   KairosEmotionAPILib.Models.MediaByIdResponse
 
   This file was automatically generated for kairos by APIMATIC BETA v2.0 on 01/15/2016
"""
from KairosEmotionAPILib.APIHelper import APIHelper

class MediaByIdResponse(object):

    """Implementation of the 'MediaById response' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        status_code (string): TODO: type description here.
        status_message (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the MediaByIdResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    id -- string -- Sets the attribute id
                    status_code -- string -- Sets the attribute status_code
                    status_message -- string -- Sets the attribute status_message
        
        """
        # Set all of the parameters to their default values
        self.status = None
        self.length = None
        self.media_id = None
        self.frames = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "status": "status",
            "length": "length",
            "media_id": "media_id",
            "frames": "frames",
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
            "status": "status",
            "length": "length",
            "media_id": "media_id",
            "frames": "frames",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)