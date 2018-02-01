from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter

#    设定item文件列的输出顺序，参考资料如下：
#    https://www.jianshu.com/p/fd6f7eba6abe


class JavBusByScrapyCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter

        fields_to_export = settings.get('FIELDS_TO_EXPORT', [])
        if fields_to_export:
            kwargs['fields_to_export'] = fields_to_export

        super(JavBusByScrapyCsvItemExporter, self).__init__(*args, **kwargs)
