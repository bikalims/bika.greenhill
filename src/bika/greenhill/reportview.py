from bika.coa.reportview import MultiReportView as MRV
from bika.coa.reportview import SingleReportView


class MultiReportView(MRV):
    """My specific controller view for multi-reports
    """

    def __init__(self, collection, request):
        super(MultiReportView, self).__init__(collection, request)
        self.collection = collection
        self.request = request
