#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Solutions Website
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Solutions Website.
#
# Hive Solutions Website is confidential and property of Hive Solutions Lda.,
# its usage is constrained by the terms of the Hive Solutions
# Confidential Usage License.
#
# Hive Solutions Website should not be distributed under any circumstances,
# violation of this may imply legal action.
#
# If you have any questions regarding the terms of this license please
# refer to <http://www.hive.pt/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Hive Solutions Confidential Usage License (HSCUL)"
""" The license for the module """

configuration = {
    "default_end_points" : [
        (
            "normal", "", 80, {}
        )
    ],
    "default_handler" : "file",
    "default_encoding" : None,
    "default_content_type_charset" : "utf-8",
    "default_service_type" : "async",
    "default_client_connection_timeout" : 3,
    "default_connection_timeout" : 30,
    "default_request_timeout" : 3,
    "default_response_timeout" : 30,
    "default_number_threads" : 1,
    "default_scheduling_algorithm" : 2,
    "default_maximum_number_threads" : 30,
    "default_maximum_number_work_threads" : 150,
    "default_work_scheduling_algorithm" : 3,
    "preferred_error_handlers" : [
        "template",
        "default"
    ],
    "verify_request" : False,
    "log_file_path" : "%configuration:pt.hive.colony.plugins.service.http%/access.log",
    "virtual_servers" : {
        "resolution_order" : [
            "hive.pt",
            "www.hive.pt",
            "blog.hive.pt",
            "openid.hive.pt",
            "getcolony.com"
        ],
        "hive.pt" : {
            "redirections" : {
                "resolution_order" : [
                    "/"
                ],
                "/" : {
                    "target" : "/dynamic/rest/mvc/hive_site/",
                    "recursive_redirection" : True
                }
            }
        },
        "www.hive.pt" : {
            "redirections" : {
                "resolution_order" : [
                    "/"
                ],
                "/" : {
                    "target" : "/dynamic/rest/mvc/hive_site/",
                    "recursive_redirection" : True
                }
            }
        },
        "blog.hive.pt" : {
            "redirections" : {
                "resolution_order" : [
                    "/"
                ],
                "/" : {
                    "target" : "/dynamic/rest/mvc/hive_blog/",
                    "recursive_redirection" : True
                }
            }
        },
        "openid.hive.pt" : {
            "redirections" : {
                "resolution_order" : [
                    "/"
                ],
                "/" : {
                    "target" : "/dynamic/rest/mvc/hive_openid/",
                    "recursive_redirection" : True
                }
            }
        },
        "getcolony.com" : {
            "redirections" : {
                "resolution_order" : [
                    "/"
                ],
                "/" : {
                    "target" : "/dynamic/rest/mvc/colony_site/",
                    "recursive_redirection" : True
                }
            }
        }
    },
    "redirections" : {
        "resolution_order" : [
            "/blog",
            "/openid",
            "/colony",
            "/"
        ],
        "/blog" : {
            "target" : "/dynamic/rest/mvc/hive_blog/",
            "recursive_redirection" : True
        },
        "/openid" : {
            "target" : "/dynamic/rest/mvc/hive_openid/",
            "recursive_redirection" : True
        },
        "/colony" : {
            "target" : "/dynamic/rest/mvc/colony_site/",
            "recursive_redirection" : True
        },
        "/" : {
            "target" : "/dynamic/rest/mvc/hive_site/",
            "recursive_redirection" : True
        }
    },
    "contexts" : {
        "resolution_order" : [
            "/dynamic"
        ],
        "/dynamic" : {
            "handler" : "colony",
            "allow_redirection" : False,
            "request_properties" : {}
        }
    }
}
