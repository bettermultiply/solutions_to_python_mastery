from ..formatter import TableFormatter


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('_'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % r for r in rowdata))