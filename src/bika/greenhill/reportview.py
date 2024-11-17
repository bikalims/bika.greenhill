from bika.coa.reportview import MultiReportView as MRV
from bika.coa.reportview import SingleReportView as SRV


class SingleReportView(SRV):
    """My specific controller view for multi-reports
    """

    def __init__(self, model, request):
        super(SingleReportView, self).__init__(model, request)
        # always provide a collection for simplicity
        self.collection = [model]
        self.model = model
        self.request = request


class MultiReportView(MRV):
    """My specific controller view for multi-reports
    """

    def __init__(self, collection, request):
        super(MultiReportView, self).__init__(collection, request)
        self.collection = collection
        self.request = request
