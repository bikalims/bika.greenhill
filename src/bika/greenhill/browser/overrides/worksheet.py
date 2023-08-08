# -*- coding: utf-8 -*-

from bika.greenhill import _
from bika.greenhill import is_installed
from bika.lims.browser.worksheet.views.analyses import AnalysesView as AV


class AnalysesView(AV):
    def before_render(self):
        if not is_installed():
            return
        unit = ("Unit", {
                "title": _("Unit"),
                "sortable": False,
                "ajax": True,
                "on_change": "_on_unit_change",
                "toggle": True}),
        self.columns.update(unit)

    def folder_item(self, obj, item, index):
        if not is_installed():
            return item
        return item
