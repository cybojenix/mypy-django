# Stubs for django.contrib.admin.options (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.utils.translation import ugettext as _

IS_POPUP_VAR = ...  # type: str
TO_FIELD_VAR = ...  # type: str
HORIZONTAL = ...  # type: Any
VERTICAL = ...  # type: Any

def get_content_type_for_model(obj): ...
def get_ul_class(radio_style): ...

class IncorrectLookupParameters(Exception): ...

FORMFIELD_FOR_DBFIELD_DEFAULTS = ...  # type: Any
csrf_protect_m = ...  # type: Any

class BaseModelAdmin:
    raw_id_fields = ...  # type: Any
    fields = ...  # type: Any
    exclude = ...  # type: Any
    fieldsets = ...  # type: Any
    form = ...  # type: Any
    filter_vertical = ...  # type: Any
    filter_horizontal = ...  # type: Any
    radio_fields = ...  # type: Any
    prepopulated_fields = ...  # type: Any
    formfield_overrides = ...  # type: Any
    readonly_fields = ...  # type: Any
    ordering = ...  # type: Any
    view_on_site = ...  # type: bool
    show_full_result_count = ...  # type: bool
    checks_class = ...  # type: Any
    def check(self, **kwargs): ...
    def __init__(self) -> None: ...
    def formfield_for_dbfield(self, db_field, **kwargs): ...
    def formfield_for_choice_field(self, db_field, request: Optional[Any] = ..., **kwargs): ...
    def get_field_queryset(self, db, db_field, request): ...
    def formfield_for_foreignkey(self, db_field, request: Optional[Any] = ..., **kwargs): ...
    def formfield_for_manytomany(self, db_field, request: Optional[Any] = ..., **kwargs): ...
    def get_view_on_site_url(self, obj: Optional[Any] = ...): ...
    def get_empty_value_display(self): ...
    def get_fields(self, request, obj: Optional[Any] = ...): ...
    def get_fieldsets(self, request, obj: Optional[Any] = ...): ...
    def get_ordering(self, request): ...
    def get_readonly_fields(self, request, obj: Optional[Any] = ...): ...
    def get_prepopulated_fields(self, request, obj: Optional[Any] = ...): ...
    def get_queryset(self, request): ...
    def lookup_allowed(self, lookup, value): ...
    def to_field_allowed(self, request, to_field): ...
    def has_add_permission(self, request): ...
    def has_change_permission(self, request, obj: Optional[Any] = ...): ...
    def has_delete_permission(self, request, obj: Optional[Any] = ...): ...
    def has_module_permission(self, request): ...

class ModelAdmin(BaseModelAdmin):
    list_display = ...  # type: Any
    list_display_links = ...  # type: Any
    list_filter = ...  # type: Any
    list_select_related = ...  # type: bool
    list_per_page = ...  # type: int
    list_max_show_all = ...  # type: int
    list_editable = ...  # type: Any
    search_fields = ...  # type: Any
    date_hierarchy = ...  # type: Any
    save_as = ...  # type: bool
    save_on_top = ...  # type: bool
    paginator = ...  # type: Any
    preserve_filters = ...  # type: bool
    inlines = ...  # type: Any
    add_form_template = ...  # type: Any
    change_form_template = ...  # type: Any
    change_list_template = ...  # type: Any
    delete_confirmation_template = ...  # type: Any
    delete_selected_confirmation_template = ...  # type: Any
    object_history_template = ...  # type: Any
    actions = ...  # type: Any
    action_form = ...  # type: Any
    actions_on_top = ...  # type: bool
    actions_on_bottom = ...  # type: bool
    actions_selection_counter = ...  # type: bool
    checks_class = ...  # type: Any
    model = ...  # type: Any
    opts = ...  # type: Any
    admin_site = ...  # type: Any
    def __init__(self, model, admin_site) -> None: ...
    def get_inline_instances(self, request, obj: Optional[Any] = ...): ...
    def get_urls(self): ...
    def urls(self): ...
    urls = ...  # type: Any
    @property
    def media(self): ...
    def get_model_perms(self, request): ...
    def get_fields(self, request, obj: Optional[Any] = ...): ...
    def get_form(self, request, obj: Optional[Any] = ..., **kwargs): ...
    def get_changelist(self, request, **kwargs): ...
    def get_object(self, request, object_id, from_field: Optional[Any] = ...): ...
    def get_changelist_form(self, request, **kwargs): ...
    def get_changelist_formset(self, request, **kwargs): ...
    def get_formsets_with_inlines(self, request, obj: Optional[Any] = ...): ...
    def get_paginator(self, request, queryset, per_page, orphans: int = ..., allow_empty_first_page: bool = ...): ...
    def log_addition(self, request, object, message): ...
    def log_change(self, request, object, message): ...
    def log_deletion(self, request, object, object_repr): ...
    def action_checkbox(self, obj): ...
    def get_actions(self, request): ...
    def get_action_choices(self, request, default_choices: Any = ...): ...
    def get_action(self, action): ...
    def get_list_display(self, request): ...
    def get_list_display_links(self, request, list_display): ...
    def get_list_filter(self, request): ...
    def get_list_select_related(self, request): ...
    def get_search_fields(self, request): ...
    def get_search_results(self, request, queryset, search_term): ...
    def get_preserved_filters(self, request): ...
    def construct_change_message(self, request, form, formsets, add: bool = ...): ...
    def message_user(self, request, message, level: Any = ..., extra_tags: str = ..., fail_silently: bool = ...): ...
    def save_form(self, request, form, change): ...
    def save_model(self, request, obj, form, change): ...
    def delete_model(self, request, obj): ...
    def save_formset(self, request, form, formset, change): ...
    def save_related(self, request, form, formsets, change): ...
    def render_change_form(self, request, context, add: bool = ..., change: bool = ..., form_url: str = ..., obj: Optional[Any] = ...): ...
    def response_add(self, request, obj, post_url_continue: Optional[Any] = ...): ...
    def response_change(self, request, obj): ...
    def response_post_save_add(self, request, obj): ...
    def response_post_save_change(self, request, obj): ...
    def response_action(self, request, queryset): ...
    def response_delete(self, request, obj_display, obj_id): ...
    def render_delete_form(self, request, context): ...
    def get_inline_formsets(self, request, formsets, inline_instances, obj: Optional[Any] = ...): ...
    def get_changeform_initial_data(self, request): ...
    def changeform_view(self, request, object_id: Optional[Any] = ..., form_url: str = ..., extra_context: Optional[Any] = ...): ...
    def add_view(self, request, form_url: str = ..., extra_context: Optional[Any] = ...): ...
    def change_view(self, request, object_id, form_url: str = ..., extra_context: Optional[Any] = ...): ...
    def changelist_view(self, request, extra_context: Optional[Any] = ...): ...
    def delete_view(self, request, object_id, extra_context: Optional[Any] = ...): ...
    def history_view(self, request, object_id, extra_context: Optional[Any] = ...): ...

class InlineModelAdmin(BaseModelAdmin):
    model = ...  # type: Any
    fk_name = ...  # type: Any
    formset = ...  # type: Any
    extra = ...  # type: int
    min_num = ...  # type: Any
    max_num = ...  # type: Any
    template = ...  # type: Any
    verbose_name = ...  # type: Any
    verbose_name_plural = ...  # type: Any
    can_delete = ...  # type: bool
    show_change_link = ...  # type: bool
    checks_class = ...  # type: Any
    admin_site = ...  # type: Any
    parent_model = ...  # type: Any
    opts = ...  # type: Any
    has_registered_model = ...  # type: Any
    def __init__(self, parent_model, admin_site) -> None: ...
    @property
    def media(self): ...
    def get_extra(self, request, obj: Optional[Any] = ..., **kwargs): ...
    def get_min_num(self, request, obj: Optional[Any] = ..., **kwargs): ...
    def get_max_num(self, request, obj: Optional[Any] = ..., **kwargs): ...
    def get_formset(self, request, obj: Optional[Any] = ..., **kwargs): ...
    def get_fields(self, request, obj: Optional[Any] = ...): ...
    def get_queryset(self, request): ...
    def has_add_permission(self, request): ...
    def has_change_permission(self, request, obj: Optional[Any] = ...): ...
    def has_delete_permission(self, request, obj: Optional[Any] = ...): ...

class StackedInline(InlineModelAdmin):
    template = ...  # type: str

class TabularInline(InlineModelAdmin):
    template = ...  # type: str