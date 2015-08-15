import reversion


class CreatedModifiedByModelMixin(object):
    @property
    def modified_by(self):
        version = reversion.get_for_object(self).first()
        return version.revision.user

    @property
    def created_by(self):
        version = reversion.get_for_object(self).last()
        return version.revision.user
