from drf_writable_nested import NestedCreateMixin, NestedUpdateMixin


class ActionPermissionMixin:
    """Mixin which allows to define specific permissions per actions

    It requires filled ``action_permission_classes`` attribute

    It should be used for ``ModelViewSet``

    Examples:

        class NoteViewSet(ActionPermissionsMixin, viewsets.ModelViewSet):
            queryset = Note.objects.all()
            serializer_class = NoteSerializer
            action_permission_classes = {
                "list": [IsOwner],
                "update": [CanModerate, IsOwner],
                ...
            }
    """
    action_permission_classes = {}

    def get_permissions(self):
        if hasattr(self, 'action_permission_classes'):
            try:
                permission_classes = self.action_permission_classes[self.action]  # noqa
                return [permission_class() for permission_class in permission_classes]  # noqa
            except KeyError:
                pass
        return super().get_permissions()


class NestedCreateUpdateMixin(NestedCreateMixin, NestedUpdateMixin):
    """Help create/update nested objects implicitly."""
    pass
