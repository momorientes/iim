"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'ihdb2.admin_dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name



class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        # append an app list module for "Applications"
        from infos.models import MOTDMessage
        from django.template.defaultfilters import linebreaksbr
        self.children.append(modules.DashboardModule(
            column=1,
            title="MOTD",
            collapsible=False,
            pre_content="<ul>" +  '<hr>'.join(['<li><strong>&nbsp;{}</strong><br/> {}</li>'.format(obj.subject, linebreaksbr(obj.content)) for obj in MOTDMessage.objects.filter(display=True)]) + "</ul>")
        )

        self.children.append(modules.AppList(
            _('Tools'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            exclude=('django.contrib.*',),
        ))
        
        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('ModelList: Administration'),
            column=1,
            collapsible=False,
            models=('django.contrib.*',),
        ))
        
        # append another link list module for "support".
        from infos.models import LinkList
        self.children.append(modules.LinkList(
            _('Link List'),
            column=2,
            children=[
                {
                    'title': obj.name, 
                    'url': obj.url, 
                    'external': True,
                } for obj in LinkList.objects.all() if obj.display_on_dashboard
            ]
        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


