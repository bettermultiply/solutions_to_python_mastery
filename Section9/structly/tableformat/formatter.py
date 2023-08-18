from abc import ABC, abstractmethod


__all__ = ['create_formatter', 'print_table_2']


def print_table(portfolio, attrs: list):
    print(''.join('%10s ' % attr for attr in attrs))
    print(('-'*10+' ')*len(attrs))
    for record in portfolio:
        print(''.join('%10s ' % getattr(record, attr) for attr in attrs))


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        # raise NotImplementedError()
        pass

    @abstractmethod
    def row(self, rowdata):
        # raise NotImplementedError()
        pass


from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter


def print_table_2(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected TableFormatter')
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, field) for field in fields]
        formatter.row(rowdata)


class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


class ColumnFormatMixin:
    formats = []

    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


def create_formatter(formatter: str):
    if formatter.lower() == 'text':
        return TextTableFormatter()
    elif formatter.lower() == 'csv':
        return CSVTableFormatter()
    elif formatter.lower() == 'html':
        return HTMLTableFormatter()
    else:
        raise TypeError('Unknown Format %s' % formatter)


def create_table_2(formatter: str, column_formats=None, upper_headers=False):
    if formatter.lower() == 'text':
        FormatterCls = TextTableFormatter
    elif formatter.lower() == 'csv':
        FormatterCls = CSVTableFormatter
    elif formatter.lower() == 'html':
        FormatterCls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % formatter)

    if column_formats:
        class FormatterCls(ColumnFormatMixin, FormatterCls):
            formats = column_formats

    if upper_headers:
        class FormatterCls(UpperHeadersMixin, FormatterCls):
            pass

    return FormatterCls()
