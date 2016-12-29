#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Solutions Website
# Copyright (c) 2008-2017 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2017 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Hive Solutions Confidential Usage License (HSCUL)"
""" The license for the module """

import sys

def u(value, encoding = "utf-8"):
    if sys.version_info[0] >= 3: return value
    return value.decode(encoding)

configuration = {
    "user_information" : {
        "admin" : {
            "name" : u("System Administrator"),
            "first_name" : u("System"),
            "last_name" : u("Administrator"),
            "email" : u("admin@hive.pt"),
            "username" : u("admin"),
            "website" : u("http://hive.pt"),
            "description" : u("The global system administrator of the system"),
            "images" : {
                "gravatar" : u("http://www.gravatar.com/avatar/639590e6cd348a5581826da23b78511a")
            },
            "social" : {
                "gravatar" : u("http://gravatar.com/admin"),
                "facebook" : u("http://facebook.com/admin"),
                "twitter" : u("http://twitter.com/admin"),
            },
            "work" : {
                "company" : u("Hive Solutions"),
                "position" : u("Software Developer"),
                "email" : u("admin@hive.pt"),
                "address" : {
                    "street" : u("Rua 31 de Janeiro, 190A 3º Dto."),
                    "zip_code" : u("4000-542"),
                    "city" : u("Porto"),
                    "country" : u("Portugal"),
                }
            }
        },
        "joamag" : {
            "name" : u("João Magalhães"),
            "first_name" : u("João"),
            "last_name" : u("Magalhães"),
            "email" : u("joamag@hive.pt"),
            "username" : u("joamag"),
            "website" : u("http://joaomagalhaes.eu"),
            "description" : u("Enthusiasm driven software developer, programming language devourer"),
            "images" : {
                "gravatar" : u("http://www.gravatar.com/avatar/639590e6cd348a5581826da23b78511a")
            },
            "social" : {
                "gravatar" : u("http://gravatar.com/joamag"),
                "facebook" : u("http://facebook.com/joamag"),
                "twitter" : u("http://twitter.com/joamag"),
            },
            "work" : {
                "company" : u("Hive Solutions"),
                "position" : u("Software Developer"),
                "email" : u("joamag@hive.pt"),
                "address" : {
                    "street" : u("Rua 31 de Janeiro, 190A 3º Dto."),
                    "zip_code" : u("4000-542"),
                    "city" : u("Porto"),
                    "country" : u("Portugal"),
                }
            }
        },
        "tsilva" : {
            "name" : u("Tiago Silva"),
            "first_name" : u("Tiago"),
            "last_name" : u("Silva"),
            "email" : u("tsilva@hive.pt"),
            "username" : u("tsilva"),
            "website" : u("http://tiagosilva.me"),
            "description" : u("A diversified multi-cultural post-modern deconstructionist"),
            "images" : {
                "gravatar" : u("http://www.gravatar.com/avatar/b2e064935878cfd489107331aaa296d3")
            },
            "social" : {
                "facebook" : u("http://facebook.com/eng.tiago.silva"),
                "twitter" : u("http://twitter.com/tiagosilva"),
            },
            "work" : {
                "company" : u("Hive Solutions"),
                "position" : u("Software Developer"),
                "email" : u("tsilva@hive.pt"),
                "address" : {
                    "street" : u("Rua 31 de Janeiro, 190A 3º Dto."),
                    "zip_code" : u("4000-542"),
                    "city" : u("Porto"),
                    "country" : u("Portugal"),
                }
            }
        },
        "lmartinho" : {
            "name" : u("Luis Martinho"),
            "first_name" : u("Luis"),
            "last_name" : u("Martinho"),
            "email" : u("lmartinho@hive.pt"),
            "username" : u("lmartinho"),
            "website" : u("http://luismartinho.com"),
            "description" : u("Software Craftsman, I build stuff"),
            "images" : {
                "gravatar" : u("http://www.gravatar.com/avatar/8262b6b2a430566de13df6da0c481846")
            },
            "social" : {
                "facebook" : u("http://facebook.com/lmartinho"),
                "twitter" : u("http://twitter.com/lmartinho"),
            },
            "work" : {
                "company" : u("Hive Solutions"),
                "position" : u("Software Developer"),
                "email" : u("lmartinho@hive.pt"),
                "address" : {
                    "street" : u("Rua 31 de Janeiro, 190A 3º Dto."),
                    "zip_code" : u("4000-542"),
                    "city" : u("Porto"),
                    "country" : u("Portugal"),
                }
            }
        },
        "v-fcastro" : {
            "name" : u("Francisco Castro"),
            "first_name" : u("Francisco"),
            "last_name" : u("Castro"),
            "email" : u("v-fcastro@hive.pt"),
            "username" : u("v-fcastro"),
            "description" : u("Work in progress..."),
            "images" : {
                "gravatar" : u("http://www.gravatar.com/avatar/e8f4b05866847b6d9e9638c40ce77d93")
            },
            "social" : {
                "facebook" : u("http://facebook.com/castromatic"),
                "twitter" : u("http://twitter.com/frcastro"),
            },
            "work" : {
                "company" : u("Hive Solutions"),
                "position" : u("Designer"),
                "email" : u("v-fcastro@hive.pt"),
                "address" : {
                    "street" : u("Rua 31 de Janeiro, 190A 3º Dto."),
                    "zip_code" : u("4000-542"),
                    "city" : u("Porto"),
                    "country" : u("Portugal"),
                }
            }
        },
        "v-msousa" : {
            "name" : u("Marco Sousa"),
            "first_name" : u("Marco"),
            "last_name" : u("Sousa"),
            "email" : u("v-msousa@hive.pt"),
            "username" : u("v-msousa"),
            "website" : u("http://marcosousa.me"),
            "description" : u("Visual Designer & Web Design"),
            "images" : {
                "gravatar" : u("http://www.gravatar.com/avatar/e7f7880c089f0d104df7f088dbc213e9")
            },
            "social" : {
                "facebook" : u("http://facebook.com/sousa.marco"),
                "twitter" : u("http://twitter.com/h1brd"),
                "dribbble" : u("http://dribbble.com/h1brd"),
            },
            "work" : {
                "company" : u("Hive Solutions"),
                "position" : u("Designer"),
                "email" : u("v-msousa@hive.pt"),
                "address" : {
                    "street" : u("Rua 31 de Janeiro, 190A 3º Dto."),
                    "zip_code" : u("4000-542"),
                    "city" : u("Porto"),
                    "country" : u("Portugal"),
                }
            }
        }
    }
}
