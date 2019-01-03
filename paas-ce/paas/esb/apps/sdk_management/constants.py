# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
Copyright (C) 2017-2018 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
""" # noqa


COLLECTIONS_PY_TMPL = '''# -*- coding: utf-8 -*-
"""Collections for component client"""
{{ import_collections }}


# Available components
AVAILABLE_COLLECTIONS = {
{{ available_collections }}
}

'''

API_PY_TMPL = '''# -*- coding: utf-8 -*-
from ..base import ComponentAPI


class Collections{{ system_name_smart }}(object):
    """Collections of {{ system_name }} APIS"""

    def __init__(self, client):
        self.client = client

{{ apis }}
'''


API_COMPONENT_TMPL = '''\
        self.{api_name} = ComponentAPI(
            client=self.client, method='{suggest_method}',
            path='{api_path}',
            description=u'{description}'
        )
'''
