abbrevs = (
    (1 << 50, 'PB'),
    (1 << 40, 'TB'),
    (1 << 30, 'GB'),
    (1 << 20, 'MB'),
    (1 << 10, 'KB'),
    (1, 'bytes')
)


class CheckResult(object):
    critical = 4
    high = 3
    middle = 2
    low = 1

    def __init__(self, catalog, name, score, advise):
        self.catalog = catalog
        self.name = name
        self.score = score
        self.advise = advise

    @staticmethod
    def get_result_template(worker, score):
        return CheckResult(worker.catalog, worker.name, score, None)


def humanize_bytes(bytes, precision=2):
    if bytes == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytes >= factor:
            return '%.*f %s' % (precision, bytes * 1.0 / factor, suffix)