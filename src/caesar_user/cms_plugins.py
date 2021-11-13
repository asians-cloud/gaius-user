from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

@plugin_pool.register_plugin
class UserPlugin(CMSPluginBase):
    model = CMSPlugin
    name = 'User Plugin'
    render_template = "user_plugin.html"
    cache = False
    allow_children = False
