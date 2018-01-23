# -*- coding: utf-8 -*-

###################################################################################
#
#    Copyright (C) 2018 GFP SOLUTIONS LLC
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################
{
    'name': 'Braintree Payment Capture on Sale Order',
    'category': 'Hidden',
    'author': 'GFP Solutions LLC',
    'summary': 'Braintree Implementation',
    'version': '1.0',
    "website": "https://www.gfpsolutions.com",
    'description': """
    THIS MODULE IS PROVIDED AS IS - INSTALLATION AT USERS' OWN RISK - AUTHOR OF MODULE DOES NOT CLAIM ANY
    RESPONSIBILITY FOR ANY BEHAVIOR ONCE INSTALLED.
    Server Requirements:
    wget https://pypi.python.org/packages/fc/dd/4550c5820d2ec63f99f3410c9f07195768500c36e8f74a018c4fb1bd1252/braintree-3.39.1.tar.gz#md5=da65499398f362b205e3fb0c73eec2b2
    tar zxf braintree-3.39.1.tar.gz
    cd braintree-3.39.1
    python setup.py install
    """,
    'depends': ['payment'],
    'data': [
        'views/ir_ui_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
}
