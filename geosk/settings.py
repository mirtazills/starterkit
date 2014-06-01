# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
from geonode.settings import *
#
# General Django development settings
#

# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "geosk.wsgi.application"


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# MEDIA_ROOT = os.path.join(LOCAL_ROOT, "uploaded")

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
# STATIC_ROOT = os.path.join(LOCAL_ROOT, "static_root")

# Additional directories which hold static files
STATICFILES_DIRS.append(
   os.path.join(LOCAL_ROOT, "static"),
)

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

# Location of url mappings
ROOT_URLCONF = 'geosk.urls'

LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS


LANGUAGES = (
    ('en', 'English'),
    ('it', 'Italiano'),
)

INSTALLED_APPS = (
    # GeoSK
    # 'geosk.rndt',
    'geosk.osk',
    'geosk.mdtools',
    'geosk.geoskbase',
    'geosk.search',
    'geosk.patches',
    'geosk.skregistration',
    'overextends', # https://github.com/stephenmcd/django-overextends
    'rosetta',
    'grappelli.dashboard',
    'grappelli',

    # Apps bundled with Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.humanize',

    # Third party apps

    # Utility
    'pagination',
    'taggit',
    'taggit_templatetags',
    'south',
    'friendlytagloader',
    'geoexplorer',
    'django_extensions',

    # Theme
    "pinax_theme_bootstrap_account",
    "pinax_theme_bootstrap",
    'django_forms_bootstrap',

    # Social
    'account',
    'avatar',
    'dialogos',
    'agon_ratings',
    'notification',
    'announcements',
    'actstream',
    'user_messages',

    # GeoNode internal apps
    'geonode.people',
    'geonode.base',
    'geonode.layers',
    'geonode.upload',
    'geonode.maps',
    'geonode.proxy',
    'geonode.security',
    'geonode.search',
    'geonode.social',
    'geonode.catalogue',
    'geonode.documents',

)

METADATA_DEFAULT_VALUES = {
    'category': 'environment',
    'language': 'ita',
    'regions': ['ITA']
}


DEFAULT_TOPICCATEGORY = METADATA_DEFAULT_VALUES['category']

# rosetta
ROSETTA_WSGI_AUTO_RELOAD = True
# ROSETTA_EXCLUDED_APPLICATIONS = ('geonode',)

# grappelli
GRAPPELLI_ADMIN_TITLE = "Starter Kit - Admin"
GRAPPELLI_INDEX_DASHBOARD = 'geosk.dashboard.CustomIndexDashboard'

# add skregistration context processor
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    "django.core.context_processors.tz",
    'django.core.context_processors.media',
    "django.core.context_processors.static",
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'account.context_processors.account',
    'pinax_theme_bootstrap_account.context_processors.theme',
    # The context processor below adds things like SITEURL
    # and GEOSERVER_BASE_URL to all pages that use a RequestContext
    'geonode.context_processors.resource_urls',
    # skregistraion
    'geosk.skregistration.context_processors.skregistration',
)

#RITMARE services
RITMARE = {
    'MDSERVICE': 'https://sp7.irea.cnr.it/jboss/MDService/rest/' # postMetadata, auth/register, auth/verify
    }

# Load more settings from a file called local_settings.py if it exists
try:
    from local_settings import *
except ImportError:
    pass
