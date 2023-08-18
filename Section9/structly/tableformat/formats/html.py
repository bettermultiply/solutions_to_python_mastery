from ..formatter import TableFormatter


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('<th>%s</th>' % h for h in headers))

    def row(self, rowdata):
        print(' '.join('<td>%s</td>' % r for r in rowdata))