from django.utils.translation import ugettext_lazy as _

from grappelli.dashboard import modules, Dashboard


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        # append an app list module for "Applications"
        from infos.models import MOTDMessage
        from django.template.defaultfilters import linebreaksbr
        self.children.append(modules.DashboardModule(
            column=1,
            title="MOTD",
            collapsible=False,
            pre_content='<ul class="grp-listing-small">' + '<hr>'.join(
                ['<li class="grp-row"><h5><strong>{}</strong></h5> {}</li>'.format(
                    obj.subject, linebreaksbr(obj.content))
                    for obj in MOTDMessage.objects.filter(display=True)]) + "</ul>")
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
